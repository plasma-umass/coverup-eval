# file: lib/ansible/config/manager.py:433-560
# asked: {"lines": [451, 453, 454, 456, 457, 462, 463, 467, 468, 469, 471, 472, 473, 474, 475, 476, 478, 479, 483, 484, 485, 497, 498, 499, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 513, 518, 519, 520, 531, 532, 534, 535, 537, 538, 545, 551, 552, 556, 558], "branches": [[435, 440], [444, 558], [450, 451], [452, 453], [455, 456], [461, 462], [466, 467], [467, 468], [467, 471], [471, 472], [471, 478], [472, 473], [472, 478], [473, 472], [473, 474], [478, 479], [478, 481], [481, 483], [493, 496], [496, 497], [498, 499], [498, 516], [499, 501], [499, 511], [502, 503], [502, 516], [504, 502], [504, 505], [507, 502], [507, 508], [511, 513], [511, 516], [516, 529], [517, 518], [518, 519], [518, 529], [532, 534], [532, 537], [543, 545], [550, 551], [555, 556]]}
# gained: {"lines": [451, 453, 454, 462, 463, 467, 468, 469, 478, 479, 483, 484, 485, 497, 498, 499, 501, 502, 503, 504, 505, 506, 507, 531, 532, 537, 538, 551, 552, 556], "branches": [[435, 440], [450, 451], [452, 453], [461, 462], [466, 467], [467, 468], [478, 479], [481, 483], [493, 496], [496, 497], [498, 499], [499, 501], [502, 503], [502, 516], [504, 505], [507, 502], [516, 529], [532, 537], [550, 551], [555, 556]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleOptionsError, AnsibleError
from ansible.module_utils.six import string_types
from ansible.utils import py3compat
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_get_config_value_and_origin_direct(config_manager):
    config_manager.get_configuration_definitions = MagicMock(return_value={
        'test_config': {
            'aliases': ['alias1', 'alias2'],
            'type': 'string'
        }
    })
    direct = {'test_config': 'direct_value'}
    value, origin = config_manager.get_config_value_and_origin('test_config', direct=direct)
    assert value == 'direct_value'
    assert origin == 'Direct'

def test_get_config_value_and_origin_variables(config_manager):
    config_manager.get_configuration_definitions = MagicMock(return_value={
        'test_config': {
            'vars': [{'name': 'var1'}, {'name': 'var2'}],
            'type': 'string'
        }
    })
    config_manager._loop_entries = MagicMock(return_value=('var_value', 'var1'))
    variables = {'var1': 'var_value'}
    value, origin = config_manager.get_config_value_and_origin('test_config', variables=variables)
    assert value == 'var_value'
    assert origin == 'var: var1'

def test_get_config_value_and_origin_keys(config_manager):
    config_manager.get_configuration_definitions = MagicMock(return_value={
        'test_config': {
            'aliases': ['alias1', 'alias2'],
            'type': 'string'
        }
    })
    keys = {'test_config': 'key_value'}
    value, origin = config_manager.get_config_value_and_origin('test_config', keys=keys)
    assert value == 'key_value'
    assert origin == 'keyword: test_config'

def test_get_config_value_and_origin_cli(config_manager):
    config_manager.get_configuration_definitions = MagicMock(return_value={
        'test_config': {
            'cli': [{'name': 'cli1'}, {'name': 'cli2'}],
            'type': 'string'
        }
    })
    with patch('ansible.context.CLIARGS', {'cli1': 'cli_value'}):
        config_manager._loop_entries = MagicMock(return_value=('cli_value', 'cli1'))
        value, origin = config_manager.get_config_value_and_origin('test_config')
        assert value == 'cli_value'
        assert origin == 'cli: cli1'

def test_get_config_value_and_origin_env(config_manager, monkeypatch):
    config_manager.get_configuration_definitions = MagicMock(return_value={
        'test_config': {
            'env': [{'name': 'ENV_VAR'}],
            'type': 'string'
        }
    })
    monkeypatch.setattr(py3compat, 'environ', {'ENV_VAR': 'env_value'})
    config_manager._loop_entries = MagicMock(return_value=('env_value', 'ENV_VAR'))
    value, origin = config_manager.get_config_value_and_origin('test_config')
    assert value == 'env_value'
    assert origin == 'env: ENV_VAR'

def test_get_config_value_and_origin_config_file(config_manager):
    config_manager.get_configuration_definitions = MagicMock(return_value={
        'test_config': {
            'ini': [{'section': 'default', 'key': 'test_config'}],
            'type': 'string'
        }
    })
    config_manager._parsers = { 'config_file': MagicMock() }
    config_manager._parse_config_file = MagicMock()
    with patch('ansible.config.manager.get_config_type', return_value='ini'):
        with patch('ansible.config.manager.get_ini_config_value', return_value='ini_value'):
            value, origin = config_manager.get_config_value_and_origin('test_config', cfile='config_file')
            assert value == 'ini_value'
            assert origin == 'config_file'

def test_get_config_value_and_origin_default(config_manager):
    config_manager.get_configuration_definitions = MagicMock(return_value={
        'test_config': {
            'default': 'default_value',
            'type': 'string'
        }
    })
    value, origin = config_manager.get_config_value_and_origin('test_config')
    assert value == 'default_value'
    assert origin == 'default'

def test_get_config_value_and_origin_invalid_type(config_manager):
    config_manager.get_configuration_definitions = MagicMock(return_value={
        'test_config': {
            'type': 'integer'
        }
    })
    with pytest.raises(AnsibleOptionsError):
        config_manager.get_config_value_and_origin('test_config', direct={'test_config': 'not_an_int'})

def test_get_config_value_and_origin_invalid_choice(config_manager):
    config_manager.get_configuration_definitions = MagicMock(return_value={
        'test_config': {
            'choices': ['valid_choice'],
            'type': 'string'
        }
    })
    with pytest.raises(AnsibleOptionsError):
        config_manager.get_config_value_and_origin('test_config', direct={'test_config': 'invalid_choice'})

def test_get_config_value_and_origin_deprecated(config_manager):
    config_manager.get_configuration_definitions = MagicMock(return_value={
        'test_config': {
            'deprecated': 'This setting is deprecated',
            'type': 'string'
        }
    })
    config_manager.DEPRECATED = []
    value, origin = config_manager.get_config_value_and_origin('test_config', direct={'test_config': 'deprecated_value'})
    assert ('test_config', 'This setting is deprecated') in config_manager.DEPRECATED
