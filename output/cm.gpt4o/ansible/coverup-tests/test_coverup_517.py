# file lib/ansible/config/manager.py:347-354
# lines [347, 349, 350, 351, 352, 354]
# branches ['351->352', '351->354']

import pytest
from unittest.mock import MagicMock, patch
from ansible.config.manager import ConfigManager

@pytest.fixture
def mock_config_manager(mocker):
    with patch('ansible.config.manager.ConfigManager.get_configuration_definitions') as mock_get_defs, \
         patch('ansible.config.manager.ConfigManager.get_config_value') as mock_get_value, \
         patch('ansible.config.manager.ConfigManager.update_config_data') as mock_update_config_data:
        
        mock_get_defs.return_value = {
            'option1': {'default': 'default_value1'},
            'option2': {'default': 'default_value2'}
        }
        mock_get_value.side_effect = lambda option, **kwargs: f"value_of_{option}"
        mock_update_config_data.return_value = None
        
        yield ConfigManager()

def test_get_plugin_options(mock_config_manager):
    plugin_type = 'test_plugin_type'
    name = 'test_plugin_name'
    keys = {'option1': 'key_value1', 'option2': 'key_value2'}
    variables = {'var1': 'value1'}
    direct = {'option1': 'direct_value1'}

    options = mock_config_manager.get_plugin_options(plugin_type, name, keys, variables, direct)

    assert options == {
        'option1': 'value_of_option1',
        'option2': 'value_of_option2'
    }
