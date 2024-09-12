# file: lib/ansible/config/manager.py:356-363
# asked: {"lines": [], "branches": [[360, 359]]}
# gained: {"lines": [], "branches": [[360, 359]]}

import pytest
from unittest.mock import MagicMock
from ansible.config.manager import ConfigManager

class TestConfigManager:
    
    @pytest.fixture
    def config_manager(self):
        return ConfigManager()

    def test_get_plugin_vars_with_vars(self, config_manager, mocker):
        mock_get_config_defs = mocker.patch.object(
            config_manager, 
            'get_configuration_definitions', 
            return_value={
                'plugin1': {'vars': [{'name': 'var1'}, {'name': 'var2'}]},
                'plugin2': {'vars': [{'name': 'var3'}]}
            }
        )
        
        result = config_manager.get_plugin_vars('some_type', 'some_name')
        
        assert result == ['var1', 'var2', 'var3']
        mock_get_config_defs.assert_called_once_with('some_type', 'some_name')

    def test_get_plugin_vars_without_vars(self, config_manager, mocker):
        mock_get_config_defs = mocker.patch.object(
            config_manager, 
            'get_configuration_definitions', 
            return_value={
                'plugin1': {},
                'plugin2': {'vars': []}
            }
        )
        
        result = config_manager.get_plugin_vars('some_type', 'some_name')
        
        assert result == []
        mock_get_config_defs.assert_called_once_with('some_type', 'some_name')
