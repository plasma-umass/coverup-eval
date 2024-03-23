# file lib/ansible/utils/collection_loader/_collection_finder.py:505-514
# lines [505, 506, 507, 508, 509, 511, 513, 514]
# branches ['508->exit', '508->509', '513->exit', '513->514']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionNSPkgLoader

def test_ansible_collection_nspkgloader_validate_args_raises_import_error(mocker):
    mocker.patch.object(_AnsibleCollectionNSPkgLoader, '__init__', return_value=None)
    loader = _AnsibleCollectionNSPkgLoader()
    loader._fullname = 'invalid.name'
    loader._split_name = ['invalid', 'name', 'extra']
    with pytest.raises(ImportError) as excinfo:
        loader._validate_args()
    assert 'this loader can only load packages from the ansible_collections package' in str(excinfo.value)

def test_ansible_collection_nspkgloader_validate_final_raises_import_error(mocker):
    mocker.patch.object(_AnsibleCollectionNSPkgLoader, '__init__', return_value=None)
    loader = _AnsibleCollectionNSPkgLoader()
    loader._subpackage_search_paths = []
    loader._package_to_load = 'ansible.collection'
    loader._candidate_paths = ['/fake/path']
    with pytest.raises(ImportError) as excinfo:
        loader._validate_final()
    assert 'no ansible.collection found in' in str(excinfo.value)
