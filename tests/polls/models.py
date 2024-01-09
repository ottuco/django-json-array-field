from django.db import models

from json_array_field.db.fields import JSONArrayField


class JSONArrayFieldModel(models.Model):
    list_field = JSONArrayField()

    def __str__(self):
        return str(self.list_field)

    def save(self, **kwargs):
        here = 123
        return super().save(**kwargs)
