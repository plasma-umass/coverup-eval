# file: lib/ansible/config/manager.py:433-560
# asked: {"lines": [451, 453, 454, 456, 457, 462, 463, 467, 468, 469, 471, 472, 473, 474, 475, 476, 478, 479, 483, 484, 485, 497, 498, 499, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 513, 518, 519, 520, 531, 532, 534, 535, 537, 538, 545, 551, 552, 556, 558], "branches": [[435, 440], [444, 558], [450, 451], [452, 453], [455, 456], [461, 462], [466, 467], [467, 468], [467, 471], [471, 472], [471, 478], [472, 473], [472, 478], [473, 472], [473, 474], [478, 479], [478, 481], [481, 483], [493, 496], [496, 497], [498, 499], [498, 516], [499, 501], [499, 511], [502, 503], [502, 516], [504, 502], [504, 505], [507, 502], [507, 508], [511, 513], [511, 516], [516, 529], [517, 518], [518, 519], [518, 529], [532, 534], [532, 537], [543, 545], [550, 551], [555, 556]]}
# gained: {"lines": [451, 453, 454, 462, 463, 467, 471, 472, 473, 474, 475, 476, 478, 479, 483, 484, 485, 497, 498, 499, 501, 502, 503, 504, 505, 506, 507, 518, 519, 520, 531, 532, 537, 538, 551, 552, 556, 558], "branches": [[435, 440], [444, 558], [450, 451], [452, 453], [461, 462], [466, 467], [467, 471], [471, 472], [472, 473], [473, 474], [478, 479], [481, 483], [493, 496], [496, 497], [498, 499], [498, 516], [499, 501], [502, 503], [502, 516], [504, 505], [507, 502], [516, 529], [517, 518], [518, 519], [532, 537], [550, 551], [555, 556]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleError, AnsibleOptionsError

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_get_config_value_and_origin_default_config(config_manager):
    with patch.object(config_manager, '_config_file', 'default_config.ini'), \
         patch.object(config_manager, 'get_configuration_definitions', return_value={'test_config': {'default': 'default_value'}}), \
         patch('ansible.config.manager.get_config_type', return_value='ini'), \
         patch.object(config_manager, '_parse_config_file'):
        value, origin = config_manager.get_config_value_and_origin('test_config')
        assert value == 'default_value'
        assert origin == 'default'

def test_get_config_value_and_origin_direct(config_manager):
    with patch.object(config_manager, 'get_configuration_definitions', return_value={'test_config': {'aliases': ['alias1']}}):
        value, origin = config_manager.get_config_value_and_origin('test_config', direct={'test_config': 'direct_value', 'alias1': 'alias_value'})
        assert value == 'direct_value'
        assert origin == 'Direct'

def test_get_config_value_and_origin_variables(config_manager):
    with patch.object(config_manager, 'get_configuration_definitions', return_value={'test_config': {'vars': ['var1']}}), \
         patch.object(config_manager, '_loop_entries', return_value=('var_value', 'var1')):
        value, origin = config_manager.get_config_value_and_origin('test_config', variables={'var1': 'var_value'})
        assert value == 'var_value'
        assert origin == 'var: var1'

def test_get_config_value_and_origin_keys(config_manager):
    with patch.object(config_manager, 'get_configuration_definitions', return_value={'test_config': {'aliases': ['alias1']}}):
        value, origin = config_manager.get_config_value_and_origin('test_config', keys={'alias1': 'key_value'})
        assert value == 'key_value'
        assert origin == 'keyword: alias1'

def test_get_config_value_and_origin_cli(config_manager):
    with patch.object(config_manager, 'get_configuration_definitions', return_value={'test_config': {'cli': ['cli1']}}), \
         patch('ansible.context.CLIARGS', {'cli1': 'cli_value'}), \
         patch.object(config_manager, '_loop_entries', return_value=('cli_value', 'cli1')):
        value, origin = config_manager.get_config_value_and_origin('test_config')
        assert value == 'cli_value'
        assert origin == 'cli: cli1'

def test_get_config_value_and_origin_env(config_manager):
    with patch.object(config_manager, 'get_configuration_definitions', return_value={'test_config': {'env': ['ENV_VAR']}}), \
         patch('ansible.module_utils.six.moves.builtins.__import__', return_value={'ENV_VAR': 'env_value'}), \
         patch.object(config_manager, '_loop_entries', return_value=('env_value', 'ENV_VAR')):
        value, origin = config_manager.get_config_value_and_origin('test_config')
        assert value == 'env_value'
        assert origin == 'env: ENV_VAR'

def test_get_config_value_and_origin_ini(config_manager):
    with patch.object(config_manager, 'get_configuration_definitions', return_value={'test_config': {'ini': [{'section': 'test_section', 'key': 'test_key'}]}}), \
         patch.object(config_manager, '_parsers', {'test_config_file.ini': MagicMock()}), \
         patch('ansible.config.manager.get_ini_config_value', return_value='ini_value'), \
         patch('ansible.config.manager.get_config_type', return_value='ini'):
        value, origin = config_manager.get_config_value_and_origin('test_config', cfile='test_config_file.ini')
        assert value == 'ini_value'
        assert origin == 'test_config_file.ini'

def test_get_config_value_and_origin_required(config_manager):
    with patch.object(config_manager, 'get_configuration_definitions', return_value={'test_config': {'required': True}}):
        with pytest.raises(AnsibleError):
            config_manager.get_config_value_and_origin('test_config')

def test_get_config_value_and_origin_default(config_manager):
    with patch.object(config_manager, 'get_configuration_definitions', return_value={'test_config': {'default': 'default_value'}}):
        value, origin = config_manager.get_config_value_and_origin('test_config')
        assert value == 'default_value'
        assert origin == 'default'

def test_get_config_value_and_origin_invalid_type(config_manager):
    with patch.object(config_manager, 'get_configuration_definitions', return_value={'test_config': {'type': 'int'}}):
        with pytest.raises(AnsibleOptionsError):
            config_manager.get_config_value_and_origin('test_config', direct={'test_config': 'invalid_type'})

def test_get_config_value_and_origin_invalid_choice(config_manager):
    with patch.object(config_manager, 'get_configuration_definitions', return_value={'test_config': {'choices': ['valid_choice']}}):
        with pytest.raises(AnsibleOptionsError):
            config_manager.get_config_value_and_origin('test_config', direct={'test_config': 'invalid_choice'})

def test_get_config_value_and_origin_deprecated(config_manager):
    with patch.object(config_manager, 'get_configuration_definitions', return_value={'test_config': {'deprecated': 'deprecated_message'}}):
        config_manager.DEPRECATED = []
        config_manager.get_config_value_and_origin('test_config', direct={'test_config': 'direct_value'})
        assert ('test_config', 'deprecated_message') in config_manager.DEPRECATED

def test_get_config_value_and_origin_not_defined(config_manager):
    with patch.object(config_manager, 'get_configuration_definitions', return_value={}):
        with pytest.raises(AnsibleError):
            config_manager.get_config_value_and_origin('test_config')
