# file lib/ansible/config/manager.py:316-341
# lines [330, 331, 334, 335]
# branches ['320->323']

import pytest
from unittest import mock
from ansible.config.manager import ConfigManager, AnsibleOptionsError
import configparser

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_parse_config_file_no_cfile(config_manager, mocker):
    mocker.patch.object(config_manager, '_config_file', 'test.ini')
    mocker.patch('ansible.config.manager.get_config_type', return_value='ini')
    mocker.patch('builtins.open', mock.mock_open(read_data=b'[section]\nkey=value'))
    mocker.patch('ansible.config.manager.to_bytes', side_effect=lambda x: x)
    mocker.patch('ansible.config.manager.to_text', side_effect=lambda x, errors: x.decode('utf-8'))

    config_manager._parsers = {}
    config_manager._parse_config_file()
    assert 'test.ini' in config_manager._parsers

def test_parse_config_file_unicode_error(config_manager, mocker):
    mocker.patch.object(config_manager, '_config_file', 'test.ini')
    mocker.patch('ansible.config.manager.get_config_type', return_value='ini')
    mocker.patch('builtins.open', mock.mock_open(read_data=b'\x80\x81'))
    mocker.patch('ansible.config.manager.to_bytes', side_effect=lambda x: x)
    mocker.patch('ansible.config.manager.to_text', side_effect=UnicodeError)

    with pytest.raises(AnsibleOptionsError, match="Error reading config file"):
        config_manager._parse_config_file()

def test_parse_config_file_configparser_error(config_manager, mocker):
    mocker.patch.object(config_manager, '_config_file', 'test.ini')
    mocker.patch('ansible.config.manager.get_config_type', return_value='ini')
    mocker.patch('builtins.open', mock.mock_open(read_data=b'[section]\nkey=value'))
    mocker.patch('ansible.config.manager.to_bytes', side_effect=lambda x: x)
    mocker.patch('ansible.config.manager.to_text', side_effect=lambda x, errors: x.decode('utf-8'))
    mocker.patch.object(configparser.ConfigParser, 'read_string', side_effect=configparser.Error)

    with pytest.raises(AnsibleOptionsError, match="Error reading config file"):
        config_manager._parse_config_file()
