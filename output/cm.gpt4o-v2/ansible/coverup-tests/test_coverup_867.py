# file: lib/ansible/inventory/group.py:79-80
# asked: {"lines": [79, 80], "branches": []}
# gained: {"lines": [79, 80], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.group import Group

def test_group_getstate(monkeypatch):
    # Mock the to_safe_group_name function if necessary
    monkeypatch.setattr('ansible.inventory.group.to_safe_group_name', lambda x: x)

    parent_group = MagicMock(spec=Group)
    parent_group.serialize.return_value = {'name': 'parent', 'vars': {}, 'parent_groups': [], 'depth': 1, 'hosts': []}
    
    group = Group(name='test')
    group.vars = {'var1': 'value1'}
    group.parent_groups = [parent_group]
    group.depth = 0
    group.hosts = ['host1']
    
    state = group.__getstate__()
    
    assert state['name'] == 'test'
    assert state['vars'] == {'var1': 'value1'}
    assert state['parent_groups'] == [{'name': 'parent', 'vars': {}, 'parent_groups': [], 'depth': 1, 'hosts': []}]
    assert state['depth'] == 0
    assert state['hosts'] == ['host1']
