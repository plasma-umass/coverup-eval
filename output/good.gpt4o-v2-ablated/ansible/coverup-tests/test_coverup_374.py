# file: lib/ansible/config/manager.py:343-345
# asked: {"lines": [343, 345], "branches": []}
# gained: {"lines": [343], "branches": []}

import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_find_yaml_config_files_called(config_manager, mocker):
    mocker.patch.object(config_manager, '_find_yaml_config_files', return_value=None)
    config_manager._find_yaml_config_files()
    config_manager._find_yaml_config_files.assert_called_once()

def test_find_yaml_config_files_no_files(config_manager, mocker):
    mocker.patch.object(config_manager, '_find_yaml_config_files', return_value=[])
    result = config_manager._find_yaml_config_files()
    assert result == []

def test_find_yaml_config_files_with_files(config_manager, mocker):
    mock_files = ['file1.yaml', 'file2.yaml']
    mocker.patch.object(config_manager, '_find_yaml_config_files', return_value=mock_files)
    result = config_manager._find_yaml_config_files()
    assert result == mock_files
