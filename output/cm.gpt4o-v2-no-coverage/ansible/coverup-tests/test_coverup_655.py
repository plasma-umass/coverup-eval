# file: lib/ansible/utils/collection_loader/_collection_finder.py:406-409
# asked: {"lines": [406, 407, 408, 409], "branches": [[407, 408], [407, 409]]}
# gained: {"lines": [406, 407, 408, 409], "branches": [[407, 408], [407, 409]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:
    
    @pytest.fixture
    def loader(self):
        return _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.test.package', path_list=['/some/path'])

    def test_is_package_correct_fullname(self, loader):
        assert loader.is_package('ansible_collections.test.package') == (loader._subpackage_search_paths is not None)

    def test_is_package_incorrect_fullname(self, loader):
        with pytest.raises(ValueError) as excinfo:
            loader.is_package('wrong.package')
        assert str(excinfo.value) == 'this loader cannot answer is_package for wrong.package, only ansible_collections.test.package'
