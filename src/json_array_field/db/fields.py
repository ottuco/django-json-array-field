from typing import Any

from django.db.models import JSONField
from django.forms import Field as FormField

from ..forms.fields import JSONArrayFormField
from ..utils import str_to_list


class JSONArrayField(JSONField):
    """
    An alternative solution to `django_mysql.models.List[Char|Text]Field`
    """

    def __init__(self, *args, **kwargs) -> None:
        kwargs.setdefault("default", list)
        self.validate_default_type(default=kwargs["default"])
        super().__init__(*args, **kwargs)

    def validate_default_type(self, default: Any) -> None:
        if callable(default):
            default = default()
        if not isinstance(default, list):
            raise TypeError("Default value must be a list")

    def clean_input(self, value: Any) -> list:
        if not value:
            return self.get_default() or []
        if isinstance(value, str):
            return str_to_list(value=value)
        return value

    def pre_save(self, model_instance, add) -> list:
        """
        The `to_python(...)` method doesn't get called when we assign values directly to
        the field. But, we really need to convert the strings into arrays.
        So, we have to use the `pre_save(...)` method

        Example:

        # models.py
        class Person(models.Model):
            groups = JSONArrayField(default=list)

        # Usage

            jpg = Person()
            jpg.groups = "Admin, Editor, Author"
            jpg.save()

        # OR

            jpg = Person.objects.create(groups="Admin, Editor, Author")

        # Drawback
        The `clean_input(...)` method will get called more than once if we try to save
        the data using forms. Because, the form's `is_valid()` method will call
        the `clean()` method of the model, and it will call the `to_python()` method
        and thus the `clean_input()` method.

        """
        value = super().pre_save(model_instance, add)
        value = self.clean_input(value=value)

        # Set the new value to the model instance.
        # This will ensure that the returned object will have the correct value.
        setattr(model_instance, self.attname, value)

        return value

    def formfield(self, **kwargs) -> FormField:
        defaults = {
            "form_class": JSONArrayFormField,
        }
        return super(JSONField, self).formfield(**defaults)
