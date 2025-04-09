# file: lib/ansible/playbook/helpers.py:323-346
# asked: {"lines": [323, 335, 337, 338, 340, 341, 342, 343, 344, 346], "branches": [[337, 338], [337, 340], [341, 342], [341, 346]]}
# gained: {"lines": [323, 335, 337, 338, 340, 341, 342, 343, 344, 346], "branches": [[337, 338], [337, 340], [341, 342], [341, 346]]}

import pytest
from ansible.errors import AnsibleAssertionError, AnsibleParserError, AnsibleError
from ansible.playbook.helpers import load_list_of_roles
from ansible.playbook.role.include import RoleInclude
from unittest.mock import MagicMock

def test_load_list_of_roles_with_invalid_ds():
    with pytest.raises(AnsibleAssertionError):
        load_list_of_roles("not_a_list", play=MagicMock())

def test_load_list_of_roles_with_valid_ds(monkeypatch):
    mock_role_include = MagicMock()
    monkeypatch.setattr(RoleInclude, 'load', mock_role_include)
    
    ds = [{'name': 'role1'}, {'name': 'role2'}]
    play = MagicMock()
    current_role_path = '/path/to/role'
    variable_manager = MagicMock()
    loader = MagicMock()
    collection_search_list = ['collection1', 'collection2']
    
    roles = load_list_of_roles(ds, play, current_role_path, variable_manager, loader, collection_search_list)
    
    assert len(roles) == 2
    assert mock_role_include.call_count == 2
    mock_role_include.assert_any_call(ds[0], play=play, current_role_path=current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_search_list)
    mock_role_include.assert_any_call(ds[1], play=play, current_role_path=current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_search_list)
