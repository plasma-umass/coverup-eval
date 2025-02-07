# file: lib/ansible/cli/doc.py:304-329
# asked: {"lines": [312, 313, 315, 317, 318, 319, 320, 321, 323, 324, 325, 326, 327, 329], "branches": [[317, 318], [317, 323], [320, 317], [320, 321], [323, 324], [323, 329], [326, 323], [326, 327]]}
# gained: {"lines": [312, 313, 315, 317, 318, 319, 320, 321, 323, 324, 325, 326, 327, 329], "branches": [[317, 318], [317, 323], [320, 321], [323, 324], [323, 329], [326, 327]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import RoleMixin

class TestRoleMixin:
    
    @patch('ansible.cli.doc.RoleMixin._find_all_normal_roles')
    @patch('ansible.cli.doc.RoleMixin._find_all_collection_roles')
    @patch('ansible.cli.doc.RoleMixin._load_argspec')
    @patch('ansible.cli.doc.RoleMixin._build_doc')
    def test_create_role_doc(self, mock_build_doc, mock_load_argspec, mock_find_all_collection_roles, mock_find_all_normal_roles):
        role_mixin = RoleMixin()
        
        # Mock the return values
        mock_find_all_normal_roles.return_value = [('role1', '/path/to/role1')]
        mock_find_all_collection_roles.return_value = [('role2', 'collection1', '/path/to/collection1')]
        mock_load_argspec.side_effect = [
            {'entry1': {'key': 'value'}},  # For normal role
            {'entry2': {'key': 'value'}}   # For collection role
        ]
        mock_build_doc.side_effect = [
            ('role1', {'path': '/path/to/role1', 'collection': '', 'entry_points': {'entry1': {'key': 'value'}}}),
            ('collection1.role2', {'path': '/path/to/collection1', 'collection': 'collection1', 'entry_points': {'entry2': {'key': 'value'}}})
        ]
        
        result = role_mixin._create_role_doc(('role1', 'role2'), ('/roles/path1', '/roles/path2'), entry_point=None)
        
        # Assertions
        assert 'role1' in result
        assert result['role1']['path'] == '/path/to/role1'
        assert result['role1']['entry_points']['entry1'] == {'key': 'value'}
        
        assert 'collection1.role2' in result
        assert result['collection1.role2']['path'] == '/path/to/collection1'
        assert result['collection1.role2']['entry_points']['entry2'] == {'key': 'value'}
        
        # Ensure the mocks were called as expected
        mock_find_all_normal_roles.assert_called_once_with(('/roles/path1', '/roles/path2'), name_filters=('role1', 'role2'))
        mock_find_all_collection_roles.assert_called_once_with(name_filters=('role1', 'role2'))
        mock_load_argspec.assert_any_call('role1', role_path='/path/to/role1')
        mock_load_argspec.assert_any_call('role2', collection_path='/path/to/collection1')
        mock_build_doc.assert_any_call('role1', '/path/to/role1', '', {'entry1': {'key': 'value'}}, None)
        mock_build_doc.assert_any_call('role2', '/path/to/collection1', 'collection1', {'entry2': {'key': 'value'}}, None)
