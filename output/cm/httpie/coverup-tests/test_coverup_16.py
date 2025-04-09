# file httpie/config.py:84-97
# lines [84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 95, 96, 97]
# branches ['96->exit', '96->97']

import errno
import json
import pytest
from pathlib import Path
from unittest.mock import mock_open, patch

# Assuming the ConfigFileError is defined somewhere in httpie.config
from httpie.config import ConfigFileError, BaseConfigDict

class TestConfig(BaseConfigDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def test_config_load_ioerror(tmp_path):
    # Test to cover the IOError branch that is not ENOENT
    test_path = tmp_path / 'config.json'
    test_path.touch()
    with patch.object(Path, 'open', side_effect=IOError(errno.EACCES, 'Permission denied')):
        config = TestConfig(path=test_path)
        with pytest.raises(ConfigFileError) as excinfo:
            config.load()
        assert 'cannot read testconfig file: [Errno 13] Permission denied' in str(excinfo.value)

def test_config_load_valueerror(tmp_path):
    # Test to cover the ValueError branch
    test_path = tmp_path / 'config.json'
    test_path.write_text('{not valid json}')
    config = TestConfig(path=test_path)
    with pytest.raises(ConfigFileError) as excinfo:
        config.load()
    assert 'invalid testconfig file' in str(excinfo.value)

def test_config_load_success(tmp_path):
    # Test to cover the successful load branch
    valid_json = '{"key": "value"}'
    test_path = tmp_path / 'config.json'
    test_path.write_text(valid_json)
    config = TestConfig(path=test_path)
    config.load()
    assert config['key'] == 'value'
