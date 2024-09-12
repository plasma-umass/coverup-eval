# file: lib/ansible/config/manager.py:433-560
# asked: {"lines": [433, 435, 437, 440, 441, 443, 444, 446, 449, 450, 451, 452, 453, 454, 455, 456, 457, 461, 462, 463, 466, 467, 468, 469, 471, 472, 473, 474, 475, 476, 478, 479, 481, 483, 484, 485, 488, 489, 490, 493, 494, 496, 497, 498, 499, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 513, 516, 517, 518, 519, 520, 522, 523, 525, 526, 529, 530, 531, 532, 534, 535, 537, 538, 541, 542, 543, 545, 548, 550, 551, 552, 555, 556, 558, 560], "branches": [[435, 437], [435, 440], [444, 446], [444, 558], [450, 451], [450, 452], [452, 453], [452, 455], [455, 456], [455, 461], [461, 462], [461, 466], [466, 467], [466, 481], [467, 468], [467, 471], [471, 472], [471, 478], [472, 473], [472, 478], [473, 472], [473, 474], [478, 479], [478, 481], [481, 483], [481, 488], [488, 489], [488, 493], [493, 494], [493, 496], [496, 497], [496, 516], [498, 499], [498, 516], [499, 501], [499, 511], [502, 503], [502, 516], [504, 502], [504, 505], [507, 502], [507, 508], [511, 513], [511, 516], [516, 517], [516, 529], [517, 518], [517, 522], [518, 519], [518, 529], [525, 526], [525, 529], [532, 534], [532, 537], [541, 542], [541, 555], [543, 545], [543, 548], [550, 551], [550, 555], [555, 556], [555, 560]]}
# gained: {"lines": [433, 435, 437, 440, 441, 443, 444, 446, 449, 450, 451, 452, 453, 454, 455, 461, 462, 463, 466, 467, 468, 469, 478, 479, 481, 483, 484, 485, 488, 489, 490, 493, 494, 496, 497, 498, 499, 501, 502, 503, 504, 505, 506, 507, 516, 517, 522, 523, 525, 526, 529, 530, 531, 532, 537, 538, 541, 542, 543, 548, 550, 551, 552, 555, 556, 558, 560], "branches": [[435, 437], [435, 440], [444, 446], [444, 558], [450, 451], [450, 452], [452, 453], [452, 455], [455, 461], [461, 462], [461, 466], [466, 467], [466, 481], [467, 468], [478, 479], [481, 483], [481, 488], [488, 489], [488, 493], [493, 494], [493, 496], [496, 497], [496, 516], [498, 499], [499, 501], [502, 503], [502, 516], [504, 505], [507, 502], [516, 517], [516, 529], [517, 522], [525, 526], [525, 529], [532, 537], [541, 542], [541, 555], [543, 548], [550, 551], [550, 555], [555, 556], [555, 560]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleOptionsError, AnsibleError

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_get_config_value_and_origin_direct(config_manager):
    config = 'some_config'
    cfile = None
    plugin_type = None
    plugin_name = None
    keys = None
    variables = None
    direct = {config: 'direct_value'}

    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'aliases': []}}):
        value, origin = config_manager.get_config_value_and_origin(config, cfile, plugin_type, plugin_name, keys, variables, direct)
        assert value == 'direct_value'
        assert origin == 'Direct'

def test_get_config_value_and_origin_variables(config_manager):
    config = 'some_config'
    cfile = None
    plugin_type = None
    plugin_name = None
    keys = None
    variables = {'var1': 'var_value'}
    direct = None

    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'vars': [{'name': 'var1'}]}}):
        with patch.object(config_manager, '_loop_entries', return_value=('var_value', 'var1')):
            value, origin = config_manager.get_config_value_and_origin(config, cfile, plugin_type, plugin_name, keys, variables, direct)
            assert value == 'var_value'
            assert origin == 'var: var1'

def test_get_config_value_and_origin_keys(config_manager):
    config = 'some_config'
    cfile = None
    plugin_type = None
    plugin_name = None
    keys = {config: 'key_value'}
    variables = None
    direct = None

    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'aliases': []}}):
        value, origin = config_manager.get_config_value_and_origin(config, cfile, plugin_type, plugin_name, keys, variables, direct)
        assert value == 'key_value'
        assert origin == 'keyword: some_config'

def test_get_config_value_and_origin_cli(config_manager):
    config = 'some_config'
    cfile = None
    plugin_type = None
    plugin_name = None
    keys = None
    variables = None
    direct = None

    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'cli': [{'name': 'cli_arg'}]}}):
        with patch('ansible.context.CLIARGS', {'cli_arg': 'cli_value'}):
            with patch.object(config_manager, '_loop_entries', return_value=('cli_value', 'cli_arg')):
                value, origin = config_manager.get_config_value_and_origin(config, cfile, plugin_type, plugin_name, keys, variables, direct)
                assert value == 'cli_value'
                assert origin == 'cli: cli_arg'

def test_get_config_value_and_origin_env(config_manager):
    config = 'some_config'
    cfile = None
    plugin_type = None
    plugin_name = None
    keys = None
    variables = None
    direct = None

    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'env': [{'name': 'ENV_VAR'}]}}):
        with patch('ansible.utils.py3compat.environ', {'ENV_VAR': 'env_value'}):
            with patch.object(config_manager, '_loop_entries', return_value=('env_value', 'ENV_VAR')):
                value, origin = config_manager.get_config_value_and_origin(config, cfile, plugin_type, plugin_name, keys, variables, direct)
                assert value == 'env_value'
                assert origin == 'env: ENV_VAR'

def test_get_config_value_and_origin_ini(config_manager):
    config = 'some_config'
    cfile = 'test.ini'
    plugin_type = None
    plugin_name = None
    keys = None
    variables = None
    direct = None

    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'ini': [{'section': 'defaults', 'key': 'some_key'}]}}):
        with patch.object(config_manager, '_parsers', {cfile: MagicMock()}):
            with patch('ansible.config.manager.get_ini_config_value', return_value='ini_value'):
                value, origin = config_manager.get_config_value_and_origin(config, cfile, plugin_type, plugin_name, keys, variables, direct)
                assert value == 'ini_value'
                assert origin == cfile

def test_get_config_value_and_origin_default(config_manager):
    config = 'some_config'
    cfile = None
    plugin_type = None
    plugin_name = None
    keys = None
    variables = None
    direct = None

    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'default': 'default_value'}}):
        value, origin = config_manager.get_config_value_and_origin(config, cfile, plugin_type, plugin_name, keys, variables, direct)
        assert value == 'default_value'
        assert origin == 'default'

def test_get_config_value_and_origin_invalid_type(config_manager):
    config = 'some_config'
    cfile = None
    plugin_type = None
    plugin_name = None
    keys = None
    variables = None
    direct = {config: 'invalid_value'}

    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'type': 'int', 'aliases': []}}):
        with pytest.raises(AnsibleOptionsError):
            config_manager.get_config_value_and_origin(config, cfile, plugin_type, plugin_name, keys, variables, direct)

def test_get_config_value_and_origin_invalid_choice(config_manager):
    config = 'some_config'
    cfile = None
    plugin_type = None
    plugin_name = None
    keys = None
    variables = None
    direct = {config: 'invalid_choice'}

    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'choices': ['valid_choice'], 'aliases': []}}):
        with pytest.raises(AnsibleOptionsError):
            config_manager.get_config_value_and_origin(config, cfile, plugin_type, plugin_name, keys, variables, direct)

def test_get_config_value_and_origin_deprecated(config_manager):
    config = 'some_config'
    cfile = None
    plugin_type = None
    plugin_name = None
    keys = None
    variables = None
    direct = {config: 'deprecated_value'}

    with patch.object(config_manager, 'get_configuration_definitions', return_value={config: {'deprecated': 'deprecated_message', 'aliases': []}}):
        value, origin = config_manager.get_config_value_and_origin(config, cfile, plugin_type, plugin_name, keys, variables, direct)
        assert value == 'deprecated_value'
        assert origin == 'Direct'
        assert (config, 'deprecated_message') in config_manager.DEPRECATED

def test_get_config_value_and_origin_not_defined(config_manager):
    config = 'undefined_config'
    cfile = None
    plugin_type = None
    plugin_name = None
    keys = None
    variables = None
    direct = None

    with patch.object(config_manager, 'get_configuration_definitions', return_value={}):
        with pytest.raises(AnsibleError):
            config_manager.get_config_value_and_origin(config, cfile, plugin_type, plugin_name, keys, variables, direct)
