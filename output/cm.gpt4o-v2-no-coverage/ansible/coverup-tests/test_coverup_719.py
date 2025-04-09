# file: lib/ansible/utils/collection_loader/_collection_finder.py:319-321
# asked: {"lines": [319, 320, 321], "branches": [[320, 0], [320, 321]]}
# gained: {"lines": [319, 320, 321], "branches": [[320, 0], [320, 321]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, fullname, path_list=None):
        self._fullname = fullname
        self._redirect_module = None
        self._split_name = fullname.split('.')
        self._rpart_name = fullname.rpartition('.')
        self._parent_package_name = self._rpart_name[0]
        self._package_to_load = self._rpart_name[2]
        self._source_code_path = None
        self._decoded_source = None
        self._compiled_code = None
        self._validate_args()

def test_validate_args_correct_package():
    loader = TestAnsibleCollectionPkgLoaderBase('ansible_collections.test')
    try:
        loader._validate_args()
    except ImportError:
        pytest.fail("Unexpected ImportError raised")

def test_validate_args_incorrect_package():
    with pytest.raises(ImportError, match="this loader can only load packages from the ansible_collections package, not invalid_package"):
        loader = TestAnsibleCollectionPkgLoaderBase('invalid_package.test')
        loader._validate_args()
