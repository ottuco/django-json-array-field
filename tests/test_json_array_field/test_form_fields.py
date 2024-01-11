import pytest

from tests.params import params_form
from tests.polls.forms import JSONArrayForm, JSONArrayModelForm
from tests.polls.models import JSONArrayFieldModel

pytestmark = pytest.mark.django_db


class TestJSONArrayModelForm:
    @pytest.mark.parametrize("list_field, expected_out", params_form)
    def test_create(self, list_field, expected_out):
        form = JSONArrayModelForm(data={"list_field": list_field})
        assert form.is_valid()
        obj = form.save()
        assert obj.list_field == expected_out

    @pytest.mark.parametrize("list_field, expected_out", params_form)
    def test_update(self, list_field, expected_out):
        obj = JSONArrayFieldModel.objects.create(list_field=["foo", "bar"])
        assert obj.list_field == ["foo", "bar"]
        form = JSONArrayModelForm(data={"list_field": list_field}, instance=obj)
        assert form.is_valid()
        obj = form.save()
        assert obj.list_field == expected_out


class TestJSONArrayForm:
    @pytest.mark.parametrize("list_field, expected_out", params_form)
    def test_create_cleaned_data(self, list_field, expected_out):
        form = JSONArrayForm(data={"list_field": list_field})
        assert form.is_valid()
        assert form.cleaned_data["list_field"] == expected_out
