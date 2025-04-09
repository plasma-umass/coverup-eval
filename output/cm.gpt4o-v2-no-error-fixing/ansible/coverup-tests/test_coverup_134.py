# file: lib/ansible/config/manager.py:282-304
# asked: {"lines": [282, 284, 285, 286, 288, 289, 291, 292, 294, 296, 299, 301, 304], "branches": [[294, 296], [294, 299], [299, 301], [299, 304]]}
# gained: {"lines": [282, 284, 285, 286, 288, 289, 291, 292, 294, 296, 299, 301, 304], "branches": [[294, 296], [294, 299], [299, 301], [299, 304]]}

import os
import pytest
from unittest.mock import patch, mock_open
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleError, AnsibleOptionsError

@pytest.fixture
def mock_config_data():
    with patch('ansible.config.manager.ConfigData') as MockConfigData:
        yield MockConfigData

@pytest.fixture
def mock_read_config_yaml_file():
    with patch('ansible.config.manager.ConfigManager._read_config_yaml_file') as mock_method:
        yield mock_method

@pytest.fixture
def mock_add_base_defs_deprecations():
    with patch('ansible.config.manager._add_base_defs_deprecations') as mock_method:
        yield mock_method

@pytest.fixture
def mock_find_ini_config_file():
    with patch('ansible.config.manager.find_ini_config_file') as mock_method:
        yield mock_method

@pytest.fixture
def mock_parse_config_file():
    with patch('ansible.config.manager.ConfigManager._parse_config_file') as mock_method:
        yield mock_method

@pytest.fixture
def mock_update_config_data():
    with patch('ansible.config.manager.ConfigManager.update_config_data') as mock_method:
        yield mock_method

def test_init_with_conf_file(mock_config_data, mock_read_config_yaml_file, mock_add_base_defs_deprecations, mock_parse_config_file, mock_update_config_data):
    conf_file = '/path/to/conf_file.yml'
    defs_file = '/path/to/defs_file.yml'
    
    mock_read_config_yaml_file.return_value = {}
    
    config_manager = ConfigManager(conf_file=conf_file, defs_file=defs_file)
    
    assert config_manager._config_file == conf_file
    mock_read_config_yaml_file.assert_called_once_with(defs_file)
    mock_add_base_defs_deprecations.assert_called_once()
    mock_parse_config_file.assert_called_once()
    mock_update_config_data.assert_called_once()

def test_init_without_conf_file(mock_config_data, mock_read_config_yaml_file, mock_add_base_defs_deprecations, mock_find_ini_config_file, mock_parse_config_file, mock_update_config_data):
    conf_file = None
    defs_file = '/path/to/defs_file.yml'
    
    mock_read_config_yaml_file.return_value = {}
    mock_find_ini_config_file.return_value = '/path/to/found_conf_file.ini'
    
    config_manager = ConfigManager(conf_file=conf_file, defs_file=defs_file)
    
    assert config_manager._config_file == '/path/to/found_conf_file.ini'
    mock_read_config_yaml_file.assert_called_once_with(defs_file)
    mock_add_base_defs_deprecations.assert_called_once()
    mock_find_ini_config_file.assert_called_once()
    mock_parse_config_file.assert_called_once()
    mock_update_config_data.assert_called_once()

def test_init_without_conf_file_and_no_ini_found(mock_config_data, mock_read_config_yaml_file, mock_add_base_defs_deprecations, mock_find_ini_config_file, mock_update_config_data):
    conf_file = None
    defs_file = '/path/to/defs_file.yml'
    
    mock_read_config_yaml_file.return_value = {}
    mock_find_ini_config_file.return_value = None
    
    config_manager = ConfigManager(conf_file=conf_file, defs_file=defs_file)
    
    assert config_manager._config_file is None
    mock_read_config_yaml_file.assert_called_once_with(defs_file)
    mock_add_base_defs_deprecations.assert_called_once()
    mock_find_ini_config_file.assert_called_once()
    mock_update_config_data.assert_called_once()
