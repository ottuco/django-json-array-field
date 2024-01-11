from rest_framework import serializers

from json_array_field.rest_framework.fields import JSONArrayField
from tests.polls.models import JSONArrayFieldModel


class JSONArraySerializer(serializers.Serializer):
    list_field = JSONArrayField()


class JSONArrayModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JSONArrayFieldModel
        fields = "__all__"
