# file lib/ansible/utils/collection_loader/_collection_finder.py:492-496
# lines [492, 493, 494, 495, 496]
# branches ['495->exit', '495->496']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionRootPkgLoader

class TestAnsibleCollectionRootPkgLoader:
    @pytest.fixture
    def mock_loader(self, mocker):
        mocker.patch.object(_AnsibleCollectionRootPkgLoader, '__init__', return_value=None)
        loader = _AnsibleCollectionRootPkgLoader()
        loader._split_name = None
        loader._fullname = None
        return loader

    def test_validate_args_success(self, mock_loader):
        mock_loader._split_name = ['ansible_collections']
        mock_loader._fullname = 'ansible_collections'
        # No exception should be raised
        mock_loader._validate_args()

    def test_validate_args_failure(self, mock_loader):
        mock_loader._split_name = ['ansible_collections', 'extra']
        mock_loader._fullname = 'ansible_collections.extra'
        with pytest.raises(ImportError) as excinfo:
            mock_loader._validate_args()
        assert str(excinfo.value) == 'this loader can only load the ansible_collections toplevel package, not ansible_collections.extra'
