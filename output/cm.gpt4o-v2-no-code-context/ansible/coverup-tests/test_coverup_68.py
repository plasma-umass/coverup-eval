# file: lib/ansible/utils/collection_loader/_collection_finder.py:77-108
# asked: {"lines": [77, 79, 81, 82, 83, 84, 87, 90, 91, 93, 95, 98, 99, 101, 102, 104, 105, 106, 108], "branches": [[81, 82], [81, 83], [83, 84], [83, 87], [90, 91], [90, 93], [95, 98], [95, 104], [98, 99], [98, 101], [101, 95], [101, 102]]}
# gained: {"lines": [77, 79, 81, 82, 83, 84, 87, 90, 91, 93, 95, 98, 99, 101, 102, 104, 105, 106, 108], "branches": [[81, 82], [81, 83], [83, 84], [83, 87], [90, 91], [90, 93], [95, 98], [95, 104], [98, 99], [98, 101], [101, 102]]}

import os
import sys
import pytest
from unittest.mock import patch, MagicMock

# Assuming the class _AnsibleCollectionFinder is imported from the module
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

@pytest.fixture
def mock_sys_modules():
    with patch.dict('sys.modules', {'ansible': MagicMock(__file__='/fake/path/to/ansible/__init__.py')}):
        yield

@pytest.fixture
def mock_os_path():
    with patch('os.path.isdir', return_value=True) as mock_isdir:
        with patch('os.path.expanduser', side_effect=lambda x: x):
            with patch('os.path.basename', side_effect=os.path.basename):
                with patch('os.path.dirname', side_effect=os.path.dirname):
                    yield mock_isdir

def test_ansible_collection_finder_with_paths(mock_sys_modules, mock_os_path):
    paths = ['/fake/path/to/ansible_collections']
    finder = _AnsibleCollectionFinder(paths=paths, scan_sys_paths=False)
    
    assert finder._n_configured_paths == ['/fake/path/to']
    assert finder._n_cached_collection_paths is None
    assert finder._n_cached_collection_qualified_paths is None
    assert finder._n_playbook_paths == []

def test_ansible_collection_finder_with_string_path(mock_sys_modules, mock_os_path):
    paths = '/fake/path/to/ansible_collections'
    finder = _AnsibleCollectionFinder(paths=paths, scan_sys_paths=False)
    
    assert finder._n_configured_paths == ['/fake/path/to']
    assert finder._n_cached_collection_paths is None
    assert finder._n_cached_collection_qualified_paths is None
    assert finder._n_playbook_paths == []

def test_ansible_collection_finder_with_no_paths(mock_sys_modules, mock_os_path):
    finder = _AnsibleCollectionFinder(paths=None, scan_sys_paths=False)
    
    assert finder._n_configured_paths == []
    assert finder._n_cached_collection_paths is None
    assert finder._n_cached_collection_qualified_paths is None
    assert finder._n_playbook_paths == []

def test_ansible_collection_finder_with_sys_paths(mock_sys_modules, mock_os_path):
    with patch('sys.path', new=['/fake/sys/path']):
        finder = _AnsibleCollectionFinder(paths=None, scan_sys_paths=True)
        
        assert '/fake/sys/path' in finder._n_configured_paths
        assert finder._n_cached_collection_paths is None
        assert finder._n_cached_collection_qualified_paths is None
        assert finder._n_playbook_paths == []
