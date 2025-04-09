# file: lib/ansible/vars/plugins.py:22-39
# asked: {"lines": [24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 38, 39], "branches": [[29, 30], [29, 39], [30, 31], [30, 33], [35, 36], [35, 38]]}
# gained: {"lines": [24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 38, 39], "branches": [[29, 30], [29, 39], [30, 31], [30, 33], [35, 36], [35, 38]]}

import pytest
from unittest.mock import Mock, create_autospec
from ansible.errors import AnsibleError
from ansible.inventory.host import Host
from ansible.inventory.group import Group

def test_get_plugin_vars_with_get_vars(monkeypatch):
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    entities = [Mock()]

    plugin.get_vars.return_value = {'key': 'value'}
    
    from ansible.vars.plugins import get_plugin_vars
    result = get_plugin_vars(loader, plugin, path, entities)
    
    assert result == {'key': 'value'}
    plugin.get_vars.assert_called_once_with(loader, path, entities)

def test_get_plugin_vars_with_host_vars(monkeypatch):
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    host = create_autospec(Host, instance=True)
    host.name = 'host1'
    entities = [host]

    plugin.get_host_vars.return_value = {'host_key': 'host_value'}
    del plugin.get_vars  # Ensure get_vars does not exist

    from ansible.vars.plugins import get_plugin_vars
    result = get_plugin_vars(loader, plugin, path, entities)
    
    assert result == {'host_key': 'host_value'}
    plugin.get_host_vars.assert_called_once_with('host1')

def test_get_plugin_vars_with_group_vars(monkeypatch):
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    group = create_autospec(Group, instance=True)
    group.name = 'group1'
    entities = [group]

    plugin.get_group_vars.return_value = {'group_key': 'group_value'}
    del plugin.get_vars  # Ensure get_vars does not exist

    from ansible.vars.plugins import get_plugin_vars
    result = get_plugin_vars(loader, plugin, path, entities)
    
    assert result == {'group_key': 'group_value'}
    plugin.get_group_vars.assert_called_once_with('group1')

def test_get_plugin_vars_with_v1_type_plugin(monkeypatch):
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    entities = [Mock()]

    plugin._load_name = 'plugin_name'
    plugin._original_path = 'plugin_path'
    plugin.run = Mock()
    del plugin.get_vars  # Ensure get_vars does not exist
    del plugin.get_host_vars  # Ensure get_host_vars does not exist
    del plugin.get_group_vars  # Ensure get_group_vars does not exist

    from ansible.vars.plugins import get_plugin_vars
    with pytest.raises(AnsibleError, match="Cannot use v1 type vars plugin plugin_name from plugin_path"):
        get_plugin_vars(loader, plugin, path, entities)

def test_get_plugin_vars_with_invalid_plugin(monkeypatch):
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    entities = [Mock()]

    plugin._load_name = 'plugin_name'
    plugin._original_path = 'plugin_path'
    del plugin.get_vars  # Ensure get_vars does not exist
    del plugin.get_host_vars  # Ensure get_host_vars does not exist
    del plugin.get_group_vars  # Ensure get_group_vars does not exist
    del plugin.run  # Ensure run does not exist

    from ansible.vars.plugins import get_plugin_vars
    with pytest.raises(AnsibleError, match="Invalid vars plugin plugin_name from plugin_path"):
        get_plugin_vars(loader, plugin, path, entities)
