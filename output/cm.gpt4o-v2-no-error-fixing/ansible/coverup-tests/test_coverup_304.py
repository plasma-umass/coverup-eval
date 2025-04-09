# file: lib/ansible/config/manager.py:306-314
# asked: {"lines": [306, 309, 310, 311, 312, 313, 314], "branches": [[310, 311], [310, 313]]}
# gained: {"lines": [306, 309, 310, 311, 312, 313, 314], "branches": [[310, 311], [310, 313]]}

import os
import pytest
from unittest.mock import mock_open, patch
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_bytes, to_native
from ansible.module_utils.common.yaml import yaml_load
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_read_config_yaml_file_exists(config_manager):
    mock_yaml_content = b"key: value"
    with patch("builtins.open", mock_open(read_data=mock_yaml_content)) as mock_file:
        with patch("os.path.exists", return_value=True):
            with patch("ansible.module_utils.common.yaml.yaml_load", return_value={"key": "value"}):
                result = config_manager._read_config_yaml_file("/fake/path/config.yml")
                mock_file.assert_called_once_with(to_bytes("/fake/path/config.yml"), 'rb')
                assert result == {"key": "value"}

def test_read_config_yaml_file_not_exists(config_manager):
    with patch("os.path.exists", return_value=False):
        with pytest.raises(AnsibleError) as excinfo:
            config_manager._read_config_yaml_file("/fake/path/config.yml")
        assert "Missing base YAML definition file (bad install?): /fake/path/config.yml" in str(excinfo.value)
