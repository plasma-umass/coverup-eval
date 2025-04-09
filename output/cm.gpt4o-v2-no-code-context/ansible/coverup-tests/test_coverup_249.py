# file: lib/ansible/inventory/group.py:102-114
# asked: {"lines": [102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114], "branches": [[111, 0], [111, 112]]}
# gained: {"lines": [102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114], "branches": [[111, 0], [111, 112]]}

import pytest
from ansible.inventory.group import Group

@pytest.fixture
def group():
    return Group()

def test_deserialize_no_parent_groups(group):
    data = {
        'name': 'test_group',
        'vars': {'var1': 'value1'},
        'depth': 1,
        'hosts': ['host1', 'host2']
    }
    group.deserialize(data)
    
    assert group.name == 'test_group'
    assert group.vars == {'var1': 'value1'}
    assert group.depth == 1
    assert group.hosts == ['host1', 'host2']
    assert group._hosts is None
    assert group.parent_groups == []

def test_deserialize_with_parent_groups(group):
    data = {
        'name': 'test_group',
        'vars': {'var1': 'value1'},
        'depth': 1,
        'hosts': ['host1', 'host2'],
        'parent_groups': [
            {
                'name': 'parent_group1',
                'vars': {'var2': 'value2'},
                'depth': 2,
                'hosts': ['host3'],
                'parent_groups': []
            },
            {
                'name': 'parent_group2',
                'vars': {'var3': 'value3'},
                'depth': 3,
                'hosts': ['host4'],
                'parent_groups': []
            }
        ]
    }
    group.deserialize(data)
    
    assert group.name == 'test_group'
    assert group.vars == {'var1': 'value1'}
    assert group.depth == 1
    assert group.hosts == ['host1', 'host2']
    assert group._hosts is None
    assert len(group.parent_groups) == 2
    
    parent_group1 = group.parent_groups[0]
    assert parent_group1.name == 'parent_group1'
    assert parent_group1.vars == {'var2': 'value2'}
    assert parent_group1.depth == 2
    assert parent_group1.hosts == ['host3']
    assert parent_group1._hosts is None
    assert parent_group1.parent_groups == []
    
    parent_group2 = group.parent_groups[1]
    assert parent_group2.name == 'parent_group2'
    assert parent_group2.vars == {'var3': 'value3'}
    assert parent_group2.depth == 3
    assert parent_group2.hosts == ['host4']
    assert parent_group2._hosts is None
    assert parent_group2.parent_groups == []
