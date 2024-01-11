def str_to_list(value: str) -> list:
    return list(filter(None, map(str.strip, value.split(","))))
