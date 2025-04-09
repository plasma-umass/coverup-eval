# file: httpie/config.py:74-79
# asked: {"lines": [74, 75, 76, 77, 78, 79], "branches": [[78, 0], [78, 79]]}
# gained: {"lines": [74, 75, 76, 77, 78, 79], "branches": [[78, 0], [78, 79]]}

import pytest
from pathlib import Path
import os
import errno
from httpie.config import BaseConfigDict

@pytest.fixture
def temp_path(tmp_path):
    return tmp_path / "config" / "testfile"

def test_ensure_directory_creates_directory(temp_path):
    config = BaseConfigDict(temp_path)
    config.ensure_directory()
    assert temp_path.parent.exists()
    assert oct(temp_path.parent.stat().st_mode & 0o777) == '0o700'

def test_ensure_directory_existing_directory(temp_path, mocker):
    config = BaseConfigDict(temp_path)
    temp_path.parent.mkdir(parents=True, exist_ok=True)
    
    mock_mkdir = mocker.patch("pathlib.Path.mkdir", side_effect=OSError(errno.EEXIST, "File exists"))
    config.ensure_directory()  # Should not raise an exception
    mock_mkdir.assert_called_once_with(mode=0o700, parents=True)

def test_ensure_directory_raises_other_oserror(temp_path, mocker):
    config = BaseConfigDict(temp_path)
    
    mock_mkdir = mocker.patch("pathlib.Path.mkdir", side_effect=OSError(errno.EACCES, "Permission denied"))
    with pytest.raises(OSError) as excinfo:
        config.ensure_directory()
    assert excinfo.value.errno == errno.EACCES
    mock_mkdir.assert_called_once_with(mode=0o700, parents=True)
