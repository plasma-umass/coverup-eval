# file: lib/ansible/utils/collection_loader/_collection_finder.py:769-810
# asked: {"lines": [769, 770, 783, 784, 786, 787, 788, 790, 791, 792, 793, 794, 796, 797, 798, 802, 803, 804, 806, 808, 810], "branches": [[783, 784], [783, 786], [790, 791], [790, 796], [803, 804], [803, 806]]}
# gained: {"lines": [769, 770, 783, 784, 786, 787, 788, 790, 791, 792, 793, 794, 796, 797, 798, 802, 803, 804, 806, 808, 810], "branches": [[783, 784], [783, 786], [790, 791], [790, 796], [803, 804], [803, 806]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_native, to_text

class TestAnsibleCollectionRef:
    
    @pytest.mark.parametrize("ref, ref_type", [
        ("namespace.collection.module_name", "module"),
        ("namespace.collection.subdir.module_name", "module"),
        ("namespace.collection.role_name", "role"),
        ("namespace.collection.subdir1.subdir2.module_name", "module"),
        ("namespace.collection.playbook_name.yml", "playbook"),
    ])
    def test_from_fqcr_valid(self, ref, ref_type, monkeypatch):
        # Mock the VALID_REF_TYPES to include the test ref_type
        monkeypatch.setattr(AnsibleCollectionRef, 'VALID_REF_TYPES', ['module', 'role', 'playbook'])
        
        result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
        assert result is not None
        assert isinstance(result, AnsibleCollectionRef)
    
    @pytest.mark.parametrize("ref, ref_type", [
        ("invalid_ref", "module"),
        ("namespace.collection", "module"),
        ("namespace.collection.", "module"),
        ("namespace.collection..module_name", "module"),
    ])
    def test_from_fqcr_invalid(self, ref, ref_type, monkeypatch):
        # Mock the VALID_REF_TYPES to include the test ref_type
        monkeypatch.setattr(AnsibleCollectionRef, 'VALID_REF_TYPES', ['module', 'role', 'playbook'])
        
        with pytest.raises(ValueError):
            AnsibleCollectionRef.from_fqcr(ref, ref_type)
    
    def test_from_fqcr_playbook_with_extension(self, monkeypatch):
        ref = "namespace.collection.playbook_name.yml"
        ref_type = "playbook"
        
        # Mock the VALID_REF_TYPES to include the test ref_type
        monkeypatch.setattr(AnsibleCollectionRef, 'VALID_REF_TYPES', ['module', 'role', 'playbook'])
        
        result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
        assert result is not None
        assert isinstance(result, AnsibleCollectionRef)
        assert result.resource.endswith(".yml")
    
    def test_from_fqcr_module_with_subdirs(self, monkeypatch):
        ref = "namespace.collection.subdir1.subdir2.module_name"
        ref_type = "module"
        
        # Mock the VALID_REF_TYPES to include the test ref_type
        monkeypatch.setattr(AnsibleCollectionRef, 'VALID_REF_TYPES', ['module', 'role', 'playbook'])
        
        result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
        assert result is not None
        assert isinstance(result, AnsibleCollectionRef)
        assert result.subdirs == "subdir1.subdir2"
    
    def test_from_fqcr_role(self, monkeypatch):
        ref = "namespace.collection.role_name"
        ref_type = "role"
        
        # Mock the VALID_REF_TYPES to include the test ref_type
        monkeypatch.setattr(AnsibleCollectionRef, 'VALID_REF_TYPES', ['module', 'role', 'playbook'])
        
        result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
        assert result is not None
        assert isinstance(result, AnsibleCollectionRef)
        assert result.resource == "role_name"
        assert result.ref_type == "role"
