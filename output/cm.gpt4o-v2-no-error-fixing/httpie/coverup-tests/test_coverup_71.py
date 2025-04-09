# file: httpie/config.py:74-79
# asked: {"lines": [75, 76, 77, 78, 79], "branches": [[78, 0], [78, 79]]}
# gained: {"lines": [75, 76, 77, 78, 79], "branches": [[78, 79]]}

import pytest
from pathlib import Path
import errno
from unittest.mock import patch, MagicMock

from httpie.config import BaseConfigDict

@pytest.fixture
def temp_path(tmp_path):
    return tmp_path / "config" / "testfile"

def test_ensure_directory_creates_directory(temp_path):
    config = BaseConfigDict(temp_path)
    config.ensure_directory()
    assert temp_path.parent.is_dir()

def test_ensure_directory_handles_existing_directory(temp_path):
    config = BaseConfigDict(temp_path)
    temp_path.parent.mkdir(parents=True)
    with patch("pathlib.Path.mkdir") as mock_mkdir:
        config.ensure_directory()
        mock_mkdir.assert_called_once_with(mode=0o700, parents=True)

def test_ensure_directory_raises_on_other_oserror(temp_path):
    config = BaseConfigDict(temp_path)
    with patch("pathlib.Path.mkdir", side_effect=OSError(errno.EACCES, "Permission denied")):
        with pytest.raises(OSError) as excinfo:
            config.ensure_directory()
        assert excinfo.value.errno == errno.EACCES
