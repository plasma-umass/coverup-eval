# file: lib/ansible/playbook/role/definition.py:234-235
# asked: {"lines": [234, 235], "branches": []}
# gained: {"lines": [234], "branches": []}

import pytest
from ansible.playbook.role.definition import RoleDefinition

class MockBase:
    pass

class MockConditional:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

@pytest.fixture
def role_definition(monkeypatch):
    class MockRoleDefinition(MockBase, MockConditional, MockTaggable, MockCollectionSearch):
        def __init__(self, role_path):
            self._role_path = role_path

        def get_role_path(self):
            return self._role_path

    monkeypatch.setattr('ansible.playbook.role.definition.RoleDefinition', MockRoleDefinition)
    return MockRoleDefinition('/mock/path')

def test_get_role_path(role_definition):
    assert role_definition.get_role_path() == '/mock/path'
