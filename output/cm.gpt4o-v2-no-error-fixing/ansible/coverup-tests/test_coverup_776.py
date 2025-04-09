# file: lib/ansible/config/manager.py:356-363
# asked: {"lines": [358, 359, 360, 361, 362, 363], "branches": [[359, 360], [359, 363], [360, 359], [360, 361], [361, 359], [361, 362]]}
# gained: {"lines": [358, 359, 360, 361, 362, 363], "branches": [[359, 360], [359, 363], [360, 359], [360, 361], [361, 359], [361, 362]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def config_manager():
    from ansible.config.manager import ConfigManager
    return ConfigManager()

def test_get_plugin_vars(config_manager, mocker):
    mock_get_config_defs = mocker.patch.object(config_manager, 'get_configuration_definitions')
    
    # Mocking the return value of get_configuration_definitions
    mock_get_config_defs.return_value = {
        'plugin1': {
            'vars': [{'name': 'var1'}, {'name': 'var2'}]
        },
        'plugin2': {
            'vars': [{'name': 'var3'}, {'name': 'var4'}]
        }
    }
    
    result = config_manager.get_plugin_vars('some_plugin_type', 'some_name')
    
    assert result == ['var1', 'var2', 'var3', 'var4']
    mock_get_config_defs.assert_called_once_with('some_plugin_type', 'some_name')

def test_get_plugin_vars_no_vars(config_manager, mocker):
    mock_get_config_defs = mocker.patch.object(config_manager, 'get_configuration_definitions')
    
    # Mocking the return value of get_configuration_definitions with no 'vars' key
    mock_get_config_defs.return_value = {
        'plugin1': {},
        'plugin2': {}
    }
    
    result = config_manager.get_plugin_vars('some_plugin_type', 'some_name')
    
    assert result == []
    mock_get_config_defs.assert_called_once_with('some_plugin_type', 'some_name')
