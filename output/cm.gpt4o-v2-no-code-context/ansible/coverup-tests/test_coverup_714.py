# file: lib/ansible/inventory/group.py:79-80
# asked: {"lines": [79, 80], "branches": []}
# gained: {"lines": [79, 80], "branches": []}

import pytest
from ansible.inventory.group import Group

class MockGroup(Group):
    def serialize(self):
        return {'mock': 'data'}

@pytest.fixture
def mock_group():
    return MockGroup()

def test_getstate_executes(mock_group):
    state = mock_group.__getstate__()
    assert state == {'mock': 'data'}
