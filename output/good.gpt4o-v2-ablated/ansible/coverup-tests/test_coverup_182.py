# file: lib/ansible/config/manager.py:306-314
# asked: {"lines": [306, 309, 310, 311, 312, 313, 314], "branches": [[310, 311], [310, 313]]}
# gained: {"lines": [306, 309, 310, 311, 312, 313, 314], "branches": [[310, 311], [310, 313]]}

import os
import pytest
from unittest import mock
from ansible.errors import AnsibleError
from ansible.config.manager import ConfigManager
from ansible.module_utils._text import to_bytes, to_native
import yaml

# Mocking yaml_load function
def yaml_load(stream):
    return yaml.safe_load(stream)

@pytest.fixture
def mock_yaml_load(monkeypatch):
    monkeypatch.setattr('ansible.config.manager.yaml_load', yaml_load)

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_read_config_yaml_file_exists(mock_yaml_load, config_manager, tmp_path):
    # Create a temporary YAML file
    yml_file = tmp_path / "config.yml"
    yml_file.write_text("key: value")

    # Convert to bytes as the function expects
    yml_file_bytes = to_bytes(str(yml_file))

    # Call the method
    result = config_manager._read_config_yaml_file(yml_file_bytes)

    # Assertions
    assert result == {"key": "value"}

def test_read_config_yaml_file_not_exists(config_manager):
    # Create a non-existent file path
    yml_file = "/non/existent/path/config.yml"
    yml_file_bytes = to_bytes(yml_file)

    # Call the method and expect an exception
    with pytest.raises(AnsibleError) as excinfo:
        config_manager._read_config_yaml_file(yml_file_bytes)

    # Assertions
    assert "Missing base YAML definition file" in str(excinfo.value)
    assert to_native(yml_file_bytes) in str(excinfo.value)
