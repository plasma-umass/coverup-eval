# file httpie/config.py:74-79
# lines [74, 75, 76, 77, 78, 79]
# branches ['78->exit', '78->79']

import errno
import pytest
from unittest.mock import MagicMock
from httpie.config import BaseConfigDict

@pytest.fixture
def mock_path(mocker):
    mock_path = MagicMock()
    mock_path.parent.mkdir = MagicMock()
    return mock_path

def test_ensure_directory_creates_directory(mock_path):
    config_dict = BaseConfigDict(path=mock_path)

    config_dict.ensure_directory()

    mock_path.parent.mkdir.assert_called_once_with(mode=0o700, parents=True)

def test_ensure_directory_existing_directory(mock_path):
    mock_path.parent.mkdir.side_effect = OSError(errno.EEXIST, 'Directory exists')

    config_dict = BaseConfigDict(path=mock_path)

    config_dict.ensure_directory()

    mock_path.parent.mkdir.assert_called_once_with(mode=0o700, parents=True)

def test_ensure_directory_raises_exception(mock_path):
    mock_path.parent.mkdir.side_effect = OSError(errno.EACCES, 'Permission denied')

    config_dict = BaseConfigDict(path=mock_path)

    with pytest.raises(OSError) as exc_info:
        config_dict.ensure_directory()

    assert exc_info.value.errno == errno.EACCES
    assert str(exc_info.value) == '[Errno 13] Permission denied'

    mock_path.parent.mkdir.assert_called_once_with(mode=0o700, parents=True)
