# file lib/ansible/utils/collection_loader/_collection_finder.py:599-603
# lines [599, 600, 601, 603]
# branches ['600->601', '600->603']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionLoader

class MockAnsibleCollectionPkgLoaderBase:
    def __init__(self, split_name):
        self._split_name = split_name

class TestAnsibleCollectionLoader:
    def test_get_candidate_paths_raises_value_error(self):
        loader = _AnsibleCollectionLoader.__new__(_AnsibleCollectionLoader)
        loader._split_name = ['some', 'other', 'collection']
        path_list = ['path1', 'path2']
        
        with pytest.raises(ValueError, match='this loader requires exactly one path to search'):
            loader._get_candidate_paths(path_list)
    
    def test_get_candidate_paths_returns_path_list(self):
        loader = _AnsibleCollectionLoader.__new__(_AnsibleCollectionLoader)
        loader._split_name = ['some', 'ansible', 'builtin']
        path_list = ['path1']
        
        result = loader._get_candidate_paths(path_list)
        
        assert result == path_list
