# file isort/exceptions.py:54-60
# lines [54, 55, 57, 58, 59]
# branches []

import pytest

from isort.exceptions import FileSkipComment

def test_file_skip_comment_exception():
    file_path = "test_file.py"
    try:
        raise FileSkipComment(file_path)
    except FileSkipComment as e:
        assert str(e) == f"{file_path} contains an file skip comment and was skipped."
        assert e.file_path == file_path
