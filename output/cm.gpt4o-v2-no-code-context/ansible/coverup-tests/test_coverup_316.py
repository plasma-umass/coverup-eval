# file: lib/ansible/config/manager.py:365-375
# asked: {"lines": [365, 367, 368, 369, 370, 371, 373, 375], "branches": [[368, 369], [368, 370], [370, 371], [370, 373]]}
# gained: {"lines": [365, 367, 368, 369, 370, 371, 373, 375], "branches": [[368, 369], [368, 370], [370, 371], [370, 373]]}

import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_get_configuration_definition_base_def(config_manager, monkeypatch):
    monkeypatch.setattr(config_manager, '_base_defs', {'test_name': 'test_value'})
    result = config_manager.get_configuration_definition('test_name')
    assert result == 'test_value'

def test_get_configuration_definition_plugin_type(config_manager, monkeypatch):
    monkeypatch.setattr(config_manager, '_plugins', {'test_type': {'test_name': 'test_value'}})
    result = config_manager.get_configuration_definition('test_name', plugin_type='test_type')
    assert result == 'test_value'

def test_get_configuration_definition_plugin_name(config_manager, monkeypatch):
    monkeypatch.setattr(config_manager, '_plugins', {'test_type': {'test_plugin': {'test_name': 'test_value'}}})
    result = config_manager.get_configuration_definition('test_name', plugin_type='test_type', plugin_name='test_plugin')
    assert result == 'test_value'

def test_get_configuration_definition_none(config_manager, monkeypatch):
    monkeypatch.setattr(config_manager, '_base_defs', {})
    monkeypatch.setattr(config_manager, '_plugins', {})
    result = config_manager.get_configuration_definition('non_existent_name')
    assert result is None
