# file: lib/ansible/utils/collection_loader/_collection_finder.py:599-603
# asked: {"lines": [601], "branches": [[600, 601]]}
# gained: {"lines": [601], "branches": [[600, 601]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionLoader

class MockAnsibleCollectionPkgLoaderBase:
    def __init__(self, fullname, path_list=None):
        self._fullname = fullname
        self._split_name = fullname.split('.')

class TestAnsibleCollectionLoader:
    def test_get_candidate_paths_raises_value_error(self):
        loader = _AnsibleCollectionLoader.__new__(_AnsibleCollectionLoader)
        loader._split_name = ['some', 'other', 'name']
        path_list = ['path1', 'path2']
        
        with pytest.raises(ValueError, match='this loader requires exactly one path to search'):
            loader._get_candidate_paths(path_list)
