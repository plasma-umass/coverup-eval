# file lib/ansible/cli/doc.py:254-302
# lines [284, 285, 287, 288, 290, 292, 293, 294, 295, 297, 298, 299, 300, 302]
# branches ['284->285', '284->287', '292->293', '292->297', '297->298', '297->302']

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
def mock_build_summary(mocker):
    return mocker.patch.object(RoleMixin, '_build_summary', return_value=('fqcn', {'collection': '', 'entry_points': {}}))

def test_create_role_list_without_collection_filter(role_mixin, mock_find_all_normal_roles, mock_find_all_collection_roles, mock_load_argspec, mock_build_summary):
    roles_path = ('/path/to/roles',)
    result = role_mixin._create_role_list(roles_path)
    assert isinstance(result, dict)
    mock_find_all_normal_roles.assert_called_once_with(roles_path)
    mock_find_all_collection_roles.assert_called_once_with(collection_filter=None)
    mock_load_argspec.assert_not_called()
    mock_build_summary.assert_not_called()

def test_create_role_list_with_collection_filter(role_mixin, mock_find_all_normal_roles, mock_find_all_collection_roles, mock_load_argspec, mock_build_summary):
    roles_path = ('/path/to/roles',)
    collection_filter = 'some.collection'
    result = role_mixin._create_role_list(roles_path, collection_filter=collection_filter)
    assert isinstance(result, dict)
    mock_find_all_normal_roles.assert_not_called()
    mock_find_all_collection_roles.assert_called_once_with(collection_filter=collection_filter)
    mock_load_argspec.assert_not_called()
    mock_build_summary.assert_not_called()
