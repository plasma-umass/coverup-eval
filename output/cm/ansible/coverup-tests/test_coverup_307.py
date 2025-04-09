# file lib/ansible/inventory/group.py:102-114
# lines [102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114]
# branches ['111->exit', '111->112']

import pytest
from ansible.inventory.group import Group

# Assuming the Group class has a parent_groups attribute initialized as an empty list
# and a __init__ method that initializes the necessary attributes.

@pytest.fixture
def group_data():
    return {
        'name': 'testgroup',
        'vars': {'key1': 'value1'},
        'depth': 1,
        'hosts': ['host1', 'host2'],
        'parent_groups': [
            {'name': 'parent1', 'vars': {'key2': 'value2'}, 'depth': 0, 'hosts': ['host3']},
            {'name': 'parent2', 'vars': {'key3': 'value3'}, 'depth': 0, 'hosts': ['host4']}
        ]
    }

def test_group_deserialize_with_parent_groups(group_data):
    group = Group()
    group.deserialize(group_data)

    assert group.name == 'testgroup'
    assert group.vars == {'key1': 'value1'}
    assert group.depth == 1
    assert group.hosts == ['host1', 'host2']
    assert len(group.parent_groups) == 2

    parent_group1 = group.parent_groups[0]
    assert parent_group1.name == 'parent1'
    assert parent_group1.vars == {'key2': 'value2'}
    assert parent_group1.depth == 0
    assert parent_group1.hosts == ['host3']

    parent_group2 = group.parent_groups[1]
    assert parent_group2.name == 'parent2'
    assert parent_group2.vars == {'key3': 'value3'}
    assert parent_group2.depth == 0
    assert parent_group2.hosts == ['host4']
