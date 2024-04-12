# file isort/exceptions.py:35-43
# lines [35, 36, 38, 39, 40, 41, 43]
# branches []

import pytest

from isort.exceptions import IntroducedSyntaxErrors

def test_introduced_syntax_errors_exception():
    file_path = "some_file.py"
    try:
        raise IntroducedSyntaxErrors(file_path)
    except IntroducedSyntaxErrors as e:
        assert str(e) == "isort introduced syntax errors when attempting to sort the imports contained within some_file.py."
        assert e.file_path == file_path
