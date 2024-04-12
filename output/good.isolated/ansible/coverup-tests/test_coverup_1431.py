# file lib/ansible/cli/doc.py:304-329
# lines []
# branches ['320->317', '326->323']

import pytest
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    return RoleMixin()

@pytest.fixture
def mock_find_all_normal_roles(mocker):
    return mocker.patch.object(RoleMixin, '_find_all_normal_roles', return_value=[])

@pytest.fixture
def mock_find_all_collection_roles(mocker):
    return mocker.patch.object(RoleMixin, '_find_all_collection_roles', return_value=[])

@pytest.fixture
def mock_load_argspec(mocker):
    return mocker.patch.object(RoleMixin, '_load_argspec', return_value={})

@pytest.fixture
def mock_build_doc(mocker):
    return mocker.patch.object(RoleMixin, '_build_doc', side_effect=lambda *args, **kwargs: (args[0], None))

def test_create_role_doc_no_doc_returned(role_mixin, mock_find_all_normal_roles, mock_find_all_collection_roles, mock_load_argspec, mock_build_doc):
    role_names = ('role1', 'role2')
    roles_path = ('path1', 'path2')
    entry_point = 'main'

    # Mocking the return values to simulate the condition where no doc is returned
    mock_find_all_normal_roles.return_value = [('role1', 'path1')]
    mock_find_all_collection_roles.return_value = [('role2', 'collection', 'path2')]

    result = role_mixin._create_role_doc(role_names, roles_path, entry_point)

    # Assertions to ensure that the branches 320->317 and 326->323 are executed
    # and that the result is empty as no doc is returned
    assert result == {}
    mock_find_all_normal_roles.assert_called_once_with(roles_path, name_filters=role_names)
    mock_find_all_collection_roles.assert_called_once_with(name_filters=role_names)
    mock_load_argspec.assert_any_call('role1', role_path='path1')
    mock_load_argspec.assert_any_call('role2', collection_path='path2')
    mock_build_doc.assert_any_call('role1', 'path1', '', {}, entry_point)
    mock_build_doc.assert_any_call('role2', 'path2', 'collection', {}, entry_point)
