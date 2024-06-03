# file lib/ansible/utils/collection_loader/_collection_finder.py:505-514
# lines [509, 514]
# branches ['508->509', '513->514']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionNSPkgLoader

class MockLoader(_AnsibleCollectionNSPkgLoader):
    def __init__(self, split_name, fullname, subpackage_search_paths, package_to_load, candidate_paths):
        self._split_name = split_name
        self._fullname = fullname
        self._subpackage_search_paths = subpackage_search_paths
        self._package_to_load = package_to_load
        self._candidate_paths = candidate_paths
        self._source_code_path = None  # Mock attribute to avoid AttributeError

    def _validate_args(self):
        if len(self._split_name) != 2:
            raise ImportError('this loader can only load collections namespace packages, not {0}'.format(self._fullname))

def test_validate_args_raises_import_error():
    loader = MockLoader(split_name=['invalid'], fullname='invalid.fullname', subpackage_search_paths=[], package_to_load='', candidate_paths=[])
    with pytest.raises(ImportError, match='this loader can only load collections namespace packages, not invalid.fullname'):
        loader._validate_args()

def test_validate_final_raises_import_error():
    loader = MockLoader(split_name=['valid', 'name'], fullname='valid.name', subpackage_search_paths=[], package_to_load='not_ansible', candidate_paths=['some_path'])
    with pytest.raises(ImportError, match="no not_ansible found in \['some_path'\]"):
        loader._validate_final()
