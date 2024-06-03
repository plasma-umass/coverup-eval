# file lib/ansible/utils/collection_loader/_collection_finder.py:299-316
# lines [299, 300, 301, 302, 303, 304, 305, 307, 308, 309, 311, 313, 314, 316]
# branches []

import pytest
from unittest import mock

# Assuming the class is imported from the module
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def mock_to_native(mocker):
    return mocker.patch('ansible.utils.collection_loader._collection_finder.to_native', side_effect=lambda x: x)

def test_ansible_collection_pkg_loader_base(mock_to_native):
    fullname = 'ansible_collections.somens'
    path_list = ['/some/path', '/another/path']
    
    with mock.patch.object(_AnsibleCollectionPkgLoaderBase, '_get_candidate_paths', return_value=[f"{p}/somens" for p in path_list]), \
         mock.patch.object(_AnsibleCollectionPkgLoaderBase, '_get_subpackage_search_paths', return_value=[]), \
         mock.patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_args'), \
         mock.patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_final'):
        
        loader = _AnsibleCollectionPkgLoaderBase(fullname, path_list)
        
        assert loader._fullname == fullname
        assert loader._split_name == fullname.split('.')
        assert loader._rpart_name == fullname.rpartition('.')
        assert loader._parent_package_name == 'ansible_collections'
        assert loader._package_to_load == 'somens'
        
        assert loader._source_code_path is None
        assert loader._decoded_source is None
        assert loader._compiled_code is None
        
        assert loader._candidate_paths == [f"{p}/somens" for p in path_list]
        assert isinstance(loader._subpackage_search_paths, list)
