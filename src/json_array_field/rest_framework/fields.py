from rest_framework.fields import Field

from ..utils import clean_input_data


class JSONArrayField(Field):
    def to_internal_value(self, data):
        return clean_input_data(data, self.default)

    def to_representation(self, value):
        return value
