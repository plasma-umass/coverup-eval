# file isort/exceptions.py:35-43
# lines [35, 36, 38, 39, 40, 41, 43]
# branches []

import pytest
from isort.exceptions import IntroducedSyntaxErrors

def test_introduced_syntax_errors():
    file_path = "test_file.py"
    error = IntroducedSyntaxErrors(file_path)
    
    assert isinstance(error, IntroducedSyntaxErrors)
    assert error.file_path == file_path
    assert str(error) == f"isort introduced syntax errors when attempting to sort the imports contained within {file_path}."
