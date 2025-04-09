# file: lib/ansible/inventory/group.py:82-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest
from ansible.inventory.group import Group

def test_group_setstate():
    group = Group()
    data = {
        'name': 'test_group',
        'vars': {'var1': 'value1'},
        'depth': 1,
        'hosts': ['host1', 'host2'],
        'parent_groups': [{'name': 'parent_group'}]
    }
    
    group.__setstate__(data)
    
    assert group.name == 'test_group'
    assert group.vars == {'var1': 'value1'}
    assert group.depth == 1
    assert group.hosts == ['host1', 'host2']
    assert len(group.parent_groups) == 1
    assert group.parent_groups[0].name == 'parent_group'
