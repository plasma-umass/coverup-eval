# file: httpie/config.py:123-128
# asked: {"lines": [124, 125, 126, 127, 128], "branches": [[127, 0], [127, 128]]}
# gained: {"lines": [124, 125, 126, 127, 128], "branches": [[127, 0], [127, 128]]}

import pytest
import errno
from pathlib import Path
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

def test_delete_file_not_exists(mocker):
    mock_path = mocker.Mock()
    mock_path.unlink.side_effect = OSError(errno.ENOENT, "No such file or directory")
    config = BaseConfigDict(mock_path)
    config.delete()
    mock_path.unlink.assert_called_once()

def test_delete_other_oserror(mocker):
    mock_path = mocker.Mock()
    mock_path.unlink.side_effect = OSError(errno.EACCES, "Permission denied")
    config = BaseConfigDict(mock_path)
    with pytest.raises(OSError) as excinfo:
        config.delete()
    assert excinfo.value.errno == errno.EACCES
    mock_path.unlink.assert_called_once()
