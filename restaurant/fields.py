from django import forms
from django.contrib.postgres.fields import ArrayField


class MultipleChoiceField(forms.MultipleChoiceField):
    """
    Custom field to handle ArrayField with multiple choices
    """

    def __init__(self, *args, **kwargs):
        self.base_field = kwargs.pop('base_field', forms.CharField(max_length=kwargs.pop('max_length')))
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            return []
        elif not isinstance(value, (list, tuple)):
            raise forms.ValidationError(
                'Expected a list'
            )
        return [str(val) for val in value]


class MultipleChoiceArrayField(ArrayField):
    """
    Custom Array field to handle multiple choices
    """

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": MultipleChoiceField,
                "choices": self.base_field.choices,
                "widget": forms.CheckboxSelectMultiple,
                **kwargs,
            }
        )
