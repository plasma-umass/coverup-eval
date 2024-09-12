# file: lib/ansible/config/manager.py:562-567
# asked: {"lines": [562, 564, 565, 567], "branches": [[564, 565], [564, 567]]}
# gained: {"lines": [562, 564, 565, 567], "branches": [[564, 565], [564, 567]]}

import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_initialize_plugin_configuration_definitions_new_plugin_type(config_manager):
    plugin_type = 'test_plugin_type'
    name = 'test_name'
    defs = {'key': 'value'}
    
    config_manager.initialize_plugin_configuration_definitions(plugin_type, name, defs)
    
    assert plugin_type in config_manager._plugins
    assert name in config_manager._plugins[plugin_type]
    assert config_manager._plugins[plugin_type][name] == defs

def test_initialize_plugin_configuration_definitions_existing_plugin_type(config_manager):
    plugin_type = 'test_plugin_type'
    name1 = 'test_name1'
    defs1 = {'key1': 'value1'}
    name2 = 'test_name2'
    defs2 = {'key2': 'value2'}
    
    config_manager.initialize_plugin_configuration_definitions(plugin_type, name1, defs1)
    config_manager.initialize_plugin_configuration_definitions(plugin_type, name2, defs2)
    
    assert plugin_type in config_manager._plugins
    assert name1 in config_manager._plugins[plugin_type]
    assert config_manager._plugins[plugin_type][name1] == defs1
    assert name2 in config_manager._plugins[plugin_type]
    assert config_manager._plugins[plugin_type][name2] == defs2
