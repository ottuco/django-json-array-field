from django import forms

from json_array_field.utils import str_to_list


class JSONArrayFormField(forms.CharField):
    def clean(self, value):
        value = super().clean(value)
        return str_to_list(value=value)
