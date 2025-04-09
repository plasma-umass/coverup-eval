# file: lib/ansible/cli/doc.py:134-166
# asked: {"lines": [134, 145, 146, 148, 149, 150, 153, 154, 157, 158, 159, 160, 161, 162, 163, 165, 166], "branches": [[148, 149], [148, 166], [149, 150], [149, 153], [153, 148], [153, 154], [157, 153], [157, 158], [159, 157], [159, 160], [160, 161], [160, 165], [161, 162], [161, 163]]}
# gained: {"lines": [134, 145, 146, 148, 149, 153, 154, 157, 158, 159, 160, 161, 162, 163, 165, 166], "branches": [[148, 149], [148, 166], [149, 153], [153, 148], [153, 154], [157, 158], [159, 160], [160, 161], [160, 165], [161, 162], [161, 163]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    return RoleMixin()

@pytest.fixture
def mock_os_path_isdir(monkeypatch):
    with patch('os.path.isdir') as mock_isdir:
        yield mock_isdir

@pytest.fixture
def mock_os_listdir(monkeypatch):
    with patch('os.listdir') as mock_listdir:
        yield mock_listdir

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    with patch('os.path.exists') as mock_exists:
        yield mock_exists

def test_find_all_normal_roles(role_mixin, mock_os_path_isdir, mock_os_listdir, mock_os_path_exists):
    role_mixin.ROLE_ARGSPEC_FILES = ['main.yml', 'argument_specs.yml']

    # Mock the os.path.isdir to return True
    mock_os_path_isdir.side_effect = lambda path: True

    # Mock the os.listdir to return a list of directories
    mock_os_listdir.side_effect = lambda path: ['role1', 'role2']

    # Mock the os.path.exists to return True for specific paths
    def mock_exists_side_effect(path):
        if 'meta/main.yml' in path or 'meta/argument_specs.yml' in path:
            return True
        return False

    mock_os_path_exists.side_effect = mock_exists_side_effect

    role_paths = ('/fake/path1', '/fake/path2')
    name_filters = None

    result = role_mixin._find_all_normal_roles(role_paths, name_filters)

    expected = {('role1', '/fake/path1/role1'), ('role2', '/fake/path1/role2')}
    assert result == expected

def test_find_all_normal_roles_with_name_filters(role_mixin, mock_os_path_isdir, mock_os_listdir, mock_os_path_exists):
    role_mixin.ROLE_ARGSPEC_FILES = ['main.yml', 'argument_specs.yml']

    # Mock the os.path.isdir to return True
    mock_os_path_isdir.side_effect = lambda path: True

    # Mock the os.listdir to return a list of directories
    mock_os_listdir.side_effect = lambda path: ['role1', 'role2']

    # Mock the os.path.exists to return True for specific paths
    def mock_exists_side_effect(path):
        if 'meta/main.yml' in path or 'meta/argument_specs.yml' in path:
            return True
        return False

    mock_os_path_exists.side_effect = mock_exists_side_effect

    role_paths = ('/fake/path1', '/fake/path2')
    name_filters = ('role1',)

    result = role_mixin._find_all_normal_roles(role_paths, name_filters)

    expected = {('role1', '/fake/path1/role1')}
    assert result == expected
