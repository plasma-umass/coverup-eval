# file: lib/ansible/config/manager.py:347-354
# asked: {"lines": [349, 350, 351, 352, 354], "branches": [[351, 352], [351, 354]]}
# gained: {"lines": [349, 350, 351, 352, 354], "branches": [[351, 352], [351, 354]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def config_manager():
    from ansible.config.manager import ConfigManager
    return ConfigManager()

def test_get_plugin_options_all_branches(config_manager, mocker):
    mocker.patch.object(config_manager, 'get_configuration_definitions', return_value=['option1', 'option2'])
    mocker.patch.object(config_manager, 'get_config_value', side_effect=lambda option, **kwargs: f"value_of_{option}")

    plugin_type = 'test_plugin_type'
    name = 'test_name'
    keys = ['key1', 'key2']
    variables = {'var1': 'value1'}
    direct = True

    options = config_manager.get_plugin_options(plugin_type, name, keys, variables, direct)

    assert options == {
        'option1': 'value_of_option1',
        'option2': 'value_of_option2'
    }

    config_manager.get_configuration_definitions.assert_called_once_with(plugin_type, name)
    config_manager.get_config_value.assert_any_call('option1', plugin_type=plugin_type, plugin_name=name, keys=keys, variables=variables, direct=direct)
    config_manager.get_config_value.assert_any_call('option2', plugin_type=plugin_type, plugin_name=name, keys=keys, variables=variables, direct=direct)
