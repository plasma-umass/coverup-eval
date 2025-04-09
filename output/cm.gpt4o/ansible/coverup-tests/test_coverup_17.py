# file lib/ansible/collections/list.py:50-102
# lines [50, 58, 59, 60, 61, 62, 63, 64, 65, 67, 69, 70, 72, 73, 75, 77, 79, 80, 82, 84, 85, 87, 89, 90, 92, 94, 97, 98, 99, 100, 101, 102]
# branches ['60->61', '60->69', '61->62', '61->67', '70->exit', '70->72', '72->73', '72->75', '77->70', '77->79', '79->80', '79->82', '84->70', '84->85', '87->84', '87->89', '89->90', '89->92', '94->84', '94->97', '97->94', '97->98', '100->94', '100->101']

import os
import pytest
from unittest.mock import patch, mock_open, MagicMock
from collections import defaultdict
from ansible.errors import AnsibleError

# Assuming the function is imported from the module
from ansible.collections.list import list_collection_dirs

@pytest.fixture
def mock_list_valid_collection_paths():
    with patch('ansible.collections.list.list_valid_collection_paths') as mock:
        yield mock

@pytest.fixture
def mock_os_path():
    with patch('os.path') as mock:
        yield mock

@pytest.fixture
def mock_os_listdir():
    with patch('os.listdir') as mock:
        yield mock

@pytest.fixture
def mock_is_collection_path():
    with patch('ansible.collections.list.is_collection_path') as mock:
        yield mock

def test_list_collection_dirs_with_coll_filter(mock_list_valid_collection_paths, mock_os_path, mock_os_listdir, mock_is_collection_path):
    # Setup the mocks
    mock_list_valid_collection_paths.return_value = ['/fake/path']
    mock_os_path.basename.return_value = 'ansible_collections'
    mock_os_path.exists.return_value = True
    mock_os_path.isdir.side_effect = lambda x: True
    mock_os_listdir.side_effect = lambda x: [b'namespace1'] if b'ansible_collections' in x else [b'collection1']
    mock_is_collection_path.return_value = True

    # Test with coll_filter containing a dot
    coll_filter = 'namespace1.collection1'
    result = list(list_collection_dirs(coll_filter=coll_filter))
    assert result == [os.path.join('/fake/path/ansible_collections', 'namespace1', 'collection1')]

    # Test with coll_filter not containing a dot
    coll_filter = 'namespace1'
    result = list(list_collection_dirs(coll_filter=coll_filter))
    assert result == [os.path.join('/fake/path/ansible_collections', 'namespace1', 'collection1')]

    # Test with invalid coll_filter
    coll_filter = 'invalid.pattern.too.many.dots'
    with pytest.raises(AnsibleError, match="Invalid collection pattern supplied: invalid.pattern.too.many.dots"):
        list(list_collection_dirs(coll_filter=coll_filter))

def test_list_collection_dirs_without_coll_filter(mock_list_valid_collection_paths, mock_os_path, mock_os_listdir, mock_is_collection_path):
    # Setup the mocks
    mock_list_valid_collection_paths.return_value = ['/fake/path']
    mock_os_path.basename.return_value = 'ansible_collections'
    mock_os_path.exists.return_value = True
    mock_os_path.isdir.side_effect = lambda x: True
    mock_os_listdir.side_effect = lambda x: [b'namespace1'] if b'ansible_collections' in x else [b'collection1']
    mock_is_collection_path.return_value = True

    # Test without coll_filter
    result = list(list_collection_dirs())
    assert result == [os.path.join('/fake/path/ansible_collections', 'namespace1', 'collection1')]
