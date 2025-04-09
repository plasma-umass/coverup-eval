# file: lib/ansible/config/manager.py:377-393
# asked: {"lines": [377, 380, 381, 382, 383, 384, 386, 388, 389, 390, 391, 393], "branches": [[381, 382], [381, 383], [383, 384], [383, 386], [388, 389], [388, 393], [389, 390], [389, 393], [390, 389], [390, 391]]}
# gained: {"lines": [377, 380, 381, 382, 383, 384, 386, 388, 389, 390, 391, 393], "branches": [[381, 382], [381, 383], [383, 384], [383, 386], [388, 389], [388, 393], [389, 390], [389, 393], [390, 389], [390, 391]]}

import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_get_configuration_definitions_base_defs(config_manager, mocker):
    mocker.patch.object(config_manager, '_base_defs', {'setting1': 'value1', '_private_setting': 'value2'})
    result = config_manager.get_configuration_definitions()
    assert result == {'setting1': 'value1', '_private_setting': 'value2'}

def test_get_configuration_definitions_plugin_type(config_manager, mocker):
    mocker.patch.object(config_manager, '_plugins', {'plugin_type1': {'setting2': 'value3'}})
    result = config_manager.get_configuration_definitions(plugin_type='plugin_type1')
    assert result == {'setting2': 'value3'}

def test_get_configuration_definitions_plugin_name(config_manager, mocker):
    mocker.patch.object(config_manager, '_plugins', {'plugin_type1': {'plugin_name1': {'setting3': 'value4'}}})
    result = config_manager.get_configuration_definitions(plugin_type='plugin_type1', name='plugin_name1')
    assert result == {'setting3': 'value4'}

def test_get_configuration_definitions_ignore_private(config_manager, mocker):
    mocker.patch.object(config_manager, '_base_defs', {'setting1': 'value1', '_private_setting': 'value2'})
    result = config_manager.get_configuration_definitions(ignore_private=True)
    assert result == {'setting1': 'value1'}
