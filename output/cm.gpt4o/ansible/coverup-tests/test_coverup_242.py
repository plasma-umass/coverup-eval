# file lib/ansible/config/manager.py:282-304
# lines [282, 284, 285, 286, 288, 289, 291, 292, 294, 296, 299, 301, 304]
# branches ['294->296', '294->299', '299->301', '299->304']

import os
import pytest
from unittest import mock
from ansible.config.manager import ConfigManager

@pytest.fixture
def mock_config_data(mocker):
    return mocker.patch('ansible.config.manager.ConfigData', autospec=True)

@pytest.fixture
def mock_read_config_yaml_file(mocker):
    return mocker.patch('ansible.config.manager.ConfigManager._read_config_yaml_file', return_value={})

@pytest.fixture
def mock_add_base_defs_deprecations(mocker):
    return mocker.patch('ansible.config.manager._add_base_defs_deprecations')

@pytest.fixture
def mock_find_ini_config_file(mocker):
    return mocker.patch('ansible.config.manager.find_ini_config_file', return_value='/path/to/config.ini')

@pytest.fixture
def mock_parse_config_file(mocker):
    return mocker.patch('ansible.config.manager.ConfigManager._parse_config_file')

@pytest.fixture
def mock_update_config_data(mocker):
    return mocker.patch('ansible.config.manager.ConfigManager.update_config_data')

def test_config_manager_initialization_with_defaults(mock_config_data, mock_read_config_yaml_file, mock_add_base_defs_deprecations, mock_find_ini_config_file, mock_parse_config_file, mock_update_config_data):
    with mock.patch('os.path.dirname', return_value='/output/lib/ansible/config'):
        manager = ConfigManager()
    
    mock_read_config_yaml_file.assert_called_once_with('/output/lib/ansible/config/base.yml')
    mock_add_base_defs_deprecations.assert_called_once_with({})
    mock_find_ini_config_file.assert_called_once_with(manager.WARNINGS)
    mock_parse_config_file.assert_called_once()
    mock_update_config_data.assert_called_once()

def test_config_manager_initialization_with_custom_files(mock_config_data, mock_read_config_yaml_file, mock_add_base_defs_deprecations, mock_parse_config_file, mock_update_config_data):
    conf_file = '/custom/path/to/config.ini'
    defs_file = '/custom/path/to/base.yml'
    
    manager = ConfigManager(conf_file=conf_file, defs_file=defs_file)
    
    mock_read_config_yaml_file.assert_called_once_with(defs_file)
    mock_add_base_defs_deprecations.assert_called_once_with({})
    mock_parse_config_file.assert_called_once()
    mock_update_config_data.assert_called_once()
    assert manager._config_file == conf_file
