# file: lib/ansible/config/data.py:8-43
# asked: {"lines": [8, 10, 11, 12, 14, 16, 17, 18, 19, 20, 22, 24, 26, 27, 28, 29, 30, 32, 34, 36, 37, 39, 40, 41, 42, 43], "branches": [[17, 18], [17, 19], [19, 20], [19, 22], [27, 28], [27, 29], [29, 30], [29, 32], [36, 37], [36, 39], [39, 40], [39, 41], [41, 42], [41, 43]]}
# gained: {"lines": [8, 10, 11, 12, 14, 16, 17, 18, 19, 20, 22, 24, 26, 27, 28, 29, 30, 32, 34, 36, 37, 39, 40, 41, 42, 43], "branches": [[17, 18], [17, 19], [19, 20], [27, 28], [27, 29], [29, 30], [36, 37], [36, 39], [39, 40], [41, 42]]}

import pytest

class MockPlugin:
    def __init__(self, type, name):
        self.type = type
        self.name = name

class MockSetting:
    def __init__(self, name, value):
        self.name = name
        self.value = value

@pytest.fixture
def config_data():
    from ansible.config.data import ConfigData
    return ConfigData()

def test_get_setting_global(config_data):
    setting = MockSetting('test_setting', 'test_value')
    config_data._global_settings[setting.name] = setting
    result = config_data.get_setting('test_setting')
    assert result == setting

def test_get_setting_plugin(config_data):
    plugin = MockPlugin('test_type', 'test_plugin')
    setting = MockSetting('test_setting', 'test_value')
    config_data._plugins[plugin.type] = {plugin.name: {setting.name: setting}}
    result = config_data.get_setting('test_setting', plugin)
    assert result == setting

def test_get_settings_global(config_data):
    setting1 = MockSetting('test_setting1', 'test_value1')
    setting2 = MockSetting('test_setting2', 'test_value2')
    config_data._global_settings[setting1.name] = setting1
    config_data._global_settings[setting2.name] = setting2
    result = config_data.get_settings()
    assert setting1 in result
    assert setting2 in result

def test_get_settings_plugin(config_data):
    plugin = MockPlugin('test_type', 'test_plugin')
    setting1 = MockSetting('test_setting1', 'test_value1')
    setting2 = MockSetting('test_setting2', 'test_value2')
    config_data._plugins[plugin.type] = {plugin.name: {setting1.name: setting1, setting2.name: setting2}}
    result = config_data.get_settings(plugin)
    assert setting1 in result
    assert setting2 in result

def test_update_setting_global(config_data):
    setting = MockSetting('test_setting', 'test_value')
    config_data.update_setting(setting)
    assert config_data._global_settings[setting.name] == setting

def test_update_setting_plugin(config_data):
    plugin = MockPlugin('test_type', 'test_plugin')
    setting = MockSetting('test_setting', 'test_value')
    config_data.update_setting(setting, plugin)
    assert config_data._plugins[plugin.type][plugin.name][setting.name] == setting

def test_update_setting_plugin_new_type(config_data):
    plugin = MockPlugin('new_type', 'test_plugin')
    setting = MockSetting('test_setting', 'test_value')
    config_data.update_setting(setting, plugin)
    assert config_data._plugins[plugin.type][plugin.name][setting.name] == setting

def test_update_setting_plugin_new_name(config_data):
    plugin = MockPlugin('test_type', 'new_plugin')
    setting = MockSetting('test_setting', 'test_value')
    config_data.update_setting(setting, plugin)
    assert config_data._plugins[plugin.type][plugin.name][setting.name] == setting
