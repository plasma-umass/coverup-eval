# file lib/ansible/config/manager.py:562-567
# lines []
# branches ['564->567']

import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_initialize_plugin_configuration_definitions_new_plugin_type(config_manager, mocker):
    mocker.patch.object(config_manager, '_plugins', new={})
    plugin_type = 'test_plugin_type'
    name = 'test_name'
    defs = {'key': 'value'}

    config_manager.initialize_plugin_configuration_definitions(plugin_type, name, defs)

    assert plugin_type in config_manager._plugins
    assert name in config_manager._plugins[plugin_type]
    assert config_manager._plugins[plugin_type][name] == defs

def test_initialize_plugin_configuration_definitions_existing_plugin_type(config_manager, mocker):
    plugin_type = 'test_plugin_type'
    name = 'test_name'
    defs = {'key': 'value'}
    mocker.patch.object(config_manager, '_plugins', new={plugin_type: {}})

    config_manager.initialize_plugin_configuration_definitions(plugin_type, name, defs)

    assert name in config_manager._plugins[plugin_type]
    assert config_manager._plugins[plugin_type][name] == defs
