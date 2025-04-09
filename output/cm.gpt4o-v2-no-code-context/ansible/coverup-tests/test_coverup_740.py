# file: lib/ansible/playbook/role_include.py:68-70
# asked: {"lines": [68, 70], "branches": []}
# gained: {"lines": [68, 70], "branches": []}

import pytest
from ansible.playbook.role_include import IncludeRole

class MockTaskInclude:
    def __init__(self, name=None, action=None, role_name=None):
        self.name = name
        self.action = action
        self._role_name = role_name

@pytest.fixture
def include_role(monkeypatch):
    def mock_init(self, name=None, action=None, role_name=None):
        self.name = name
        self.action = action
        self._role_name = role_name
        self._squashed = False
        self._finalized = False

    monkeypatch.setattr(IncludeRole, '__init__', mock_init)
    return IncludeRole()

def test_get_name_with_name(include_role):
    include_role.name = "test_name"
    assert include_role.get_name() == "test_name"

def test_get_name_without_name(include_role):
    include_role.name = None
    include_role.action = "test_action"
    include_role._role_name = "test_role"
    assert include_role.get_name() == "test_action : test_role"
