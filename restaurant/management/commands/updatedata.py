import json
from typing import Dict, List, Optional, Tuple

from django.apps import apps
from django.db.models import Model
from django.core.management.base import BaseCommand
from django.core.exceptions import FieldDoesNotExist


class Command(BaseCommand):
    help = (
        "Load data from a JSON file and update existing database records "
        "without creating new instances."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "input_file",
            help="Path to the JSON file containing data to load.",
        )

    def handle(self, *args, **options):
        input_file = options["input_file"]
        updated_count = 0
        skipped_count = 0

        # Load data from the file
        data = self._load_data(input_file)
        if data is None:
            return  # Exit if data loading fails

        # Process each entry in the data
        for entry in data:
            model_str, pk, fields = self._parse_entry(entry)
            if not model_str or pk is None:
                skipped_count += 1
                continue

            # Get the model and instance
            model = self._get_model(model_str)
            if model is None:
                skipped_count += 1
                continue

            instance = self._get_instance(model, pk)
            if instance is None:
                self.stdout.write(
                    self.style.NOTICE(f"Skipping {model_str} pk={pk} - does not exist")
                )
                skipped_count += 1
                continue

            # Update the instance
            if self._update_instance(instance, fields):
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Updated {model_str} pk={pk}"))
            else:
                skipped_count += 1

        # Print summary
        self.stdout.write(
            self.style.SUCCESS(
                f"\nOperation complete. Updated: {updated_count}, Skipped: {skipped_count}"
            )
        )

    def _load_data(self, input_file: str) -> Optional[List[Dict]]:
        """Load JSON data from the input file."""
        try:
            with open(input_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File '{input_file}' not found"))
        except json.JSONDecodeError:
            self.stderr.write(self.style.ERROR(f"Invalid JSON in '{input_file}'"))
        return None

    def _parse_entry(self, entry: Dict) -> Tuple[Optional[str], Optional[int], Dict]:
        """Parse an entry into model string, primary key, and fields."""
        model_str = entry.get("model")
        pk = entry.get("pk")
        fields = entry.get("fields", {})
        return model_str, pk, fields

    def _get_model(self, model_str: str) -> Optional[Model]:
        """Retrieve the model class from the app label and model name."""
        try:
            app_label, model_name = model_str.split(".")
            return apps.get_model(app_label, model_name)
        except (ValueError, LookupError) as e:
            self.stderr.write(
                self.style.WARNING(f"Skipping invalid model '{model_str}': {e}"))
            return None

    def _get_instance(self, model: Model, pk: int) -> Optional[Model]:
        """Retrieve an existing instance of the model by primary key."""
        try:
            return model.objects.filter(pk=pk).first()
        except Exception as e:
            self.stderr.write(
                self.style.WARNING(f"Error looking up {model._meta.label} pk={pk}: {e}"))
            return None

    def _update_instance(self, instance: Model, fields: Dict) -> bool:
        """Update an instance with the provided fields."""
        regular_fields, m2m_fields = self._separate_fields(instance, fields)

        # Update regular fields
        for field, value in regular_fields.items():
            setattr(instance, field, value)

        try:
            instance.save()
        except Exception as e:
            self.stderr.write(
                self.style.WARNING(f"Error saving {instance._meta.label} pk={instance.pk}: {e}"))
            return False

        # Update M2M fields
        for field_name, pks in m2m_fields.items():
            try:
                manager = getattr(instance, field_name)
                manager.set(pks)
            except Exception as e:
                self.stderr.write(
                    self.style.WARNING(
                        f"Error updating M2M field '{field_name}' for {instance._meta.label} pk={instance.pk}: {e}"
                    )
                )

        return True

    def _separate_fields(self, instance: Model, fields: Dict) -> Tuple[Dict, Dict]:
        """Separate regular fields from M2M fields."""
        regular_fields = {}
        m2m_fields = {}

        for field_name, value in fields.items():
            try:
                field = instance._meta.get_field(field_name)
                if field.many_to_many:
                    m2m_fields[field_name] = value
                else:
                    regular_fields[field_name] = value
            except FieldDoesNotExist:
                self.stderr.write(
                    self.style.WARNING(
                        f"Skipping invalid field '{field_name}' in {instance._meta.label}"
                    )
                )

        return regular_fields, m2m_fields
