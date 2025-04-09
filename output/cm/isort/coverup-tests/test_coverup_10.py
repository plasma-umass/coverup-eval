# file isort/exceptions.py:46-51
# lines [46, 47, 49, 50, 51]
# branches []

import pytest
from isort.exceptions import FileSkipped

def test_file_skipped_exception():
    message = "Test message"
    file_path = "/path/to/skipped/file.py"
    
    try:
        raise FileSkipped(message, file_path)
    except FileSkipped as e:
        assert str(e) == message
        assert e.file_path == file_path
