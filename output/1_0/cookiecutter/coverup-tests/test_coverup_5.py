# file cookiecutter/exceptions.py:157-163
# lines [157, 158]
# branches []

import pytest
from cookiecutter.exceptions import InvalidZipRepository

def test_invalid_zip_repository_exception():
    with pytest.raises(InvalidZipRepository) as exc_info:
        raise InvalidZipRepository("Invalid zip repository")

    assert str(exc_info.value) == "Invalid zip repository"
