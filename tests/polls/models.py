from django.db import models

from json_array_field.db.fields import JSONArrayField


class JSONArrayFieldModel(models.Model):
    list_field = JSONArrayField()

    def __str__(self):
        return str(self.list_field)


# class JSONArrayWithDefault(models.Model):
#     list_field = JSONArrayField(default=list)
#
#     def __str__(self):
#         return str(self.list_field)
#
#
# class JSONArrayBlank(models.Model):
#     list_field = JSONArrayField(blank=True)
#
#     def __str__(self):
#         return str(self.list_field)
#
#
# class JSONArrayNull(models.Model):
#     list_field = JSONArrayField(null=True)
#
#     def __str__(self):
#         return str(self.list_field)
