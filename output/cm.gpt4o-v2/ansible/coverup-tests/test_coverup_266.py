# file: lib/ansible/playbook/helpers.py:323-346
# asked: {"lines": [323, 335, 337, 338, 340, 341, 342, 343, 344, 346], "branches": [[337, 338], [337, 340], [341, 342], [341, 346]]}
# gained: {"lines": [323, 335, 337, 338, 340, 341, 342, 343, 344, 346], "branches": [[337, 338], [337, 340], [341, 342], [341, 346]]}

import pytest
from ansible.playbook.helpers import load_list_of_roles
from ansible.errors import AnsibleAssertionError
from unittest.mock import Mock, patch

@pytest.fixture
def mock_role_include_load():
    with patch('ansible.playbook.role.include.RoleInclude.load') as mock_load:
        yield mock_load

def test_load_list_of_roles_with_non_list_ds():
    play = Mock()
    with pytest.raises(AnsibleAssertionError, match=r'ds \(.*\) should be a list but was a .*'):
        load_list_of_roles("not_a_list", play)

def test_load_list_of_roles_with_empty_list(mock_role_include_load):
    play = Mock()
    result = load_list_of_roles([], play)
    assert result == []
    mock_role_include_load.assert_not_called()

def test_load_list_of_roles_with_valid_list(mock_role_include_load):
    play = Mock()
    ds = [{'role': 'test_role'}]
    mock_role_include_load.return_value = 'mock_role_include'
    
    result = load_list_of_roles(ds, play)
    
    assert result == ['mock_role_include']
    mock_role_include_load.assert_called_once_with(ds[0], play=play, current_role_path=None, variable_manager=None, loader=None, collection_list=None)
