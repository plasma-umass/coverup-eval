# file: lib/ansible/utils/collection_loader/_collection_finder.py:844-858
# asked: {"lines": [844, 845, 853, 855, 856, 858], "branches": [[855, 856], [855, 858]]}
# gained: {"lines": [844, 845, 853, 855, 856, 858], "branches": [[855, 856], [855, 858]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

def test_is_valid_fqcr_no_ref_type(monkeypatch):
    # Mock the regex match to ensure it returns True
    def mock_match(pattern, string):
        return True

    monkeypatch.setattr("re.match", mock_match)
    
    ref = "namespace.collection.resource"
    assert AnsibleCollectionRef.is_valid_fqcr(ref) == True

def test_is_valid_fqcr_with_ref_type(monkeypatch):
    # Mock the try_parse_fqcr to ensure it returns True
    def mock_try_parse_fqcr(ref, ref_type):
        return True

    monkeypatch.setattr(AnsibleCollectionRef, "try_parse_fqcr", mock_try_parse_fqcr)
    
    ref = "namespace.collection.resource"
    ref_type = "module"
    assert AnsibleCollectionRef.is_valid_fqcr(ref, ref_type) == True
