# file lib/ansible/config/manager.py:377-393
# lines [384, 389, 390, 391]
# branches ['383->384', '388->389', '389->390', '389->393', '390->389', '390->391']

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def config_manager():
    from ansible.config.manager import ConfigManager
    return ConfigManager()

def test_get_configuration_definitions_plugin_type(config_manager, mocker):
    # Mock the _plugins attribute
    config_manager._plugins = {
        'test_plugin': {
            'setting1': 'value1',
            '_private_setting': 'private_value'
        }
    }

    # Test when plugin_type is provided and name is None
    result = config_manager.get_configuration_definitions(plugin_type='test_plugin', name=None, ignore_private=False)
    assert result == {
        'setting1': 'value1',
        '_private_setting': 'private_value'
    }

def test_get_configuration_definitions_ignore_private(config_manager, mocker):
    # Mock the _plugins attribute
    config_manager._plugins = {
        'test_plugin': {
            'setting1': 'value1',
            '_private_setting': 'private_value'
        }
    }

    # Test when plugin_type is provided, name is None, and ignore_private is True
    result = config_manager.get_configuration_definitions(plugin_type='test_plugin', name=None, ignore_private=True)
    assert result == {
        'setting1': 'value1'
    }
