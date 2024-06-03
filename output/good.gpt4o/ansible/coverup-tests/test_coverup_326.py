# file lib/ansible/config/manager.py:356-363
# lines [356, 358, 359, 360, 361, 362, 363]
# branches ['359->360', '359->363', '360->359', '360->361', '361->359', '361->362']

import pytest
from unittest import mock
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_get_plugin_vars(config_manager, mocker):
    mock_get_configuration_definitions = mocker.patch.object(
        config_manager, 
        'get_configuration_definitions', 
        return_value={
            'plugin1': {'vars': [{'name': 'var1'}, {'name': 'var2'}]},
            'plugin2': {'vars': [{'name': 'var3'}]},
            'plugin3': {'vars': []},
            'plugin4': {}
        }
    )

    result = config_manager.get_plugin_vars('some_plugin_type', 'some_name')
    
    assert result == ['var1', 'var2', 'var3']
    mock_get_configuration_definitions.assert_called_once_with('some_plugin_type', 'some_name')
