from typing import Any

from django import forms


class JSONArrayFormField(forms.CharField):
    def prepare_value(self, value: Any) -> Any:
        if isinstance(value, list):
            return ",".join(map(str, value))
        return value
