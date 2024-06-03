# file lib/ansible/utils/collection_loader/_collection_finder.py:319-321
# lines [321]
# branches ['320->321']

import pytest
from unittest import mock

# Assuming the class _AnsibleCollectionPkgLoaderBase is imported from the module
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:
    @pytest.fixture
    def loader(self):
        class MockLoader(_AnsibleCollectionPkgLoaderBase):
            def __init__(self, split_name, fullname):
                self._split_name = split_name
                self._fullname = fullname

        return MockLoader

    def test_validate_args_import_error(self, loader):
        # Create an instance of the loader with a split_name that will trigger the ImportError
        instance = loader(['not_ansible_collections'], 'not_ansible_collections.some_module')
        
        # Verify that ImportError is raised with the correct message
        with pytest.raises(ImportError) as excinfo:
            instance._validate_args()
        
        assert str(excinfo.value) == 'this loader can only load packages from the ansible_collections package, not not_ansible_collections.some_module'
