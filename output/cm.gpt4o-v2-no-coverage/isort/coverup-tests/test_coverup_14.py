# file: isort/exceptions.py:54-60
# asked: {"lines": [54, 55, 57, 58, 59], "branches": []}
# gained: {"lines": [54, 55, 57, 58, 59], "branches": []}

import pytest
from isort.exceptions import FileSkipComment, FileSkipped, ISortError

def test_FileSkipComment():
    file_path = "test_file.py"
    exception = FileSkipComment(file_path)
    
    assert isinstance(exception, FileSkipComment)
    assert isinstance(exception, FileSkipped)
    assert isinstance(exception, ISortError)
    assert str(exception) == f"{file_path} contains an file skip comment and was skipped."
    assert exception.file_path == file_path
