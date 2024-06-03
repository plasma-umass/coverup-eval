# file isort/exceptions.py:54-60
# lines [54, 55, 57, 58, 59]
# branches []

import pytest
from isort.exceptions import FileSkipComment

def test_file_skip_comment():
    file_path = "test_file.py"
    exception = FileSkipComment(file_path)
    
    assert isinstance(exception, FileSkipComment)
    assert str(exception) == f"{file_path} contains an file skip comment and was skipped."
    assert exception.file_path == file_path
