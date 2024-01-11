params_form = [
    (
        # Single value
        "Admin",
        ["Admin"],
    ),
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
]

params = [
    *params_form,
    # Additional params that can be used directly with the model or via APIs
    (
        # with python-list
        ["Admin", "Editor", "Author"],
        ["Admin", "Editor", "Author"],
    ),
]

params_with_null_and_blank = [
    *params,
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
