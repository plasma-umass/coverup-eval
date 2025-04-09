# file: lib/ansible/cli/doc.py:168-208
# asked: {"lines": [182, 183, 184, 185, 186, 188, 189, 190, 193, 194, 195, 196, 197, 200, 201, 202, 203, 204, 205, 206, 207, 208], "branches": [[184, 185], [184, 208], [189, 184], [189, 190], [190, 184], [190, 193], [193, 190], [193, 194], [195, 193], [195, 196], [196, 197], [196, 200], [200, 201], [200, 207], [201, 202], [201, 205], [203, 200], [203, 204], [205, 200], [205, 206]]}
# gained: {"lines": [182, 183, 184, 185, 186, 188, 189, 190, 193, 194, 195, 196, 197, 200, 201, 202, 203, 204, 207, 208], "branches": [[184, 185], [184, 208], [189, 190], [190, 184], [190, 193], [193, 194], [195, 196], [196, 197], [196, 200], [200, 201], [200, 207], [201, 202], [203, 204]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    class TestRoleMixin(RoleMixin):
        ROLE_ARGSPEC_FILES = ['argspec.yml', 'argspec.json']
    return TestRoleMixin()

@patch('ansible.cli.doc.list_collection_dirs')
@patch('ansible.cli.doc.to_text')
@patch('ansible.cli.doc._get_collection_name_from_path')
@patch('os.path.exists')
@patch('os.listdir')
def test_find_all_collection_roles_no_filters(mock_listdir, mock_exists, mock_get_collection_name, mock_to_text, mock_list_collection_dirs, role_mixin):
    mock_list_collection_dirs.return_value = ['/fake/path']
    mock_to_text.return_value = '/fake/path'
    mock_get_collection_name.return_value = 'fake_namespace.fake_collection'
    mock_exists.side_effect = lambda x: x.endswith('roles') or x.endswith('argspec.yml')
    mock_listdir.return_value = ['roleA']

    result = role_mixin._find_all_collection_roles()

    assert result == {('roleA', 'fake_namespace.fake_collection', '/fake/path')}

@patch('ansible.cli.doc.list_collection_dirs')
@patch('ansible.cli.doc.to_text')
@patch('ansible.cli.doc._get_collection_name_from_path')
@patch('os.path.exists')
@patch('os.listdir')
def test_find_all_collection_roles_with_name_filters(mock_listdir, mock_exists, mock_get_collection_name, mock_to_text, mock_list_collection_dirs, role_mixin):
    mock_list_collection_dirs.return_value = ['/fake/path']
    mock_to_text.return_value = '/fake/path'
    mock_get_collection_name.return_value = 'fake_namespace.fake_collection'
    mock_exists.side_effect = lambda x: x.endswith('roles') or x.endswith('argspec.yml')
    mock_listdir.return_value = ['roleA']

    result = role_mixin._find_all_collection_roles(name_filters=('fake_namespace.fake_collection.roleA',))

    assert result == {('roleA', 'fake_namespace.fake_collection', '/fake/path')}

@patch('ansible.cli.doc.list_collection_dirs')
@patch('ansible.cli.doc.to_text')
@patch('ansible.cli.doc._get_collection_name_from_path')
@patch('os.path.exists')
@patch('os.listdir')
def test_find_all_collection_roles_with_collection_filter(mock_listdir, mock_exists, mock_get_collection_name, mock_to_text, mock_list_collection_dirs, role_mixin):
    mock_list_collection_dirs.return_value = ['/fake/path']
    mock_to_text.return_value = '/fake/path'
    mock_get_collection_name.return_value = 'fake_namespace.fake_collection'
    mock_exists.side_effect = lambda x: x.endswith('roles') or x.endswith('argspec.yml')
    mock_listdir.return_value = ['roleA']

    result = role_mixin._find_all_collection_roles(collection_filter='fake_namespace.fake_collection')

    assert result == {('roleA', 'fake_namespace.fake_collection', '/fake/path')}
