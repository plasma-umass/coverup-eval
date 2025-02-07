# file: lib/ansible/config/manager.py:282-304
# asked: {"lines": [301], "branches": [[294, 299], [299, 301]]}
# gained: {"lines": [301], "branches": [[294, 299], [299, 301]]}

import pytest
from unittest.mock import patch, mock_open
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleOptionsError

@pytest.fixture
def mock_config_data():
    with patch('ansible.config.manager.ConfigData') as MockConfigData:
        yield MockConfigData

@pytest.fixture
def mock_read_config_yaml_file():
    with patch('ansible.config.manager.ConfigManager._read_config_yaml_file') as mock_method:
        mock_method.return_value = {}
        yield mock_method

@pytest.fixture
def mock_add_base_defs_deprecations():
    with patch('ansible.config.manager._add_base_defs_deprecations') as mock_method:
        yield mock_method

@pytest.fixture
def mock_find_ini_config_file():
    with patch('ansible.config.manager.find_ini_config_file') as mock_method:
        mock_method.return_value = 'dummy_config.ini'
        yield mock_method

@pytest.fixture
def mock_get_config_type():
    with patch('ansible.config.manager.get_config_type') as mock_method:
        mock_method.return_value = 'ini'
        yield mock_method

@pytest.fixture
def mock_open_file():
    m = mock_open(read_data="[default]\noption=value")
    with patch('builtins.open', m):
        yield m

@pytest.fixture
def mock_config_parser():
    with patch('ansible.config.manager.configparser.ConfigParser.read_string') as mock_method:
        yield mock_method

def test_config_manager_no_config_file(mock_config_data, mock_read_config_yaml_file, mock_add_base_defs_deprecations, mock_find_ini_config_file, mock_get_config_type, mock_open_file, mock_config_parser):
    manager = ConfigManager(conf_file=None)
    assert manager._config_file == 'dummy_config.ini'
    assert 'dummy_config.ini' in manager._parsers

def test_config_manager_with_config_file(mock_config_data, mock_read_config_yaml_file, mock_add_base_defs_deprecations, mock_get_config_type, mock_open_file, mock_config_parser):
    manager = ConfigManager(conf_file='dummy_config.ini')
    assert manager._config_file == 'dummy_config.ini'
    assert 'dummy_config.ini' in manager._parsers

def test_config_manager_unsupported_file_type(mock_config_data, mock_read_config_yaml_file, mock_add_base_defs_deprecations, mock_get_config_type):
    mock_get_config_type.return_value = 'unsupported'
    with pytest.raises(AnsibleOptionsError, match='Unsupported configuration file type'):
        ConfigManager(conf_file='dummy_config.unsupported')
