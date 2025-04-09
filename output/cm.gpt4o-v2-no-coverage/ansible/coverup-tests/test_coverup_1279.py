# file: lib/ansible/utils/collection_loader/_collection_finder.py:77-108
# asked: {"lines": [82, 99, 102], "branches": [[81, 82], [98, 99], [101, 102]]}
# gained: {"lines": [82, 99, 102], "branches": [[81, 82], [98, 99], [101, 102]]}

import os
import sys
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.common.text.converters import to_native, to_bytes
from ansible.module_utils.six import string_types
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

@pytest.fixture
def mock_sys_modules():
    with patch.dict('sys.modules', {'ansible': MagicMock(__file__='/fake/path/ansible/__init__.py')}):
        yield

@pytest.fixture
def mock_sys_path():
    original_sys_path = sys.path
    sys.path = ['/fake/path1', '/fake/path2']
    yield
    sys.path = original_sys_path

@pytest.fixture
def mock_os_path_isdir():
    with patch('os.path.isdir', return_value=True) as mock_isdir:
        yield mock_isdir

@pytest.fixture
def mock_os_path_expanduser():
    with patch('os.path.expanduser', side_effect=lambda x: x):
        yield

def test_ansible_collection_finder_init_with_no_paths(mock_sys_modules, mock_sys_path, mock_os_path_isdir, mock_os_path_expanduser):
    finder = _AnsibleCollectionFinder()
    assert finder._n_configured_paths == ['/fake/path1', '/fake/path2']
    assert finder._n_cached_collection_paths is None
    assert finder._n_cached_collection_qualified_paths is None
    assert finder._n_playbook_paths == []

def test_ansible_collection_finder_init_with_paths(mock_sys_modules, mock_os_path_isdir, mock_os_path_expanduser):
    paths = ['/custom/path/ansible_collections']
    finder = _AnsibleCollectionFinder(paths=paths, scan_sys_paths=False)
    assert finder._n_configured_paths == ['/custom/path']
    assert finder._n_cached_collection_paths is None
    assert finder._n_cached_collection_qualified_paths is None
    assert finder._n_playbook_paths == []

def test_ansible_collection_finder_init_with_string_path(mock_sys_modules, mock_os_path_isdir, mock_os_path_expanduser):
    path = '/custom/path/ansible_collections'
    finder = _AnsibleCollectionFinder(paths=path, scan_sys_paths=False)
    assert finder._n_configured_paths == ['/custom/path']
    assert finder._n_cached_collection_paths is None
    assert finder._n_cached_collection_qualified_paths is None
    assert finder._n_playbook_paths == []

def test_ansible_collection_finder_init_with_scan_sys_paths(mock_sys_modules, mock_sys_path, mock_os_path_isdir, mock_os_path_expanduser):
    paths = ['/custom/path/ansible_collections']
    finder = _AnsibleCollectionFinder(paths=paths, scan_sys_paths=True)
    assert finder._n_configured_paths == ['/custom/path', '/fake/path1', '/fake/path2']
    assert finder._n_cached_collection_paths is None
    assert finder._n_cached_collection_qualified_paths is None
    assert finder._n_playbook_paths == []
