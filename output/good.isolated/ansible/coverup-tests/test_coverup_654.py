# file lib/ansible/utils/collection_loader/_collection_finder.py:319-321
# lines [319, 320, 321]
# branches ['320->exit', '320->321']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:

    @pytest.fixture
    def loader(self, mocker):
        mocker.patch.object(_AnsibleCollectionPkgLoaderBase, '__init__', lambda self: None)
        loader = _AnsibleCollectionPkgLoaderBase()
        loader._fullname = "some_other_package"
        loader._split_name = ["some_other_package"]
        return loader

    def test_validate_args_raises_import_error(self, loader):
        with pytest.raises(ImportError) as excinfo:
            loader._validate_args()
        assert "this loader can only load packages from the ansible_collections package" in str(excinfo.value)

    def test_validate_args_passes_for_ansible_collections(self, mocker):
        mocker.patch.object(_AnsibleCollectionPkgLoaderBase, '__init__', lambda self: None)
        loader = _AnsibleCollectionPkgLoaderBase()
        loader._fullname = "ansible_collections.some_collection"
        loader._split_name = ["ansible_collections", "some_collection"]
        try:
            loader._validate_args()  # Should not raise an ImportError
        except ImportError:
            pytest.fail("Unexpected ImportError raised")
