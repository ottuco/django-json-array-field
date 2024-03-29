import pytest

from json_array_field.db.fields import JSONArrayField
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
    (
        # Null
        None,
        [],
    ),
    (
        # empty
        [],
        [],
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

    def test_default_value_non_a_list(self):
        with pytest.raises(TypeError):
            JSONArrayField(default=dict)

    def test_default_value_callable(self):
        def callable_default():
            return []

        JSONArrayField(default=callable_default)

    def test_default_value_callable_non_a_list(self):
        def callable_default():
            return dict()

        with pytest.raises(TypeError):
            JSONArrayField(default=callable_default)

    def test_default_value_with_static(self):
        JSONArrayField(default=["Admin"])
