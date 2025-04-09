# file lib/ansible/utils/collection_loader/_collection_finder.py:599-603
# lines [599, 600, 601, 603]
# branches ['600->601', '600->603']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionLoader

def test_ansible_collection_loader_get_candidate_paths_single_path(mocker):
    mocker.patch.object(_AnsibleCollectionLoader, '__init__', return_value=None)
    loader = _AnsibleCollectionLoader()
    loader._split_name = ['namespace', 'collection', 'module']
    path_list = ['/path/to/collections']
    assert loader._get_candidate_paths(path_list) == path_list

def test_ansible_collection_loader_get_candidate_paths_multiple_paths(mocker):
    mocker.patch.object(_AnsibleCollectionLoader, '__init__', return_value=None)
    loader = _AnsibleCollectionLoader()
    loader._split_name = ['namespace', 'collection', 'module']
    path_list = ['/path/one', '/path/two']
    with pytest.raises(ValueError):
        loader._get_candidate_paths(path_list)

def test_ansible_collection_loader_get_candidate_paths_builtin(mocker):
    mocker.patch.object(_AnsibleCollectionLoader, '__init__', return_value=None)
    loader = _AnsibleCollectionLoader()
    loader._split_name = ['ansible', 'builtin', 'module']
    path_list = ['/path/to/collections']
    assert loader._get_candidate_paths(path_list) == path_list
