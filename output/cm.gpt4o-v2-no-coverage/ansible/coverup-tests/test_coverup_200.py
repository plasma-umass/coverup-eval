# file: lib/ansible/cli/doc.py:254-302
# asked: {"lines": [254, 284, 285, 287, 288, 290, 292, 293, 294, 295, 297, 298, 299, 300, 302], "branches": [[284, 285], [284, 287], [292, 293], [292, 297], [297, 298], [297, 302]]}
# gained: {"lines": [254, 284, 285, 287, 288, 290, 292, 293, 294, 295, 297, 298, 299, 300, 302], "branches": [[284, 285], [284, 287], [292, 293], [292, 297], [297, 298], [297, 302]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import RoleMixin

class TestRoleMixin:
    
    @patch.object(RoleMixin, '_find_all_normal_roles')
    @patch.object(RoleMixin, '_find_all_collection_roles')
    @patch.object(RoleMixin, '_load_argspec')
    @patch.object(RoleMixin, '_build_summary')
    def test_create_role_list_no_collection_filter(self, mock_build_summary, mock_load_argspec, mock_find_all_collection_roles, mock_find_all_normal_roles):
        # Setup
        role_mixin = RoleMixin()
        roles_path = ('/path/to/roles',)
        mock_find_all_normal_roles.return_value = [('roleA', '/path/to/roleA')]
        mock_find_all_collection_roles.return_value = []
        mock_load_argspec.return_value = {'main': {'short_description': 'Short description for main'}}
        mock_build_summary.return_value = ('roleA', {'collection': '', 'entry_points': {'main': 'Short description for main'}})
        
        # Execute
        result = role_mixin._create_role_list(roles_path)
        
        # Verify
        assert result == {
            'roleA': {
                'collection': '',
                'entry_points': {
                    'main': 'Short description for main'
                }
            }
        }
        mock_find_all_normal_roles.assert_called_once_with(roles_path)
        mock_find_all_collection_roles.assert_called_once_with(collection_filter=None)
        mock_load_argspec.assert_called_once_with('roleA', role_path='/path/to/roleA')
        mock_build_summary.assert_called_once_with('roleA', '', {'main': {'short_description': 'Short description for main'}})
    
    @patch.object(RoleMixin, '_find_all_normal_roles')
    @patch.object(RoleMixin, '_find_all_collection_roles')
    @patch.object(RoleMixin, '_load_argspec')
    @patch.object(RoleMixin, '_build_summary')
    def test_create_role_list_with_collection_filter(self, mock_build_summary, mock_load_argspec, mock_find_all_collection_roles, mock_find_all_normal_roles):
        # Setup
        role_mixin = RoleMixin()
        roles_path = ('/path/to/roles',)
        collection_filter = 'a.b.c'
        mock_find_all_normal_roles.return_value = []
        mock_find_all_collection_roles.return_value = [('roleB', 'a.b.c', '/path/to/collection/a.b.c')]
        mock_load_argspec.return_value = {'main': {'short_description': 'Short description for main'}}
        mock_build_summary.return_value = ('a.b.c.roleB', {'collection': 'a.b.c', 'entry_points': {'main': 'Short description for main'}})
        
        # Execute
        result = role_mixin._create_role_list(roles_path, collection_filter=collection_filter)
        
        # Verify
        assert result == {
            'a.b.c.roleB': {
                'collection': 'a.b.c',
                'entry_points': {
                    'main': 'Short description for main'
                }
            }
        }
        mock_find_all_normal_roles.assert_not_called()
        mock_find_all_collection_roles.assert_called_once_with(collection_filter=collection_filter)
        mock_load_argspec.assert_called_once_with('roleB', collection_path='/path/to/collection/a.b.c')
        mock_build_summary.assert_called_once_with('roleB', 'a.b.c', {'main': {'short_description': 'Short description for main'}})
