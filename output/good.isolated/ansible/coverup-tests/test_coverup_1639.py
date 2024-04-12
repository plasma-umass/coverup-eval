# file lib/ansible/utils/collection_loader/_collection_finder.py:187-225
# lines [202, 208, 222]
# branches ['201->202', '207->208', '219->222']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

class _AnsibleInternalRedirectLoader:
    def __init__(self, fullname, path_list):
        pass

class _AnsibleCollectionRootPkgLoader:
    def __init__(self, fullname, path_list):
        pass

class _AnsibleCollectionNSPkgLoader:
    def __init__(self, fullname, path_list):
        pass

class _AnsibleCollectionPkgLoader:
    def __init__(self, fullname, path_list):
        pass

class _AnsibleCollectionLoader:
    def __init__(self, fullname, path_list):
        pass

@pytest.fixture
def collection_finder():
    return _AnsibleCollectionFinder()

def test_find_module_with_path_for_toplevel_package(collection_finder):
    with pytest.raises(ValueError) as excinfo:
        collection_finder.find_module('ansible', path=['some_path'])
    assert 'path should not be specified for top-level packages' in str(excinfo.value)

def test_find_module_without_path_for_subpackage(collection_finder):
    with pytest.raises(ValueError) as excinfo:
        collection_finder.find_module('ansible.module.submodule')
    assert 'path must be specified for subpackages' in str(excinfo.value)

def test_find_module_for_deep_subpackage(collection_finder, mocker):
    mocker.patch('ansible.utils.collection_loader._collection_finder._AnsibleCollectionLoader', new=_AnsibleCollectionLoader)
    loader = collection_finder.find_module('ansible_collections.namespace.collection.module', path=['some_path'])
    assert isinstance(loader, _AnsibleCollectionLoader)
