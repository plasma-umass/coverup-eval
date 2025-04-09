# file: lib/ansible/utils/collection_loader/_collection_finder.py:524-532
# asked: {"lines": [528, 529, 532], "branches": [[525, 528], [528, 529], [528, 532]]}
# gained: {"lines": [528, 529, 532], "branches": [[525, 528], [528, 529], [528, 532]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoader
from unittest.mock import MagicMock

@pytest.fixture
def mock_loader():
    loader = _AnsibleCollectionPkgLoader.__new__(_AnsibleCollectionPkgLoader)
    loader._split_name = ['some', 'collection', 'name']
    loader._package_to_load = 'test_package'
    loader._candidate_paths = ['path1', 'path2']
    loader._subpackage_search_paths = ['search_path1', 'search_path2']
    return loader

def test_validate_final_builtin(mock_loader):
    mock_loader._split_name = ['some', 'ansible', 'builtin']
    mock_loader._validate_final()
    assert mock_loader._subpackage_search_paths == []

def test_validate_final_no_subpackage_search_paths(mock_loader):
    mock_loader._subpackage_search_paths = []
    with pytest.raises(ImportError, match='no test_package found in .*'):
        mock_loader._validate_final()

def test_validate_final_with_subpackage_search_paths(mock_loader):
    mock_loader._validate_final()
    assert mock_loader._subpackage_search_paths == ['search_path1']
