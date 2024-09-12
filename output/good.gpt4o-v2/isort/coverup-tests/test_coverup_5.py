# file: isort/exceptions.py:24-32
# asked: {"lines": [24, 25, 27, 28, 29, 30, 32], "branches": []}
# gained: {"lines": [24, 25, 27, 28, 29, 30, 32], "branches": []}

import pytest
from isort.exceptions import ExistingSyntaxErrors

def test_existing_syntax_errors():
    file_path = "dummy_path.py"
    exception = ExistingSyntaxErrors(file_path)
    
    assert isinstance(exception, ExistingSyntaxErrors)
    assert str(exception) == f"isort was told to sort imports within code that contains syntax errors: {file_path}."
    assert exception.file_path == file_path
