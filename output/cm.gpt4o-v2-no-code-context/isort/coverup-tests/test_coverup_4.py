# file: isort/exceptions.py:35-43
# asked: {"lines": [35, 36, 38, 39, 40, 41, 43], "branches": []}
# gained: {"lines": [35, 36, 38, 39, 40, 41, 43], "branches": []}

import pytest
from isort.exceptions import ISortError, IntroducedSyntaxErrors

def test_introduced_syntax_errors():
    file_path = "test_file.py"
    error = IntroducedSyntaxErrors(file_path)
    
    assert isinstance(error, ISortError)
    assert str(error) == f"isort introduced syntax errors when attempting to sort the imports contained within {file_path}."
    assert error.file_path == file_path
