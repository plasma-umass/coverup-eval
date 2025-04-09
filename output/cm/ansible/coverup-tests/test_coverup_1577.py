# file lib/ansible/config/manager.py:356-363
# lines [358, 359, 360, 361, 362, 363]
# branches ['359->360', '359->363', '360->359', '360->361', '361->359', '361->362']

import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

@pytest.fixture
def mock_get_configuration_definitions(mocker):
    return mocker.patch.object(ConfigManager, 'get_configuration_definitions')

def test_get_plugin_vars_with_vars(config_manager, mock_get_configuration_definitions):
    # Mock the get_configuration_definitions to return a dict with 'vars'
    mock_get_configuration_definitions.return_value = {
        'plugin_def': {
            'vars': [{'name': 'var1'}, {'name': 'var2'}]
        }
    }

    # Call the method under test
    plugin_vars = config_manager.get_plugin_vars('plugin_type', 'plugin_name')

    # Assert that the method returns the correct vars
    assert plugin_vars == ['var1', 'var2']

    # Assert that the mock was called with the correct arguments
    mock_get_configuration_definitions.assert_called_once_with('plugin_type', 'plugin_name')

def test_get_plugin_vars_without_vars(config_manager, mock_get_configuration_definitions):
    # Mock the get_configuration_definitions to return a dict without 'vars'
    mock_get_configuration_definitions.return_value = {
        'plugin_def': {}
    }

    # Call the method under test
    plugin_vars = config_manager.get_plugin_vars('plugin_type', 'plugin_name')

    # Assert that the method returns an empty list
    assert plugin_vars == []

    # Assert that the mock was called with the correct arguments
    mock_get_configuration_definitions.assert_called_once_with('plugin_type', 'plugin_name')
