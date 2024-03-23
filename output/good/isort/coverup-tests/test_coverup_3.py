# file isort/exceptions.py:24-32
# lines [24, 25, 27, 28, 29, 30, 32]
# branches []

import pytest
from isort.exceptions import ExistingSyntaxErrors

def test_existing_syntax_errors_exception():
    file_path = "example.py"
    try:
        raise ExistingSyntaxErrors(file_path)
    except ExistingSyntaxErrors as e:
        assert str(e) == "isort was told to sort imports within code that contains syntax errors: example.py."
        assert e.file_path == file_path
