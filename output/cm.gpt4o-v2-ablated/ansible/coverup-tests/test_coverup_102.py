# file: lib/ansible/playbook/helpers.py:323-346
# asked: {"lines": [323, 335, 337, 338, 340, 341, 342, 343, 344, 346], "branches": [[337, 338], [337, 340], [341, 342], [341, 346]]}
# gained: {"lines": [323, 335, 337, 338, 340, 341, 342, 343, 344, 346], "branches": [[337, 338], [337, 340], [341, 342], [341, 346]]}

import pytest
from ansible.playbook.helpers import load_list_of_roles
from ansible.playbook.role.include import RoleInclude
from ansible.errors import AnsibleAssertionError

class MockRoleInclude:
    @staticmethod
    def load(role_def, play, current_role_path=None, variable_manager=None, loader=None, collection_list=None):
        return f"RoleInclude({role_def})"

@pytest.fixture
def mock_role_include(monkeypatch):
    monkeypatch.setattr(RoleInclude, 'load', MockRoleInclude.load)

def test_load_list_of_roles_with_valid_list(mock_role_include):
    ds = [{'name': 'role1'}, {'name': 'role2'}]
    play = 'mock_play'
    roles = load_list_of_roles(ds, play)
    assert roles == ["RoleInclude({'name': 'role1'})", "RoleInclude({'name': 'role2'})"]

def test_load_list_of_roles_with_empty_list(mock_role_include):
    ds = []
    play = 'mock_play'
    roles = load_list_of_roles(ds, play)
    assert roles == []

def test_load_list_of_roles_with_invalid_ds():
    ds = 'not_a_list'
    play = 'mock_play'
    with pytest.raises(AnsibleAssertionError) as excinfo:
        load_list_of_roles(ds, play)
    assert 'ds (not_a_list) should be a list but was a' in str(excinfo.value)
