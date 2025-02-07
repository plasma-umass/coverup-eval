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
    with patch.dict('sys.modules', {'ansible': MagicMock(__file__='/fake/path/to/ansible/__init__.py')}):
        yield

@pytest.fixture
def mock_sys_path():
    original_sys_path = sys.path
    sys.path = ['/fake/path1', '/fake/path2']
    yield
    sys.path = original_sys_path

@pytest.fixture
def mock_os_path_isdir():
    with patch('os.path.isdir') as mock_isdir:
        mock_isdir.side_effect = lambda x: x in [
            to_bytes('/fake/path1/ansible_collections', errors='surrogate_or_strict'),
            to_bytes('/fake/path2/ansible_collections', errors='surrogate_or_strict')
        ]
        yield mock_isdir

def test_ansible_collection_finder_paths_string(mock_sys_modules, mock_sys_path, mock_os_path_isdir):
    finder = _AnsibleCollectionFinder(paths='/fake/path1', scan_sys_paths=False)
    assert finder._n_configured_paths == ['/fake/path1']

def test_ansible_collection_finder_paths_none(mock_sys_modules, mock_sys_path, mock_os_path_isdir):
    finder = _AnsibleCollectionFinder(paths=None, scan_sys_paths=False)
    assert finder._n_configured_paths == []

def test_ansible_collection_finder_scan_sys_paths(mock_sys_modules, mock_sys_path, mock_os_path_isdir):
    finder = _AnsibleCollectionFinder(paths=None, scan_sys_paths=True)
    assert set(finder._n_configured_paths) == {'/fake/path1', '/fake/path2'}

def test_ansible_collection_finder_ansible_collections(mock_sys_modules, mock_sys_path, mock_os_path_isdir):
    finder = _AnsibleCollectionFinder(paths='/fake/path1/ansible_collections', scan_sys_paths=False)
    assert finder._n_configured_paths == ['/fake/path1']
