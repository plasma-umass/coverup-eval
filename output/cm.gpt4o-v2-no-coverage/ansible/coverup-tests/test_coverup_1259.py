# file: lib/ansible/config/manager.py:356-363
# asked: {"lines": [358, 359, 360, 361, 362, 363], "branches": [[359, 360], [359, 363], [360, 359], [360, 361], [361, 359], [361, 362]]}
# gained: {"lines": [358, 359, 360, 361, 362, 363], "branches": [[359, 360], [359, 363], [360, 359], [360, 361], [361, 359], [361, 362]]}

import pytest
from unittest.mock import MagicMock

class TestConfigManager:
    
    @pytest.fixture
    def config_manager(self):
        from ansible.config.manager import ConfigManager
        return ConfigManager()

    def test_get_plugin_vars(self, config_manager, mocker):
        # Mock the get_configuration_definitions method
        mock_get_config_defs = mocker.patch.object(config_manager, 'get_configuration_definitions')
        
        # Define the return value for the mock
        mock_get_config_defs.return_value = {
            'plugin1': {
                'vars': [{'name': 'var1'}, {'name': 'var2'}]
            },
            'plugin2': {
                'vars': [{'name': 'var3'}]
            },
            'plugin3': {
                'novars': []
            }
        }
        
        # Call the method under test
        result = config_manager.get_plugin_vars('some_type', 'some_name')
        
        # Assert the expected result
        assert result == ['var1', 'var2', 'var3']
        
        # Verify the mock was called as expected
        mock_get_config_defs.assert_called_once_with('some_type', 'some_name')

    def test_get_plugin_vars_no_vars(self, config_manager, mocker):
        # Mock the get_configuration_definitions method
        mock_get_config_defs = mocker.patch.object(config_manager, 'get_configuration_definitions')
        
        # Define the return value for the mock
        mock_get_config_defs.return_value = {
            'plugin1': {
                'novars': []
            }
        }
        
        # Call the method under test
        result = config_manager.get_plugin_vars('some_type', 'some_name')
        
        # Assert the expected result
        assert result == []
        
        # Verify the mock was called as expected
        mock_get_config_defs.assert_called_once_with('some_type', 'some_name')
