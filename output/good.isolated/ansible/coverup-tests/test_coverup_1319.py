# file lib/ansible/utils/collection_loader/_collection_finder.py:524-532
# lines [528, 529, 532]
# branches ['525->528', '528->529', '528->532']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoader

@pytest.fixture
def mock_ansible_collection_pkg_loader(mocker):
    mocker.patch.object(_AnsibleCollectionPkgLoader, '__init__', lambda self: None)
    loader = _AnsibleCollectionPkgLoader()
    loader._split_name = ['ansible', 'collection', 'namespace', 'name']
    loader._package_to_load = 'namespace.name'
    return loader

def test_validate_final_no_search_paths(mock_ansible_collection_pkg_loader):
    mock_ansible_collection_pkg_loader._subpackage_search_paths = []
    mock_ansible_collection_pkg_loader._candidate_paths = ['/fake/path1', '/fake/path2']
    with pytest.raises(ImportError) as excinfo:
        mock_ansible_collection_pkg_loader._validate_final()
    assert 'no namespace.name found in' in str(excinfo.value)

def test_validate_final_with_search_paths(mock_ansible_collection_pkg_loader):
    mock_ansible_collection_pkg_loader._subpackage_search_paths = ['/fake/path1', '/fake/path2']
    mock_ansible_collection_pkg_loader._validate_final()
    assert mock_ansible_collection_pkg_loader._subpackage_search_paths == ['/fake/path1']
