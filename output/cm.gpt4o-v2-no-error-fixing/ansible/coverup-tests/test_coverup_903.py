# file: lib/ansible/cli/doc.py:134-166
# asked: {"lines": [150], "branches": [[149, 150], [157, 153], [159, 157]]}
# gained: {"lines": [150], "branches": [[149, 150], [157, 153], [159, 157]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    return RoleMixin()

def test_find_all_normal_roles_no_dirs(role_mixin):
    with patch('os.path.isdir', return_value=False) as mock_isdir:
        result = role_mixin._find_all_normal_roles(('path1', 'path2'))
        assert result == set()
        mock_isdir.assert_called()

def test_find_all_normal_roles_with_dirs(role_mixin):
    with patch('os.path.isdir', return_value=True) as mock_isdir, \
         patch('os.listdir', return_value=['role1', 'role2']) as mock_listdir, \
         patch('os.path.exists', side_effect=[False, True, False, False]) as mock_exists:
        
        role_mixin.ROLE_ARGSPEC_FILES = ['argspec1', 'argspec2']
        result = role_mixin._find_all_normal_roles(('path1',))
        
        assert result == {('role1', 'path1/role1')}
        mock_isdir.assert_called()
        mock_listdir.assert_called()
        mock_exists.assert_called()

def test_find_all_normal_roles_with_name_filters(role_mixin):
    with patch('os.path.isdir', return_value=True) as mock_isdir, \
         patch('os.listdir', return_value=['role1', 'role2']) as mock_listdir, \
         patch('os.path.exists', side_effect=[True, False, False, False]) as mock_exists:
        
        role_mixin.ROLE_ARGSPEC_FILES = ['argspec1', 'argspec2']
        result = role_mixin._find_all_normal_roles(('path1',), name_filters=('role1',))
        
        assert result == {('role1', 'path1/role1')}
        mock_isdir.assert_called()
        mock_listdir.assert_called()
        mock_exists.assert_called()
