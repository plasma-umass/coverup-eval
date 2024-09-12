# file: lib/ansible/vars/plugins.py:22-39
# asked: {"lines": [24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 38, 39], "branches": [[29, 30], [29, 39], [30, 31], [30, 33], [35, 36], [35, 38]]}
# gained: {"lines": [24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 38, 39], "branches": [[29, 30], [29, 39], [30, 31], [30, 33], [35, 36], [35, 38]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.host import Host
from unittest.mock import Mock

from ansible.vars.plugins import get_plugin_vars

def test_get_plugin_vars_with_get_vars(monkeypatch):
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    entities = [Mock()]

    plugin.get_vars.return_value = {'key': 'value'}
    result = get_plugin_vars(loader, plugin, path, entities)
    assert result == {'key': 'value'}

def test_get_plugin_vars_with_host_vars(monkeypatch):
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    host = Mock(spec=Host)
    host.name = 'host1'
    entities = [host]

    plugin.get_vars.side_effect = AttributeError
    plugin.get_host_vars.return_value = {'host_key': 'host_value'}
    result = get_plugin_vars(loader, plugin, path, entities)
    assert result == {'host_key': 'host_value'}

def test_get_plugin_vars_with_group_vars(monkeypatch):
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    group = Mock()
    group.name = 'group1'
    entities = [group]

    plugin.get_vars.side_effect = AttributeError
    plugin.get_group_vars.return_value = {'group_key': 'group_value'}
    result = get_plugin_vars(loader, plugin, path, entities)
    assert result == {'group_key': 'group_value'}

def test_get_plugin_vars_with_v1_plugin(monkeypatch):
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    entities = [Mock()]

    plugin.get_vars.side_effect = AttributeError
    plugin.get_host_vars.side_effect = AttributeError
    plugin.get_group_vars.side_effect = AttributeError
    plugin.run = Mock()

    with pytest.raises(AnsibleError, match="Cannot use v1 type vars plugin"):
        get_plugin_vars(loader, plugin, path, entities)

def test_get_plugin_vars_with_invalid_plugin(monkeypatch):
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    entities = [Mock()]

    plugin.get_vars.side_effect = AttributeError
    plugin.get_host_vars.side_effect = AttributeError
    plugin.get_group_vars.side_effect = AttributeError
    del plugin.run

    with pytest.raises(AnsibleError, match="Invalid vars plugin"):
        get_plugin_vars(loader, plugin, path, entities)
