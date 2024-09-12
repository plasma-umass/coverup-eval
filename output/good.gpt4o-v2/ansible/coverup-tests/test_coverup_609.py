# file: lib/ansible/utils/collection_loader/_collection_finder.py:406-409
# asked: {"lines": [406, 407, 408, 409], "branches": [[407, 408], [407, 409]]}
# gained: {"lines": [406, 407, 408, 409], "branches": [[407, 408], [407, 409]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

def test_is_package_correct_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test.fullname', path_list=[])
    assert loader.is_package('ansible_collections.test.fullname') == (loader._subpackage_search_paths is not None)

def test_is_package_incorrect_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test.fullname', path_list=[])
    with pytest.raises(ValueError) as excinfo:
        loader.is_package('ansible_collections.wrong.fullname')
    assert str(excinfo.value) == 'this loader cannot answer is_package for ansible_collections.wrong.fullname, only ansible_collections.test.fullname'
