import pytest

from tests.params import params
from tests.polls.models import JSONArrayFieldModel
from tests.polls.serializers import JSONArrayModelSerializer, JSONArraySerializer

pytestmark = pytest.mark.django_db


class TestJSONArrayModelSerializer:
    @pytest.mark.parametrize("list_field, expected_out", params)
    def test_create(self, list_field, expected_out):
        serializer = JSONArrayModelSerializer(data={"list_field": list_field})
        assert serializer.is_valid()
        obj = serializer.save()
        assert obj.list_field == expected_out
        assert serializer.data["list_field"] == expected_out

    @pytest.mark.parametrize("list_field, expected_out", params)
    def test_update(self, list_field, expected_out):
        obj = JSONArrayFieldModel.objects.create(list_field=["foo", "bar"])
        assert obj.list_field == ["foo", "bar"]

        serializer = JSONArrayModelSerializer(
            data={"list_field": list_field},
            instance=obj,
        )
        assert serializer.is_valid()
        obj = serializer.save()
        assert obj.list_field == expected_out
        assert serializer.data["list_field"] == expected_out


class TestJSONArraySerializer:
    @pytest.mark.parametrize("list_field, expected_out", params)
    def test_normal_serializer(self, list_field, expected_out):
        serializer = JSONArraySerializer(data={"list_field": list_field})
        assert serializer.is_valid()
        assert serializer.validated_data == {"list_field": expected_out}
        assert serializer.data == {"list_field": expected_out}
