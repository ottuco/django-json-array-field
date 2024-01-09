# django-array-field

[![PyPI version](https://img.shields.io/pypi/v/django-array-field.svg)](https://pypi.python.org/pypi/django-array-field)

## Installation

```bash
pip install django-array-field
```

## Test

```bash
# Install the dependencies
pip install .[test]

# Run tests
python -m pytest
```

## Release
```base
# do a dry-run first -
bump2version --dry-run --verbose [major|minor|patch]

# if everything looks good, run the following command to release
bump2version --verbose [major|minor|patch]

# push the changes to remote
git push origin master --tags
```
