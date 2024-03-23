# file lib/ansible/playbook/helpers.py:323-346
# lines [323, 335, 337, 338, 340, 341, 342, 343, 344, 346]
# branches ['337->338', '337->340', '341->342', '341->346']

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.playbook.helpers import load_list_of_roles

def test_load_list_of_roles_with_non_list_input(mocker):
    # Mock the RoleInclude to avoid circular dependency issues
    mocker.patch('ansible.playbook.role.include.RoleInclude')

    # Define the parameters for the test
    ds = "not_a_list"
    play = mocker.MagicMock()
    current_role_path = None
    variable_manager = None
    loader = None
    collection_search_list = None

    # Test that a non-list input raises the correct exception
    with pytest.raises(AnsibleAssertionError) as excinfo:
        load_list_of_roles(ds, play, current_role_path, variable_manager, loader, collection_search_list)
    
    # Check that the exception message is as expected
    assert str(excinfo.value) == 'ds (not_a_list) should be a list but was a <class \'str\'>'

def test_load_list_of_roles_with_list_input(mocker):
    # Mock the RoleInclude and its load method to avoid circular dependency issues
    role_include_mock = mocker.patch('ansible.playbook.role.include.RoleInclude')
    role_include_load_mock = role_include_mock.load
    role_include_load_mock.return_value = 'role_include_instance'

    # Define the parameters for the test
    ds = [{'role': 'test_role'}]
    play = mocker.MagicMock()
    current_role_path = None
    variable_manager = None
    loader = None
    collection_search_list = None

    # Call the function with a list input
    roles = load_list_of_roles(ds, play, current_role_path, variable_manager, loader, collection_search_list)

    # Check that the load method was called correctly
    role_include_load_mock.assert_called_once_with(
        {'role': 'test_role'},
        play=play,
        current_role_path=current_role_path,
        variable_manager=variable_manager,
        loader=loader,
        collection_list=collection_search_list
    )

    # Check that the returned list contains the correct RoleInclude instances
    assert roles == ['role_include_instance']
