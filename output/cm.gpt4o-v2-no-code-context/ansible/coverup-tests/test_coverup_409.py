# file: lib/ansible/config/manager.py:306-314
# asked: {"lines": [306, 309, 310, 311, 312, 313, 314], "branches": [[310, 311], [310, 313]]}
# gained: {"lines": [306, 309, 310, 311, 312, 313, 314], "branches": [[310, 311], [310, 313]]}

import os
import pytest
from unittest import mock
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_bytes, to_native
import yaml

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_read_config_yaml_file_exists(monkeypatch, config_manager):
    test_file_path = '/tmp/test_config.yml'
    test_content = {'key': 'value'}

    with open(test_file_path, 'w') as f:
        yaml.dump(test_content, f)

    def mock_to_bytes(path):
        return path

    monkeypatch.setattr('ansible.config.manager.to_bytes', mock_to_bytes)

    result = config_manager._read_config_yaml_file(test_file_path)
    assert result == test_content

    os.remove(test_file_path)

def test_read_config_yaml_file_not_exists(monkeypatch, config_manager):
    test_file_path = '/tmp/non_existent_config.yml'

    def mock_to_bytes(path):
        return path

    monkeypatch.setattr('ansible.config.manager.to_bytes', mock_to_bytes)

    with pytest.raises(AnsibleError) as excinfo:
        config_manager._read_config_yaml_file(test_file_path)
    
    assert "Missing base YAML definition file (bad install?):" in str(excinfo.value)
    assert to_native(test_file_path) in str(excinfo.value)
