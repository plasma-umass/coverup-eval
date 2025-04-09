# file lib/ansible/playbook/helpers.py:323-346
# lines [323, 335, 337, 338, 340, 341, 342, 343, 344, 346]
# branches ['337->338', '337->340', '341->342', '341->346']

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.helpers import load_list_of_roles
from ansible.errors import AnsibleAssertionError

@pytest.fixture
def mock_role_include():
    with patch('ansible.playbook.role.include.RoleInclude') as mock:
        yield mock

def test_load_list_of_roles_invalid_ds():
    play = Mock()
    with pytest.raises(AnsibleAssertionError, match=r'ds \(.*\) should be a list but was a .*'):
        load_list_of_roles("not_a_list", play)

def test_load_list_of_roles_valid_ds(mock_role_include):
    play = Mock()
    ds = [{'name': 'test_role'}]
    current_role_path = '/path/to/role'
    variable_manager = Mock()
    loader = Mock()
    collection_search_list = ['collection1', 'collection2']

    mock_role_include.load.return_value = Mock()

    roles = load_list_of_roles(ds, play, current_role_path, variable_manager, loader, collection_search_list)

    assert len(roles) == 1
    mock_role_include.load.assert_called_once_with(
        ds[0],
        play=play,
        current_role_path=current_role_path,
        variable_manager=variable_manager,
        loader=loader,
        collection_list=collection_search_list
    )
