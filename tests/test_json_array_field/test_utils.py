import pytest

from json_array_field.utils import clean_input_data

params = [
    (
        # Single value
        "test1",
        None,
        ["test1"],
    ),
    (
        # Comma separated values
        "test1,test2",
        None,
        ["test1", "test2"],
    ),
    (
        # Blank string
        "",
        None,
        [],
    ),
    (
        # None/null
        None,
        None,
        [],
    ),
    (
        # None/null with static default
        None,
        ["foo", "bar"],
        ["foo", "bar"],
    ),
    (
        # None/null with callable default
        None,
        lambda: ["foo", "bar"],
        ["foo", "bar"],
    ),
]


class TestCleanInputData:
    @pytest.mark.parametrize("data,default,expected", params)
    def test_func(self, data, default, expected):
        assert clean_input_data(data=data, default=default) == expected

    def test_func_with_unexpected_data_type(self):
        with pytest.raises(TypeError):
            clean_input_data(data=123)
