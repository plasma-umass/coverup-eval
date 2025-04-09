# file: lib/ansible/inventory/group.py:85-100
# asked: {"lines": [85, 86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 100], "branches": [[87, 88], [87, 90]]}
# gained: {"lines": [85, 86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 100], "branches": [[87, 88], [87, 90]]}

import pytest
from ansible.inventory.group import Group

def test_serialize(monkeypatch):
    # Create a mock parent group with a serialize method
    class MockParentGroup:
        def serialize(self):
            return {'name': 'mock_parent'}

    # Create a Group instance and set up its attributes
    group = Group(name='test_group')
    group.vars = {'var1': 'value1'}
    group.depth = 1
    group.hosts = ['host1', 'host2']
    group.parent_groups = [MockParentGroup()]

    # Call the serialize method
    result = group.serialize()

    # Assertions to verify the result
    assert result['name'] == 'test_group'
    assert result['vars'] == {'var1': 'value1'}
    assert result['parent_groups'] == [{'name': 'mock_parent'}]
    assert result['depth'] == 1
    assert result['hosts'] == ['host1', 'host2']

    # Clean up
    monkeypatch.undo()
