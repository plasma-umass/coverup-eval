# file lib/ansible/config/manager.py:562-567
# lines [562, 564, 565, 567]
# branches ['564->565', '564->567']

import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_initialize_plugin_configuration_definitions(config_manager, mocker):
    # Mock the _plugins attribute to ensure it starts empty
    mocker.patch.object(config_manager, '_plugins', {})

    plugin_type = 'test_plugin_type'
    name = 'test_plugin_name'
    defs = {'key': 'value'}

    # Call the method to test
    config_manager.initialize_plugin_configuration_definitions(plugin_type, name, defs)

    # Assertions to verify the postconditions
    assert plugin_type in config_manager._plugins
    assert name in config_manager._plugins[plugin_type]
    assert config_manager._plugins[plugin_type][name] == defs
