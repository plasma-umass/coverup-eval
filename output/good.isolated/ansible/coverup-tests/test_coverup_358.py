# file lib/ansible/config/manager.py:365-375
# lines [365, 367, 368, 369, 370, 371, 373, 375]
# branches ['368->369', '368->370', '370->371', '370->373']

import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    cm = ConfigManager()
    cm._base_defs = {'base_key': 'base_value'}
    cm._plugins = {
        'plugin_type_a': {
            'plugin_name_a': {'key_a': 'value_a'},
            'key_b': 'value_b'
        }
    }
    return cm

def test_get_configuration_definition_base(config_manager):
    assert config_manager.get_configuration_definition('base_key') == 'base_value'
    assert config_manager.get_configuration_definition('nonexistent_key') is None

def test_get_configuration_definition_plugin_type(config_manager):
    assert config_manager.get_configuration_definition('key_b', plugin_type='plugin_type_a') == 'value_b'
    assert config_manager.get_configuration_definition('nonexistent_key', plugin_type='plugin_type_a') is None

def test_get_configuration_definition_plugin_name(config_manager):
    assert config_manager.get_configuration_definition('key_a', plugin_type='plugin_type_a', plugin_name='plugin_name_a') == 'value_a'
    assert config_manager.get_configuration_definition('nonexistent_key', plugin_type='plugin_type_a', plugin_name='plugin_name_a') is None
