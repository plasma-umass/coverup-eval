# file lib/ansible/cli/doc.py:304-329
# lines [304, 312, 313, 315, 317, 318, 319, 320, 321, 323, 324, 325, 326, 327, 329]
# branches ['317->318', '317->323', '320->317', '320->321', '323->324', '323->329', '326->323', '326->327']

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
    return mocker.patch.object(RoleMixin, '_build_doc', return_value=('fqcn', {'doc': 'content'}))

def test_create_role_doc_no_roles(role_mixin, mock_find_all_normal_roles, mock_find_all_collection_roles, mock_load_argspec, mock_build_doc):
    role_names = ('role1', 'role2')
    roles_path = ('path1', 'path2')
    entry_point = 'main'

    result = role_mixin._create_role_doc(role_names, roles_path, entry_point)

    assert isinstance(result, dict)
    assert len(result) == 0
    mock_find_all_normal_roles.assert_called_once_with(roles_path, name_filters=role_names)
    mock_find_all_collection_roles.assert_called_once_with(name_filters=role_names)
    mock_load_argspec.assert_not_called()
    mock_build_doc.assert_not_called()

def test_create_role_doc_with_roles(role_mixin, mocker):
    mocker.patch.object(RoleMixin, '_find_all_normal_roles', return_value=[('role1', 'path1')])
    mocker.patch.object(RoleMixin, '_find_all_collection_roles', return_value=[('role2', 'collection', 'collection_path')])
    mocker.patch.object(RoleMixin, '_load_argspec', return_value={})
    mocker.patch.object(RoleMixin, '_build_doc', side_effect=[('fqcn1', {'doc': 'content1'}), ('fqcn2', {'doc': 'content2'})])

    role_names = ('role1', 'role2')
    roles_path = ('path1', 'path2')
    entry_point = 'main'

    result = role_mixin._create_role_doc(role_names, roles_path, entry_point)

    assert isinstance(result, dict)
    assert len(result) == 2
    assert 'fqcn1' in result
    assert 'fqcn2' in result
    assert result['fqcn1'] == {'doc': 'content1'}
    assert result['fqcn2'] == {'doc': 'content2'}
