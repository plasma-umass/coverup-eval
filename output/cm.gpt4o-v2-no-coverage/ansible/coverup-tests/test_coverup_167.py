# file: lib/ansible/utils/collection_loader/_collection_finder.py:422-446
# asked: {"lines": [422, 423, 424, 429, 432, 434, 436, 437, 438, 439, 440, 443, 444, 446], "branches": [[423, 424], [423, 429], [429, 432], [429, 434], [436, 437], [436, 446], [438, 439], [438, 443], [443, 436], [443, 444]]}
# gained: {"lines": [422, 423, 424, 429, 432, 434, 436, 437, 438, 439, 440, 443, 444, 446], "branches": [[423, 424], [423, 429], [429, 432], [429, 434], [436, 437], [436, 446], [438, 439], [438, 443], [443, 436], [443, 444]]}

import pytest
import os
from unittest.mock import patch, mock_open
from ansible.module_utils.common.text.converters import to_bytes
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def loader():
    with patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_args', return_value=None), \
         patch.object(_AnsibleCollectionPkgLoaderBase, '_get_candidate_paths', return_value=[]), \
         patch.object(_AnsibleCollectionPkgLoaderBase, '_get_subpackage_search_paths', return_value=[]), \
         patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_final', return_value=None):
        return _AnsibleCollectionPkgLoaderBase('ansible_collections.dummy.fullname', path_list=['/dummy/path'])

def test_get_data_no_path(loader):
    with pytest.raises(ValueError, match='a path must be specified'):
        loader.get_data('')

def test_get_data_relative_path(loader):
    with pytest.raises(ValueError, match='relative resource paths not supported'):
        loader.get_data('relative/path')

def test_get_data_file_exists(loader, monkeypatch):
    path = '/absolute/path/to/file'
    b_path = to_bytes(path)
    
    monkeypatch.setattr(os.path, 'isfile', lambda x: x == b_path)
    monkeypatch.setattr('builtins.open', mock_open(read_data=b'data'))
    
    result = loader.get_data(path)
    assert result == b'data'

def test_get_data_init_py(loader, monkeypatch):
    path = '/absolute/path/to/__init__.py'
    b_path = to_bytes(path)
    
    monkeypatch.setattr(os.path, 'isfile', lambda x: False)
    monkeypatch.setattr(os.path, 'isdir', lambda x: x == os.path.dirname(b_path))
    
    result = loader.get_data(path)
    assert result == ''

def test_get_data_file_not_exists(loader, monkeypatch):
    path = '/absolute/path/to/nonexistent'
    b_path = to_bytes(path)
    
    monkeypatch.setattr(os.path, 'isfile', lambda x: False)
    monkeypatch.setattr(os.path, 'isdir', lambda x: False)
    
    result = loader.get_data(path)
    assert result is None
