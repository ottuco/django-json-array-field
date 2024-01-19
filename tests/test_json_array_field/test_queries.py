import pytest

from tests.polls.models import JSONArrayFieldModel

pytestmark = pytest.mark.django_db


class TestDBQueries:
    def test_icontains(self):
        data = [
            "Admin, Editor, Author",
            ["Administrator", "Editorial", "Authorized"],
        ]
        for list_field in data:
            JSONArrayFieldModel.objects.create(list_field=list_field)

        # Pull data from the database
        qs = JSONArrayFieldModel.objects.filter(list_field__icontains="Editor")
        assert qs.count() == 2
        qs = JSONArrayFieldModel.objects.filter(list_field__icontains="Authori")
        assert qs.count() == 1
