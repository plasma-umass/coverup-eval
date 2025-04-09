# file: lib/ansible/config/manager.py:562-567
# asked: {"lines": [562, 564, 565, 567], "branches": [[564, 565], [564, 567]]}
# gained: {"lines": [562, 564, 565, 567], "branches": [[564, 565], [564, 567]]}

import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_initialize_plugin_configuration_definitions_new_plugin_type(config_manager):
    plugin_type = 'test_plugin'
    name = 'test_name'
    defs = {'key': 'value'}
    
    # Ensure the plugin type does not exist initially
    assert plugin_type not in config_manager._plugins
    
    # Call the method
    config_manager.initialize_plugin_configuration_definitions(plugin_type, name, defs)
    
    # Verify the plugin type and name are added correctly
    assert plugin_type in config_manager._plugins
    assert name in config_manager._plugins[plugin_type]
    assert config_manager._plugins[plugin_type][name] == defs

def test_initialize_plugin_configuration_definitions_existing_plugin_type(config_manager):
    plugin_type = 'test_plugin'
    name1 = 'test_name1'
    name2 = 'test_name2'
    defs1 = {'key1': 'value1'}
    defs2 = {'key2': 'value2'}
    
    # Prepopulate the _plugins dictionary
    config_manager._plugins[plugin_type] = {name1: defs1}
    
    # Ensure the initial state is correct
    assert plugin_type in config_manager._plugins
    assert name1 in config_manager._plugins[plugin_type]
    assert config_manager._plugins[plugin_type][name1] == defs1
    
    # Call the method with a new name
    config_manager.initialize_plugin_configuration_definitions(plugin_type, name2, defs2)
    
    # Verify the new name is added correctly
    assert name2 in config_manager._plugins[plugin_type]
    assert config_manager._plugins[plugin_type][name2] == defs2
    # Ensure the old name still exists
    assert config_manager._plugins[plugin_type][name1] == defs1
