# file: lib/ansible/cli/doc.py:134-166
# asked: {"lines": [134, 145, 146, 148, 149, 150, 153, 154, 157, 158, 159, 160, 161, 162, 163, 165, 166], "branches": [[148, 149], [148, 166], [149, 150], [149, 153], [153, 148], [153, 154], [157, 153], [157, 158], [159, 157], [159, 160], [160, 161], [160, 165], [161, 162], [161, 163]]}
# gained: {"lines": [134, 145, 146, 148, 149, 150, 153, 154, 157, 158, 159, 160, 161, 162, 163, 165, 166], "branches": [[148, 149], [148, 166], [149, 150], [149, 153], [153, 148], [153, 154], [157, 158], [159, 160], [160, 161], [160, 165], [161, 162]]}

import os
import pytest
from unittest.mock import patch, mock_open
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    return RoleMixin()

@pytest.fixture
def mock_os_functions(monkeypatch):
    mock_isdir = patch('os.path.isdir').start()
    mock_listdir = patch('os.listdir').start()
    mock_exists = patch('os.path.exists').start()
    yield mock_isdir, mock_listdir, mock_exists
    patch.stopall()

def test_find_all_normal_roles_no_roles(role_mixin, mock_os_functions):
    mock_isdir, mock_listdir, mock_exists = mock_os_functions
    mock_isdir.return_value = False

    result = role_mixin._find_all_normal_roles(('path1', 'path2'))
    assert result == set()

def test_find_all_normal_roles_with_roles(role_mixin, mock_os_functions):
    mock_isdir, mock_listdir, mock_exists = mock_os_functions
    mock_isdir.return_value = True
    mock_listdir.return_value = ['role1', 'role2']
    mock_exists.side_effect = lambda path: 'argument_specs.yml' in path

    role_mixin.ROLE_ARGSPEC_FILES = ['argument_specs.yml']

    result = role_mixin._find_all_normal_roles(('path1',))
    assert result == {('role1', os.path.join('path1', 'role1')), ('role2', os.path.join('path1', 'role2'))}

def test_find_all_normal_roles_with_name_filters(role_mixin, mock_os_functions):
    mock_isdir, mock_listdir, mock_exists = mock_os_functions
    mock_isdir.return_value = True
    mock_listdir.return_value = ['role1', 'role2']
    mock_exists.side_effect = lambda path: 'argument_specs.yml' in path

    role_mixin.ROLE_ARGSPEC_FILES = ['argument_specs.yml']

    result = role_mixin._find_all_normal_roles(('path1',), name_filters=('role1',))
    assert result == {('role1', os.path.join('path1', 'role1'))}

def test_find_all_normal_roles_with_multiple_paths(role_mixin, mock_os_functions):
    mock_isdir, mock_listdir, mock_exists = mock_os_functions
    mock_isdir.side_effect = lambda path: path in ['path1', 'path2']
    mock_listdir.side_effect = lambda path: ['role1'] if path == 'path1' else ['role2']
    mock_exists.side_effect = lambda path: 'argument_specs.yml' in path

    role_mixin.ROLE_ARGSPEC_FILES = ['argument_specs.yml']

    result = role_mixin._find_all_normal_roles(('path1', 'path2'))
    assert result == {('role1', os.path.join('path1', 'role1')), ('role2', os.path.join('path2', 'role2'))}
