def str_to_list(value: str) -> list:
    return list(filter(None, map(str.strip, value.split(","))))


def clean_input_data(data, default=None):
    if not data:
        # data is either blank or None
        #
        # If data is blank, then we should return an empty list.
        if default is None:
            return []

        # Check whether the `default` is callable or not.
        # If it's callable, then call it and return the result.
        if callable(default):
            return default()
        return default

    if isinstance(data, str):
        return str_to_list(value=data)
    if isinstance(data, list):
        return data
    raise TypeError("Invalid type of data. Expected a string or list.")
