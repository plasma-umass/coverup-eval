# file: lib/ansible/inventory/group.py:82-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest
from ansible.inventory.group import Group

def test_group_setstate():
    group = Group(name="test_group")
    data = {
        'name': 'new_name',
        'vars': {'var1': 'value1'},
        'depth': 2,
        'hosts': ['host1', 'host2'],
        'parent_groups': [{'name': 'parent1'}, {'name': 'parent2'}]
    }
    
    group.__setstate__(data)
    
    assert group.name == 'new_name'
    assert group.vars == {'var1': 'value1'}
    assert group.depth == 2
    assert group.hosts == ['host1', 'host2']
    assert len(group.parent_groups) == 2
    assert group.parent_groups[0].name == 'parent1'
    assert group.parent_groups[1].name == 'parent2'
