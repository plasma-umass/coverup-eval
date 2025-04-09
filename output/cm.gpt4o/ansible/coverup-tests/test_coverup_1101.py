# file lib/ansible/config/manager.py:316-341
# lines [325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 341]
# branches ['320->323', '324->325', '325->326', '325->341']

import pytest
from unittest import mock
from ansible.config.manager import ConfigManager, AnsibleOptionsError
import configparser

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_parse_config_file_ini(config_manager, mocker):
    mocker.patch('ansible.config.manager.get_config_type', return_value='ini')
    mocker.patch('builtins.open', mock.mock_open(read_data='[DEFAULT]\nkey=value'))
    mocker.patch('ansible.config.manager.to_bytes', side_effect=lambda x: x)
    mocker.patch('ansible.config.manager.to_text', side_effect=lambda x, errors: x)

    config_manager._config_file = 'dummy.ini'
    config_manager._parsers = {}

    config_manager._parse_config_file()

    assert 'dummy.ini' in config_manager._parsers
    assert config_manager._parsers['dummy.ini'].get('DEFAULT', 'key') == 'value'

def test_parse_config_file_unsupported_type(config_manager, mocker):
    mocker.patch('ansible.config.manager.get_config_type', return_value='unsupported')
    config_manager._config_file = 'dummy.unsupported'

    with pytest.raises(AnsibleOptionsError, match="Unsupported configuration file type"):
        config_manager._parse_config_file()
