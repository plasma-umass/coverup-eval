# file lib/ansible/config/manager.py:562-567
# lines [562, 564, 565, 567]
# branches ['564->565', '564->567']

import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_initialize_plugin_configuration_definitions(config_manager):
    plugin_type = 'test_plugin_type'
    plugin_name = 'test_plugin_name'
    plugin_defs = {'key1': 'value1', 'key2': 'value2'}

    # Ensure the plugin_type is not already in the _plugins dictionary
    assert plugin_type not in config_manager._plugins

    # Call the method to test
    config_manager.initialize_plugin_configuration_definitions(plugin_type, plugin_name, plugin_defs)

    # Check if the plugin_type and plugin_name have been added correctly
    assert plugin_type in config_manager._plugins
    assert plugin_name in config_manager._plugins[plugin_type]
    assert config_manager._plugins[plugin_type][plugin_name] == plugin_defs

    # Cleanup is not necessary as the ConfigManager instance is function-scoped due to the fixture
