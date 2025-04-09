# file: lib/ansible/playbook/role/definition.py:234-235
# asked: {"lines": [235], "branches": []}
# gained: {"lines": [235], "branches": []}

import pytest
from ansible.playbook.role.definition import RoleDefinition

class MockBase:
    def __init__(self):
        pass

class MockConditional:
    def __init__(self):
        pass

class MockTaggable:
    def __init__(self):
        pass

class MockCollectionSearch:
    def __init__(self):
        pass

@pytest.fixture
def role_definition():
    class TestRoleDefinition(MockBase, MockConditional, MockTaggable, MockCollectionSearch, RoleDefinition):
        def __init__(self, play=None, role_basedir=None, variable_manager=None, loader=None, collection_list=None):
            MockBase.__init__(self)
            MockConditional.__init__(self)
            MockTaggable.__init__(self)
            MockCollectionSearch.__init__(self)
            RoleDefinition.__init__(self, play, role_basedir, variable_manager, loader, collection_list)
    return TestRoleDefinition()

def test_get_role_path(role_definition):
    role_definition._role_path = "/path/to/role"
    assert role_definition.get_role_path() == "/path/to/role"
