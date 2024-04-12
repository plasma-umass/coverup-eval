# file lib/ansible/config/manager.py:377-393
# lines [384, 389, 390, 391]
# branches ['383->384', '388->389', '389->390', '389->393', '390->389', '390->391']

import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager(mocker):
    config_manager_instance = ConfigManager()
    mocker.patch.object(config_manager_instance, '_base_defs', {'base_config': 'base_value'})
    mocker.patch.object(config_manager_instance, '_plugins', {
        'plugin_type_a': {
            'plugin_name_a': {'config_a': 'value_a'},
            '_private_config_a': 'private_value_a'
        },
        'plugin_type_b': {}
    })
    return config_manager_instance

def test_get_configuration_definitions_plugin_type_without_name(config_manager):
    # Test the branch where plugin_type is provided but name is None
    result = config_manager.get_configuration_definitions(plugin_type='plugin_type_b')
    assert result == {}, "Expected an empty dictionary for a plugin type without plugins"

def test_get_configuration_definitions_ignore_private(config_manager):
    # Test the branch where ignore_private is True
    result = config_manager.get_configuration_definitions(plugin_type='plugin_type_a', ignore_private=True)
    # The result should be a dictionary with 'plugin_name_a' as a key and its value should not contain '_private_config_a'
    assert 'plugin_name_a' in result, "Expected 'plugin_name_a' to be present in the result"
    assert 'config_a' in result['plugin_name_a'], "Expected 'config_a' to be present in the 'plugin_name_a' config"
    assert '_private_config_a' not in result['plugin_name_a'], "Expected '_private_config_a' to be filtered out due to ignore_private=True"
