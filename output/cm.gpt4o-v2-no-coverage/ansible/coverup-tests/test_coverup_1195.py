# file: lib/ansible/config/manager.py:306-314
# asked: {"lines": [313, 314], "branches": [[310, 313]]}
# gained: {"lines": [313, 314], "branches": [[310, 313]]}

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

def test_read_config_yaml_file_success(config_manager):
    mock_yaml_content = b"key: value"
    expected_result = {"key": "value"}

    with patch("builtins.open", mock_open(read_data=mock_yaml_content)), \
         patch("os.path.exists", return_value=True), \
         patch("ansible.module_utils.common.yaml.yaml_load", return_value=expected_result):
        result = config_manager._read_config_yaml_file("/path/to/config.yml")
        assert result == expected_result

def test_read_config_yaml_file_file_not_found(config_manager):
    with patch("os.path.exists", return_value=False), \
         patch("ansible.module_utils._text.to_bytes", side_effect=to_bytes), \
         patch("ansible.module_utils._text.to_native", side_effect=to_native):
        with pytest.raises(AnsibleError) as excinfo:
            config_manager._read_config_yaml_file("/path/to/missing_config.yml")
        assert "Missing base YAML definition file (bad install?):" in str(excinfo.value)

def test_read_config_yaml_file_empty_yaml(config_manager):
    mock_yaml_content = b""
    expected_result = {}

    with patch("builtins.open", mock_open(read_data=mock_yaml_content)), \
         patch("os.path.exists", return_value=True), \
         patch("ansible.module_utils.common.yaml.yaml_load", return_value=None):
        result = config_manager._read_config_yaml_file("/path/to/empty_config.yml")
        assert result == expected_result
