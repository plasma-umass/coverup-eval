# file: httpie/config.py:74-79
# asked: {"lines": [74, 75, 76, 77, 78, 79], "branches": [[78, 0], [78, 79]]}
# gained: {"lines": [74, 75, 76, 77, 78, 79], "branches": [[78, 0], [78, 79]]}

import pytest
from pathlib import Path
import errno
from unittest.mock import patch, MagicMock

from httpie.config import BaseConfigDict

@pytest.fixture
def temp_path(tmp_path):
    return tmp_path / "config" / "test_config.json"

def test_ensure_directory_creates_directory(temp_path):
    config = BaseConfigDict(temp_path)
    with patch.object(Path, "mkdir") as mock_mkdir:
        config.ensure_directory()
        mock_mkdir.assert_called_once_with(mode=0o700, parents=True)

def test_ensure_directory_raises_on_unexpected_oserror(temp_path):
    config = BaseConfigDict(temp_path)
    with patch.object(Path, "mkdir", side_effect=OSError(errno.EACCES, "Permission denied")) as mock_mkdir:
        with pytest.raises(OSError) as excinfo:
            config.ensure_directory()
        assert excinfo.value.errno == errno.EACCES

def test_ensure_directory_ignore_exists_error(temp_path):
    config = BaseConfigDict(temp_path)
    with patch.object(Path, "mkdir", side_effect=OSError(errno.EEXIST, "File exists")) as mock_mkdir:
        config.ensure_directory()
        mock_mkdir.assert_called_once_with(mode=0o700, parents=True)
