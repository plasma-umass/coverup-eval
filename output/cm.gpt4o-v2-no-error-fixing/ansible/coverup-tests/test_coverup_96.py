# file: lib/ansible/vars/plugins.py:22-39
# asked: {"lines": [22, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 38, 39], "branches": [[29, 30], [29, 39], [30, 31], [30, 33], [35, 36], [35, 38]]}
# gained: {"lines": [22, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 38, 39], "branches": [[29, 30], [29, 39], [30, 31], [30, 33], [35, 36], [35, 38]]}

import pytest
from unittest.mock import Mock, patch
from ansible.errors import AnsibleError
from ansible.inventory.host import Host
from ansible.vars.plugins import get_plugin_vars

def test_get_plugin_vars_with_get_vars():
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    entities = [Mock()]

    plugin.get_vars.return_value = {'key': 'value'}
    
    result = get_plugin_vars(loader, plugin, path, entities)
    
    assert result == {'key': 'value'}
    plugin.get_vars.assert_called_once_with(loader, path, entities)

def test_get_plugin_vars_with_host_vars():
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    host = Host(name='host1')
    entities = [host]

    plugin.get_vars.side_effect = AttributeError
    plugin.get_host_vars.return_value = {'host_key': 'host_value'}
    
    result = get_plugin_vars(loader, plugin, path, entities)
    
    assert result == {'host_key': 'host_value'}
    plugin.get_host_vars.assert_called_once_with('host1')

def test_get_plugin_vars_with_group_vars():
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
    plugin.get_group_vars.assert_called_once_with('group1')

def test_get_plugin_vars_with_v1_plugin():
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    entities = [Mock()]

    plugin.get_vars.side_effect = AttributeError
    plugin.get_host_vars.side_effect = AttributeError
    plugin.get_group_vars.side_effect = AttributeError
    plugin.run = Mock()
    plugin._load_name = 'plugin_name'
    plugin._original_path = 'plugin_path'
    
    with pytest.raises(AnsibleError, match="Cannot use v1 type vars plugin plugin_name from plugin_path"):
        get_plugin_vars(loader, plugin, path, entities)

def test_get_plugin_vars_with_invalid_plugin():
    loader = Mock()
    plugin = Mock()
    path = 'some_path'
    entities = [Mock()]

    plugin.get_vars.side_effect = AttributeError
    plugin.get_host_vars.side_effect = AttributeError
    plugin.get_group_vars.side_effect = AttributeError
    del plugin.run
    plugin._load_name = 'plugin_name'
    plugin._original_path = 'plugin_path'
    
    with pytest.raises(AnsibleError, match="Invalid vars plugin plugin_name from plugin_path"):
        get_plugin_vars(loader, plugin, path, entities)
