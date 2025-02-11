import json
from typing import Dict, List, Optional, Set, Tuple

from django.apps import apps
from django.db.models import Model
from django.core import serializers
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Dump selected data to a file based on app, model, and field specifications."

    def add_arguments(self, parser):
        parser.add_argument(
            "args",
            metavar="app_label[.ModelName][.Field]",
            nargs="*",
            help=(
                "Restricts dumped data to the specified app_label, "
                "app_label.ModelName, or app_label.ModelName.Field."
            ),
        )
        parser.add_argument(
            "-o", "--output", help="Specifies file to which the output is written."
        )

    def handle(self, *args, **options):
        output_file = options.get("output")
        models_to_serialize = self._parse_arguments(args)

        if not models_to_serialize:
            self.stderr.write("No valid models or fields specified.")
            return

        serialized_data = self._serialize_models(models_to_serialize)
        self._write_output(serialized_data, output_file)

    def _parse_arguments(self, args: List[str]) -> Dict[Model, Optional[Set[str]]]:
        """
        Parse input arguments and return a dictionary mapping models to their fields.
        """
        models_to_serialize: Dict[Model, Optional[Set[str]]] = {}

        for arg in args:
            app_label, model_name, field_name = self._parse_argument(arg)

            if not app_label:
                self.stderr.write(f"Invalid argument format: {arg}. Skipping.")
                continue

            try:
                app_config = apps.get_app_config(app_label)
            except LookupError:
                self.stderr.write(f"App '{app_label}' not found. Skipping.")
                continue

            models = self._get_models_for_app_config(app_config, model_name)
            if not models:
                continue

            self._update_models_to_serialize(models_to_serialize, models, field_name)

        return models_to_serialize

    def _parse_argument(self, arg: str) -> Tuple[str, Optional[str], Optional[str]]:
        """
        Parse a single argument into app_label, model_name, and field_name.
        """
        parts = arg.split(".", 2)
        app_label = parts[0]
        model_name = parts[1] if len(parts) >= 2 else None
        field_name = parts[2] if len(parts) >= 3 else None
        return app_label, model_name, field_name

    def _get_models_for_app_config(self, app_config, model_name: Optional[str] = None) -> List[Model]:
        """
        Retrieve models from an app config based on the model name.
        """
        if model_name:
            try:
                return [app_config.get_model(model_name)]
            except LookupError:
                self.stderr.write(f"Model '{app_config.label}.{model_name}' not found. Skipping.")
                return []
        else:
            return list(app_config.get_models())

    def _update_models_to_serialize(self, models_to_serialize: Dict[Model, Optional[Set[str]]], models: List[Model],
                                    field_name: Optional[str]) -> None:
        """
        Update the models_to_serialize dictionary with the specified fields.
        """
        for model in models:
            current_fields = models_to_serialize.get(model, set(field_name))

            if current_fields is None:
                continue  # Already set to all fields

            if field_name:
                new_fields = set() if current_fields is None else current_fields.copy()
                new_fields.add(field_name)
                models_to_serialize[model] = new_fields
            else:
                models_to_serialize[model] = None  # Set to all fields

    def _serialize_models(self, models_to_serialize: Dict[Model, Optional[Set[str]]]) -> List[dict]:
        """
        Serialize the specified models and fields.
        """
        serialized_data = []

        for model, fields in models_to_serialize.items():
            fields_list = list(fields) if fields is not None else None
            queryset = model.objects.all()

            try:
                serialized = serializers.serialize("python", queryset, fields=fields_list)
                serialized_data.extend(serialized)
            except Exception as e:
                self.stderr.write(f"Error serializing {model._meta.label}: {e}")

        return serialized_data

    def _write_output(self, data: List[dict], output_file: Optional[str]) -> None:
        """
        Write the serialized data to the specified output file or stdout.
        """
        if output_file:
            with open(output_file, "w") as f:
                json.dump(data, f, indent=2)
            self.stdout.write(self.style.SUCCESS(f"Data successfully written to {output_file}"))
        else:
            self.stdout.write(json.dumps(data, indent=2))
