# file: lib/ansible/utils/collection_loader/_collection_finder.py:844-858
# asked: {"lines": [858], "branches": [[855, 858]]}
# gained: {"lines": [858], "branches": [[855, 858]]}

import pytest
import re
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_text

# Mocking the regex and try_parse_fqcr method for testing purposes
@pytest.fixture
def mock_valid_fqcr_re(monkeypatch):
    monkeypatch.setattr(AnsibleCollectionRef, 'VALID_FQCR_RE', r'^[a-z]+\.[a-z]+\.[a-z]+$')

@pytest.fixture
def mock_try_parse_fqcr(monkeypatch):
    def mock_parse(ref, ref_type):
        return ref == "valid.ns.coll.resource" and ref_type in ["module", "role", "doc_fragment"]
    monkeypatch.setattr(AnsibleCollectionRef, 'try_parse_fqcr', mock_parse)

def test_is_valid_fqcr_no_ref_type(mock_valid_fqcr_re):
    assert AnsibleCollectionRef.is_valid_fqcr("ns.coll.resource") is True
    assert AnsibleCollectionRef.is_valid_fqcr("invalid_ref") is False

def test_is_valid_fqcr_with_ref_type(mock_try_parse_fqcr):
    assert AnsibleCollectionRef.is_valid_fqcr("valid.ns.coll.resource", "module") is True
    assert AnsibleCollectionRef.is_valid_fqcr("valid.ns.coll.resource", "invalid_type") is False
    assert AnsibleCollectionRef.is_valid_fqcr("invalid_ref", "module") is False
