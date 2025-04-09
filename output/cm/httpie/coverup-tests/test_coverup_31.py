# file httpie/config.py:123-128
# lines [123, 124, 125, 126, 127, 128]
# branches ['127->exit', '127->128']

import errno
import pytest
from pathlib import Path
from unittest.mock import Mock
from httpie.config import BaseConfigDict

def test_base_config_dict_delete_file_exists(tmp_path):
    # Setup: create a temporary file
    temp_file = tmp_path / 'temp_config.json'
    temp_file.touch()

    # Mock the path attribute in BaseConfigDict
    config_dict = BaseConfigDict(path=temp_file)

    # Test: delete the file
    config_dict.delete()

    # Assert: the file should be deleted
    assert not temp_file.exists()

def test_base_config_dict_delete_file_does_not_exist(tmp_path):
    # Setup: create a path that does not exist
    non_existent_file = tmp_path / 'non_existent_config.json'

    # Mock the path attribute in BaseConfigDict
    config_dict = BaseConfigDict(path=non_existent_file)

    # Test: try to delete the non-existent file
    config_dict.delete()

    # Assert: nothing should happen, no exception should be raised

def test_base_config_dict_delete_os_error(tmp_path):
    # Setup: create a mock path that will raise an OSError with a specific errno
    mock_path = Mock()
    mock_path.unlink.side_effect = OSError(errno.EACCES, 'Permission denied')

    # Mock the path attribute in BaseConfigDict
    config_dict = BaseConfigDict(path=mock_path)

    # Test and Assert: OSError with errno other than ENOENT should be raised
    with pytest.raises(OSError) as exc_info:
        config_dict.delete()
    assert exc_info.value.errno == errno.EACCES
