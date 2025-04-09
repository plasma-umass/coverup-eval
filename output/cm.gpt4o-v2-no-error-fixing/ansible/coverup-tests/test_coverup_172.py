# file: lib/ansible/inventory/group.py:102-114
# asked: {"lines": [102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114], "branches": [[111, 0], [111, 112]]}
# gained: {"lines": [102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114], "branches": [[111, 0], [111, 112]]}

import pytest
from ansible.inventory.group import Group

def test_deserialize_with_parent_groups():
    data = {
        'name': 'group1',
        'vars': {'var1': 'value1'},
        'depth': 1,
        'hosts': ['host1', 'host2'],
        'parent_groups': [
            {
                'name': 'parent1',
                'vars': {'var2': 'value2'},
                'depth': 2,
                'hosts': ['host3'],
                'parent_groups': []
            },
            {
                'name': 'parent2',
                'vars': {'var3': 'value3'},
                'depth': 3,
                'hosts': ['host4'],
                'parent_groups': []
            }
        ]
    }

    group = Group()
    group.deserialize(data)

    assert group.name == 'group1'
    assert group.vars == {'var1': 'value1'}
    assert group.depth == 1
    assert group.hosts == ['host1', 'host2']
    assert group._hosts is None
    assert len(group.parent_groups) == 2

    parent1 = group.parent_groups[0]
    assert parent1.name == 'parent1'
    assert parent1.vars == {'var2': 'value2'}
    assert parent1.depth == 2
    assert parent1.hosts == ['host3']
    assert parent1._hosts is None

    parent2 = group.parent_groups[1]
    assert parent2.name == 'parent2'
    assert parent2.vars == {'var3': 'value3'}
    assert parent2.depth == 3
    assert parent2.hosts == ['host4']
    assert parent2._hosts is None
