# file: lib/ansible/cli/doc.py:168-208
# asked: {"lines": [205, 206], "branches": [[189, 184], [193, 190], [195, 193], [201, 205], [203, 200], [205, 200], [205, 206]]}
# gained: {"lines": [205, 206], "branches": [[195, 193], [201, 205], [203, 200], [205, 200], [205, 206]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    class TestRoleMixin(RoleMixin):
        ROLE_ARGSPEC_FILES = ['main.yml', 'argspec.yml']
    return TestRoleMixin()

@patch('ansible.cli.doc.list_collection_dirs')
@patch('ansible.cli.doc._get_collection_name_from_path')
@patch('os.path.exists')
@patch('os.listdir')
def test_find_all_collection_roles_full_coverage(mock_listdir, mock_exists, mock_get_collection_name, mock_list_collection_dirs, role_mixin):
    # Setup the mocks
    mock_list_collection_dirs.return_value = ['/fake/path/ansible_collections/namespace/collection']
    mock_get_collection_name.return_value = 'namespace.collection'
    mock_exists.side_effect = lambda x: x in [
        '/fake/path/ansible_collections/namespace/collection/roles',
        '/fake/path/ansible_collections/namespace/collection/roles/roleA/meta/main.yml',
        '/fake/path/ansible_collections/namespace/collection/roles/roleB/meta/argspec.yml'
    ]
    mock_listdir.side_effect = lambda x: {
        '/fake/path/ansible_collections/namespace/collection/roles': ['roleA', 'roleB']
    }[x]

    # Test without name_filters
    result = role_mixin._find_all_collection_roles()
    assert result == {('roleA', 'namespace.collection', '/fake/path/ansible_collections/namespace/collection'),
                      ('roleB', 'namespace.collection', '/fake/path/ansible_collections/namespace/collection')}

    # Test with name_filters containing FQCN
    result = role_mixin._find_all_collection_roles(name_filters=('namespace.collection.roleA',))
    assert result == {('roleA', 'namespace.collection', '/fake/path/ansible_collections/namespace/collection')}

    # Test with name_filters not containing FQCN
    result = role_mixin._find_all_collection_roles(name_filters=('roleB',))
    assert result == {('roleB', 'namespace.collection', '/fake/path/ansible_collections/namespace/collection')}

    # Test with collection_filter
    result = role_mixin._find_all_collection_roles(collection_filter='namespace.collection')
    assert result == {('roleA', 'namespace.collection', '/fake/path/ansible_collections/namespace/collection'),
                      ('roleB', 'namespace.collection', '/fake/path/ansible_collections/namespace/collection')}
