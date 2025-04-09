# file: lib/ansible/utils/collection_loader/_collection_finder.py:705-760
# asked: {"lines": [705, 713, 714, 715, 716, 717, 719, 720, 722, 723, 725, 726, 727, 728, 729, 731, 733, 734, 736, 737, 739, 741, 742, 743, 744, 747, 749, 750, 751, 753, 755, 757, 759, 760], "branches": [[714, 715], [714, 716], [719, 720], [719, 722], [722, 723], [722, 725], [726, 727], [726, 731], [727, 728], [727, 729], [741, 742], [741, 743], [743, 744], [743, 747], [749, 750], [749, 753], [753, 755], [753, 757]]}
# gained: {"lines": [705, 713, 714, 715, 716, 717, 719, 720, 722, 723, 725, 726, 727, 728, 729, 731, 733, 734, 736, 737, 739, 741, 742, 743, 744, 747, 749, 750, 751, 753, 755, 757, 759, 760], "branches": [[714, 715], [714, 716], [719, 720], [719, 722], [722, 723], [722, 725], [726, 727], [726, 731], [727, 728], [727, 729], [741, 742], [741, 743], [743, 744], [743, 747], [749, 750], [749, 753], [753, 755], [753, 757]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_text, to_native

class TestAnsibleCollectionRef:
    @pytest.fixture(autouse=True)
    def setup(self, monkeypatch):
        # Mock the VALID_REF_TYPES and is_valid_collection_name for testing
        monkeypatch.setattr(AnsibleCollectionRef, 'VALID_REF_TYPES', ['module', 'role', 'playbook', 'doc_fragment'])
        monkeypatch.setattr(AnsibleCollectionRef, 'is_valid_collection_name', lambda self, name: '.' in name)

    def test_valid_collection_ref(self):
        collection_name = 'namespace.collectionname'
        subdirs = 'subdir1.subdir2'
        resource = 'mymodule'
        ref_type = 'module'
        
        ref = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
        
        assert ref.collection == collection_name
        assert ref.subdirs == subdirs
        assert ref.resource == resource
        assert ref.ref_type == ref_type
        assert ref.n_python_collection_package_name == 'ansible_collections.namespace.collectionname'
        assert ref.n_python_package_name == 'ansible_collections.namespace.collectionname.plugins.module.subdir1.subdir2'
        assert ref._fqcr == 'namespace.collectionname.subdir1.subdir2.mymodule'

    def test_invalid_collection_name(self):
        with pytest.raises(ValueError, match='invalid collection name'):
            AnsibleCollectionRef('invalid_collection_name', None, 'mymodule', 'module')

    def test_invalid_ref_type(self):
        with pytest.raises(ValueError, match='invalid collection ref_type'):
            AnsibleCollectionRef('namespace.collectionname', None, 'mymodule', 'invalid_type')

    def test_invalid_subdirs(self):
        with pytest.raises(ValueError, match='invalid subdirs entry'):
            AnsibleCollectionRef('namespace.collectionname', 'invalid/subdir', 'mymodule', 'module')

    def test_role_ref_type(self):
        collection_name = 'namespace.collectionname'
        subdirs = None
        resource = 'myrole'
        ref_type = 'role'
        
        ref = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
        
        assert ref.collection == collection_name
        assert ref.subdirs == ''
        assert ref.resource == resource
        assert ref.ref_type == ref_type
        assert ref.n_python_collection_package_name == 'ansible_collections.namespace.collectionname'
        assert ref.n_python_package_name == 'ansible_collections.namespace.collectionname.roles.myrole'
        assert ref._fqcr == 'namespace.collectionname.myrole'

    def test_playbook_ref_type(self):
        collection_name = 'namespace.collectionname'
        subdirs = None
        resource = 'myplaybook'
        ref_type = 'playbook'
        
        ref = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)
        
        assert ref.collection == collection_name
        assert ref.subdirs == ''
        assert ref.resource == resource
        assert ref.ref_type == ref_type
        assert ref.n_python_collection_package_name == 'ansible_collections.namespace.collectionname'
        assert ref.n_python_package_name == 'ansible_collections.namespace.collectionname.playbooks.myplaybook'
        assert ref._fqcr == 'namespace.collectionname.myplaybook'
