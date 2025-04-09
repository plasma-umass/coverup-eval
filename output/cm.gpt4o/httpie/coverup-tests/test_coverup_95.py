# file httpie/config.py:123-128
# lines [124, 125, 126, 127, 128]
# branches ['127->exit', '127->128']

import pytest
import errno
from unittest import mock
from httpie.config import BaseConfigDict

def test_baseconfigdict_delete_oserror(mocker):
    # Create an instance of BaseConfigDict with a mock path
    config_dict = BaseConfigDict(path=mocker.Mock())
    
    # Mock the path attribute to simulate the file path
    mock_path = config_dict.path
    
    # Simulate an OSError with errno set to something other than ENOENT
    mock_path.unlink.side_effect = OSError(errno.EACCES, "Permission denied")
    
    # Verify that the OSError is raised
    with pytest.raises(OSError) as excinfo:
        config_dict.delete()
    
    assert excinfo.value.errno == errno.EACCES
    
    # Simulate an OSError with errno set to ENOENT
    mock_path.unlink.side_effect = OSError(errno.ENOENT, "No such file or directory")
    
    # Verify that no exception is raised
    config_dict.delete()
    
    # Ensure that unlink was called twice
    assert mock_path.unlink.call_count == 2
