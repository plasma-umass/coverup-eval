# file lib/ansible/playbook/play_context.py:156-165
# lines [160, 161, 162, 163, 164, 165]
# branches ['161->exit', '161->162', '162->161', '162->163', '164->161', '164->165']

import pytest
from ansible.playbook.play_context import PlayContext
from ansible.plugins.loader import connection_loader
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleError

# Mocking the ConfigManager to return a specific configuration definition
@pytest.fixture
def mock_config_manager(mocker):
    config_manager = mocker.patch('ansible.config.manager.ConfigManager.get_configuration_definitions')
    config_manager.return_value = {'test_option': {'name': 'test_attribute'}}
    return config_manager

# Mocking a plugin with a specific _load_name and get_option method
@pytest.fixture
def mock_plugin(mocker):
    plugin = mocker.MagicMock()
    plugin._load_name = 'mock_plugin'
    plugin.get_option.return_value = 'test_value'
    return plugin

# Test function to cover lines 160-165
def test_set_attributes_from_plugin(mock_config_manager, mock_plugin):
    play_context = PlayContext()

    # Before setting attributes from plugin
    assert not hasattr(play_context, 'test_attribute')

    # Set attributes from plugin
    play_context.set_attributes_from_plugin(mock_plugin)

    # After setting attributes from plugin
    assert hasattr(play_context, 'test_attribute')
    assert getattr(play_context, 'test_attribute') == 'test_value'

    # Cleanup is not necessary as we are using fixtures with mock objects
