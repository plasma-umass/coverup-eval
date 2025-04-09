# file: lib/ansible/config/manager.py:433-560
# asked: {"lines": [456, 457, 468, 469, 508, 509, 510, 511, 513, 534, 535, 545], "branches": [[455, 456], [467, 468], [471, 478], [472, 478], [473, 472], [478, 481], [499, 511], [504, 502], [507, 508], [511, 513], [511, 516], [518, 529], [532, 534], [543, 545]]}
# gained: {"lines": [456, 457, 508, 534, 535, 545], "branches": [[455, 456], [507, 508], [532, 534], [543, 545]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleError, AnsibleOptionsError

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_direct_aliases(config_manager):
    config = 'some_config'
    direct = {'alias1': 'value1'}
    defs = {config: {'aliases': ['alias1']}}
    
    with patch.object(config_manager, 'get_configuration_definitions', return_value=defs):
        value, origin = config_manager.get_config_value_and_origin(config, direct=direct)
        assert value == 'value1'
        assert origin == 'Direct'

def test_keys_aliases(config_manager):
    config = 'some_config'
    keys = {'alias1': 'value1'}
    defs = {config: {'aliases': ['alias1']}}
    
    with patch.object(config_manager, 'get_configuration_definitions', return_value=defs):
        value, origin = config_manager.get_config_value_and_origin(config, keys=keys)
        assert value == 'value1'
        assert origin == 'keyword: alias1'

def test_ini_entry_deprecated(config_manager):
    config = 'some_config'
    cfile = 'test.ini'
    defs = {config: {'ini': [{'section': 'default', 'key': 'some_key', 'deprecated': 'deprecated_message'}]}}
    
    with patch.object(config_manager, 'get_configuration_definitions', return_value=defs), \
         patch.object(config_manager, '_parse_config_file'), \
         patch.object(config_manager, '_parsers', {cfile: MagicMock()}), \
         patch('ansible.config.manager.get_ini_config_value', return_value='value1'):
        
        config_manager.DEPRECATED = []
        value, origin = config_manager.get_config_value_and_origin(config, cfile=cfile)
        assert value == 'value1'
        assert origin == cfile
        assert config_manager.DEPRECATED == [('[default]some_key', 'deprecated_message')]

def test_required_config_missing(config_manager):
    config = 'some_config'
    defs = {config: {'required': True}}
    
    with patch.object(config_manager, 'get_configuration_definitions', return_value=defs), \
         patch('ansible.config.manager.INTERNAL_DEFS', {}):
        
        with pytest.raises(AnsibleError):
            config_manager.get_config_value_and_origin(config)

def test_env_var_empty(config_manager):
    config = 'some_config'
    defs = {config: {'env': [{'name': 'SOME_ENV_VAR'}], 'type': 'int', 'default': 42}}
    
    with patch.object(config_manager, 'get_configuration_definitions', return_value=defs), \
         patch('ansible.config.manager.py3compat.environ', {'SOME_ENV_VAR': ''}):
        
        value, origin = config_manager.get_config_value_and_origin(config)
        assert value == 42
        assert origin == 'default'

def test_invalid_choice_list(config_manager):
    config = 'some_config'
    defs = {config: {'type': 'list', 'choices': ['valid1', 'valid2']}}
    
    with patch.object(config_manager, 'get_configuration_definitions', return_value=defs):
        with pytest.raises(AnsibleOptionsError):
            config_manager.get_config_value_and_origin(config, direct={config: ['invalid']})

def test_invalid_choice_simple(config_manager):
    config = 'some_config'
    defs = {config: {'choices': ['valid1', 'valid2']}}
    
    with patch.object(config_manager, 'get_configuration_definitions', return_value=defs):
        with pytest.raises(AnsibleOptionsError):
            config_manager.get_config_value_and_origin(config, direct={config: 'invalid'})
