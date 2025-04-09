# file lib/ansible/config/manager.py:306-314
# lines [306, 309, 310, 311, 312, 313, 314]
# branches ['310->311', '310->313']

import os
import pytest
from unittest import mock
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_bytes, to_native
import yaml

# Mocking yaml_load function
def yaml_load(stream):
    return yaml.safe_load(stream)

@pytest.fixture
def mock_yaml_load(mocker):
    mocker.patch('ansible.config.manager.yaml_load', side_effect=yaml_load)

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_read_config_yaml_file_exists(mocker, mock_yaml_load, config_manager):
    # Create a temporary YAML file
    yml_content = {'key': 'value'}
    yml_file = 'test_config.yml'
    with open(yml_file, 'w') as f:
        yaml.dump(yml_content, f)

    # Mock os.path.exists to return True
    mocker.patch('os.path.exists', return_value=True)

    # Test the method
    result = config_manager._read_config_yaml_file(yml_file)
    assert result == yml_content

    # Clean up
    os.remove(yml_file)

def test_read_config_yaml_file_not_exists(mocker, config_manager):
    yml_file = 'non_existent_config.yml'

    # Mock os.path.exists to return False
    mocker.patch('os.path.exists', return_value=False)

    # Test the method and assert it raises AnsibleError
    with pytest.raises(AnsibleError) as excinfo:
        config_manager._read_config_yaml_file(yml_file)
    assert "Missing base YAML definition file (bad install?):" in str(excinfo.value)
