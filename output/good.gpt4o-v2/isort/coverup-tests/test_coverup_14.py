# file: isort/exceptions.py:46-51
# asked: {"lines": [46, 47, 49, 50, 51], "branches": []}
# gained: {"lines": [46, 47, 49, 50, 51], "branches": []}

import pytest
from isort.exceptions import FileSkipped, ISortError

def test_file_skipped_exception():
    message = "File has been skipped"
    file_path = "/path/to/skipped/file"
    
    exception = FileSkipped(message, file_path)
    
    assert isinstance(exception, ISortError)
    assert str(exception) == message
    assert exception.file_path == file_path
