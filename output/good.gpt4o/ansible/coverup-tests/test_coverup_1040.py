# file lib/ansible/cli/doc.py:168-208
# lines [182, 183, 184, 185, 186, 188, 189, 190, 193, 194, 195, 196, 197, 200, 201, 202, 203, 204, 205, 206, 207, 208]
# branches ['184->185', '184->208', '189->184', '189->190', '190->184', '190->193', '193->190', '193->194', '195->193', '195->196', '196->197', '196->200', '200->201', '200->207', '201->202', '201->205', '203->200', '203->204', '205->200', '205->206']

import os
import pytest
from unittest.mock import patch, MagicMock

# Assuming the RoleMixin class is imported from ansible.cli.doc
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    class TestRoleMixin(RoleMixin):
        ROLE_ARGSPEC_FILES = ['argspec.yml', 'argspec.json']
    return TestRoleMixin()

@pytest.fixture
def mock_list_collection_dirs():
    with patch('ansible.cli.doc.list_collection_dirs') as mock:
        yield mock

@pytest.fixture
def mock_get_collection_name_from_path():
    with patch('ansible.cli.doc._get_collection_name_from_path') as mock:
        yield mock

@pytest.fixture
def mock_os_path_exists():
    with patch('os.path.exists') as mock:
        yield mock

@pytest.fixture
def mock_os_listdir():
    with patch('os.listdir') as mock:
        yield mock

def test_find_all_collection_roles(role_mixin, mock_list_collection_dirs, mock_get_collection_name_from_path, mock_os_path_exists, mock_os_listdir):
    # Setup the mocks
    mock_list_collection_dirs.return_value = ['/fake/path']
    mock_get_collection_name_from_path.return_value = 'fake_namespace.fake_collection'
    mock_os_path_exists.side_effect = lambda x: x in [
        '/fake/path/roles',
        '/fake/path/roles/roleA/meta/argspec.yml'
    ]
    mock_os_listdir.return_value = ['roleA']

    # Test without name_filters and collection_filter
    result = role_mixin._find_all_collection_roles()
    assert result == {('roleA', 'fake_namespace.fake_collection', '/fake/path')}

    # Test with name_filters
    result = role_mixin._find_all_collection_roles(name_filters=('roleA',))
    assert result == {('roleA', 'fake_namespace.fake_collection', '/fake/path')}

    # Test with fully qualified name_filters
    result = role_mixin._find_all_collection_roles(name_filters=('fake_namespace.fake_collection.roleA',))
    assert result == {('roleA', 'fake_namespace.fake_collection', '/fake/path')}

    # Test with collection_filter
    mock_list_collection_dirs.return_value = []
    result = role_mixin._find_all_collection_roles(collection_filter='fake_namespace.fake_collection')
    assert result == set()
