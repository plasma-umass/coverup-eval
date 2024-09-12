# file: httpie/config.py:123-128
# asked: {"lines": [124, 125, 126, 127, 128], "branches": [[127, 0], [127, 128]]}
# gained: {"lines": [124, 125, 126, 127, 128], "branches": [[127, 0], [127, 128]]}

import pytest
from pathlib import Path
import errno
from httpie.config import BaseConfigDict

@pytest.fixture
def temp_file(tmp_path):
    temp_file = tmp_path / "temp_file"
    temp_file.touch()
    return temp_file

def test_delete_file_exists(temp_file):
    config = BaseConfigDict(temp_file)
    config.delete()
    assert not temp_file.exists()

def test_delete_file_not_exists(temp_file):
    config = BaseConfigDict(temp_file)
    temp_file.unlink()
    config.delete()  # Should not raise an exception
    assert not temp_file.exists()

def test_delete_raises_oserror(mocker, temp_file):
    mock_unlink = mocker.patch("pathlib.Path.unlink", side_effect=OSError(errno.EACCES, "Permission denied"))
    config = BaseConfigDict(temp_file)
    
    with pytest.raises(OSError) as excinfo:
        config.delete()
    
    assert excinfo.value.errno == errno.EACCES
