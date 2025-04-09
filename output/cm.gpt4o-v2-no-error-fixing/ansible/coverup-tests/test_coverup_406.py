# file: lib/ansible/utils/collection_loader/_collection_finder.py:599-603
# asked: {"lines": [599, 600, 601, 603], "branches": [[600, 601], [600, 603]]}
# gained: {"lines": [599, 600, 601, 603], "branches": [[600, 601], [600, 603]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionLoader

class MockAnsibleCollectionLoader(_AnsibleCollectionLoader):
    def __init__(self, fullname, path_list=None):
        self._fullname = fullname
        self._split_name = fullname.split('.')
        self._validate_args()

    def _validate_args(self):
        pass

def test_get_candidate_paths_single_path():
    loader = MockAnsibleCollectionLoader('some.module.name')
    path_list = ['/some/path']
    result = loader._get_candidate_paths(path_list)
    assert result == path_list

def test_get_candidate_paths_multiple_paths():
    loader = MockAnsibleCollectionLoader('some.module.name')
    path_list = ['/some/path', '/another/path']
    with pytest.raises(ValueError, match='this loader requires exactly one path to search'):
        loader._get_candidate_paths(path_list)

def test_get_candidate_paths_ansible_builtin():
    loader = MockAnsibleCollectionLoader('some.ansible.builtin.module')
    path_list = ['/some/path', '/another/path']
    result = loader._get_candidate_paths(path_list)
    assert result == path_list
