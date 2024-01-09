import pytest

from tests.polls.models import JSONArrayFieldModel

pytestmark = pytest.mark.django_db

params = [
    (
        # Normal
        "Admin, Editor, Author",
        ["Admin", "Editor", "Author"],
    ),
    (
        # Whitespace
        "Admin,     Editor,Author, ",
        ["Admin", "Editor", "Author"],
    ),
    (
        # With double-quotes
        '"Admin", "Editor", "Author"',
        ['"Admin"', '"Editor"', '"Author"'],
    ),
    (
        # With single-quotes
        "'Admin', 'Editor', 'Author'",
        ["'Admin'", "'Editor'", "'Author'"],
    ),
    (
        # with string-list representation
        '["Admin", "Editor", "Author"]',
        ['["Admin"', '"Editor"', '"Author"]'],
    ),
    (
        # with python-list
        ["Admin", "Editor", "Author"],
        ["Admin", "Editor", "Author"],
    ),
]


class TestJSONArrayFieldModel:
    @pytest.mark.parametrize("list_field, expected_out", params)
    def test_create_using_manager(self, list_field, expected_out):
        instance = JSONArrayFieldModel.objects.create(list_field=list_field)

        assert instance.list_field == expected_out

        # Pull data from the database
        instance = JSONArrayFieldModel.objects.get(pk=instance.pk)
        assert instance.list_field == expected_out

    @pytest.mark.parametrize("list_field, expected_out", params)
    def test_create_using_constructor(self, list_field, expected_out):
        instance = JSONArrayFieldModel(list_field=list_field)
        instance.save()

        assert instance.list_field == expected_out

        # Pull data from the database
        instance = JSONArrayFieldModel.objects.get(pk=instance.pk)
        assert instance.list_field == expected_out

    @pytest.mark.parametrize("list_field, expected_out", params)
    def test_assigning_value_using_constructor(self, list_field, expected_out):
        instance = JSONArrayFieldModel()
        instance.list_field = list_field
        instance.save()

        assert instance.list_field == expected_out

        # Pull data from the database
        instance = JSONArrayFieldModel.objects.get(pk=instance.pk)
        assert instance.list_field == expected_out
