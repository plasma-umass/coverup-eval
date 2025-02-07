# file: lib/ansible/config/manager.py:347-354
# asked: {"lines": [347, 349, 350, 351, 352, 354], "branches": [[351, 352], [351, 354]]}
# gained: {"lines": [347, 349, 350, 351, 352, 354], "branches": [[351, 352], [351, 354]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def config_manager():
    from ansible.config.manager import ConfigManager
    return ConfigManager()

def test_get_plugin_options(config_manager, mocker):
    # Mock the methods get_configuration_definitions and get_config_value
    mock_get_configuration_definitions = mocker.patch.object(config_manager, 'get_configuration_definitions', return_value=['option1', 'option2'])
    mock_get_config_value = mocker.patch.object(config_manager, 'get_config_value', side_effect=lambda option, **kwargs: f"value_of_{option}")

    # Call the method with test parameters
    plugin_type = 'test_plugin_type'
    name = 'test_name'
    keys = ['key1', 'key2']
    variables = {'var1': 'value1'}
    direct = True

    result = config_manager.get_plugin_options(plugin_type, name, keys=keys, variables=variables, direct=direct)

    # Assertions to verify the behavior
    assert result == {
        'option1': 'value_of_option1',
        'option2': 'value_of_option2'
    }
    mock_get_configuration_definitions.assert_called_once_with(plugin_type, name)
    assert mock_get_config_value.call_count == 2
    mock_get_config_value.assert_any_call('option1', plugin_type=plugin_type, plugin_name=name, keys=keys, variables=variables, direct=direct)
    mock_get_config_value.assert_any_call('option2', plugin_type=plugin_type, plugin_name=name, keys=keys, variables=variables, direct=direct)
