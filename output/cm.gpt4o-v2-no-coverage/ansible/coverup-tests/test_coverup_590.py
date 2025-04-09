# file: lib/ansible/utils/collection_loader/_collection_finder.py:844-858
# asked: {"lines": [844, 845, 853, 855, 856, 858], "branches": [[855, 856], [855, 858]]}
# gained: {"lines": [844, 845, 853, 855, 856, 858], "branches": [[855, 856], [855, 858]]}

import re
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

def test_is_valid_fqcr_no_ref_type(monkeypatch):
    # Mock the VALID_FQCR_RE to match a specific pattern
    monkeypatch.setattr(AnsibleCollectionRef, 'VALID_FQCR_RE', re.compile(r'^ns\.coll(\.\w+)+$'))
    
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource') is True
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.subdir.resource') is True
    assert AnsibleCollectionRef.is_valid_fqcr('invalid.resource') is False

def test_is_valid_fqcr_with_ref_type(monkeypatch):
    # Mock the try_parse_fqcr method to return True for specific inputs
    def mock_try_parse_fqcr(ref, ref_type):
        return ref == 'ns.coll.resource' and ref_type == 'module'
    
    monkeypatch.setattr(AnsibleCollectionRef, 'try_parse_fqcr', mock_try_parse_fqcr)
    
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource', 'module') is True
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource', 'role') is False
    assert AnsibleCollectionRef.is_valid_fqcr('invalid.resource', 'module') is False
