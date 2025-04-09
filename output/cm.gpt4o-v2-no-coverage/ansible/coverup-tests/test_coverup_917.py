# file: lib/ansible/playbook/role_include.py:68-70
# asked: {"lines": [68, 70], "branches": []}
# gained: {"lines": [68, 70], "branches": []}

import pytest
from ansible.playbook.role_include import IncludeRole

class MockIncludeRole(IncludeRole):
    def __init__(self, name=None, action=None, role_name=None):
        super().__init__()
        self.name = name
        self.action = action
        self._role_name = role_name

@pytest.fixture
def mock_include_role():
    return MockIncludeRole()

def test_get_name_with_name(mock_include_role):
    mock_include_role.name = "test_name"
    assert mock_include_role.get_name() == "test_name"

def test_get_name_without_name(mock_include_role):
    mock_include_role.name = None
    mock_include_role.action = "test_action"
    mock_include_role._role_name = "test_role"
    assert mock_include_role.get_name() == "test_action : test_role"
