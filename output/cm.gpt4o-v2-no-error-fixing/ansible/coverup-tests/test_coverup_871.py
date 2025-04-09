# file: lib/ansible/config/manager.py:433-560
# asked: {"lines": [456, 457, 471, 472, 473, 474, 475, 476, 508, 509, 510, 511, 513, 534, 535, 545], "branches": [[455, 456], [467, 471], [471, 472], [471, 478], [472, 473], [472, 478], [473, 472], [473, 474], [478, 481], [498, 516], [499, 511], [504, 502], [507, 508], [511, 513], [511, 516], [518, 529], [532, 534], [543, 545]]}
# gained: {"lines": [456, 457, 471, 472, 473, 474, 475, 476, 508, 545], "branches": [[455, 456], [467, 471], [471, 472], [472, 473], [473, 474], [507, 508], [543, 545]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleOptionsError, AnsibleError

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_direct_aliases(config_manager):
    config = 'some_config'
    direct = {'alias1': 'value1'}
    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'aliases': ['alias1']}}):
        value, origin = config_manager.get_config_value_and_origin(config, direct=direct)
        assert value == 'value1'
        assert origin == 'Direct'

def test_keys_aliases(config_manager):
    config = 'some_config'
    keys = {'alias1': 'value1'}
    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'aliases': ['alias1']}}):
        value, origin = config_manager.get_config_value_and_origin(config, keys=keys)
        assert value == 'value1'
        assert origin == 'keyword: alias1'

def test_ini_config(config_manager):
    config = 'some_config'
    cfile = 'test.ini'
    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'ini': [{'section': 'default', 'key': 'some_key'}]}}), \
         patch.object(config_manager, '_parse_config_file'), \
         patch('ansible.config.manager.get_ini_config_value', return_value='value1'), \
         patch('ansible.config.manager.get_config_type', return_value='ini'):
        config_manager._parsers[cfile] = MagicMock()
        value, origin = config_manager.get_config_value_and_origin(config, cfile=cfile)
        assert value == 'value1'
        assert origin == cfile

def test_ini_config_deprecated(config_manager):
    config = 'some_config'
    cfile = 'test.ini'
    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'ini': [{'section': 'default', 'key': 'some_key', 'deprecated': 'deprecated_message'}]}}), \
         patch.object(config_manager, '_parse_config_file'), \
         patch('ansible.config.manager.get_ini_config_value', return_value='value1'), \
         patch('ansible.config.manager.get_config_type', return_value='ini'):
        config_manager._parsers[cfile] = MagicMock()
        value, origin = config_manager.get_config_value_and_origin(config, cfile=cfile)
        assert value == 'value1'
        assert origin == cfile
        assert config_manager.DEPRECATED == [('[default]some_key', 'deprecated_message')]

def test_required_config(config_manager):
    config = 'some_config'
    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'required': True}}), \
         patch('ansible.config.manager.INTERNAL_DEFS', {}):
        with pytest.raises(AnsibleError):
            config_manager.get_config_value_and_origin(config)

def test_invalid_type_env(config_manager):
    config = 'some_config'
    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'type': 'int', 'env': [{'name': 'SOME_ENV'}]}}), \
         patch.object(config_manager, '_loop_entries', return_value=('invalid_int', 'env: SOME_ENV')):
        with pytest.raises(AnsibleOptionsError):
            config_manager.get_config_value_and_origin(config)

def test_invalid_choices(config_manager):
    config = 'some_config'
    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'choices': ['valid_choice']}}):
        with pytest.raises(AnsibleOptionsError):
            config_manager.get_config_value_and_origin(config, direct={config: 'invalid_choice'})

def test_list_invalid_choices(config_manager):
    config = 'some_config'
    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'type': 'list', 'choices': ['valid_choice']}}):
        with pytest.raises(AnsibleOptionsError):
            config_manager.get_config_value_and_origin(config, direct={config: ['invalid_choice']})
