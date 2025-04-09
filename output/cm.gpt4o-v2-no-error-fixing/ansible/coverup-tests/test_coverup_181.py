# file: lib/ansible/playbook/helpers.py:323-346
# asked: {"lines": [323, 335, 337, 338, 340, 341, 342, 343, 344, 346], "branches": [[337, 338], [337, 340], [341, 342], [341, 346]]}
# gained: {"lines": [323, 335, 337, 338, 340, 341, 342, 343, 344, 346], "branches": [[337, 338], [337, 340], [341, 342], [341, 346]]}

import pytest
from ansible.errors import AnsibleAssertionError, AnsibleError, AnsibleParserError
from ansible.playbook.helpers import load_list_of_roles
from ansible.playbook.role.include import RoleInclude
from unittest.mock import MagicMock

def test_load_list_of_roles_with_invalid_ds():
    play = MagicMock()
    with pytest.raises(AnsibleAssertionError, match=r"ds \(.*\) should be a list but was a .*"):
        load_list_of_roles("not_a_list", play)

def test_load_list_of_roles_with_valid_ds(mocker):
    play = MagicMock()
    role_def = {"name": "test_role"}
    ds = [role_def]
    
    mock_role_include = mocker.patch('ansible.playbook.role.include.RoleInclude.load', return_value="mock_role")
    
    roles = load_list_of_roles(ds, play)
    
    mock_role_include.assert_called_once_with(role_def, play=play, current_role_path=None, variable_manager=None, loader=None, collection_list=None)
    assert roles == ["mock_role"]

def test_load_list_of_roles_with_multiple_roles(mocker):
    play = MagicMock()
    role_def1 = {"name": "test_role1"}
    role_def2 = {"name": "test_role2"}
    ds = [role_def1, role_def2]
    
    mock_role_include = mocker.patch('ansible.playbook.role.include.RoleInclude.load', side_effect=["mock_role1", "mock_role2"])
    
    roles = load_list_of_roles(ds, play)
    
    assert mock_role_include.call_count == 2
    mock_role_include.assert_any_call(role_def1, play=play, current_role_path=None, variable_manager=None, loader=None, collection_list=None)
    mock_role_include.assert_any_call(role_def2, play=play, current_role_path=None, variable_manager=None, loader=None, collection_list=None)
    assert roles == ["mock_role1", "mock_role2"]
