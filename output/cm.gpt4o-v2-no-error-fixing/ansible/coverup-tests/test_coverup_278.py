# file: lib/ansible/utils/collection_loader/_collection_finder.py:860-877
# asked: {"lines": [860, 861, 868, 870, 871, 873, 875, 876], "branches": [[870, 871], [870, 873]]}
# gained: {"lines": [860, 861, 868, 870, 871, 873, 875, 876], "branches": [[870, 871], [870, 873]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils.common.text.converters import to_text

def test_is_valid_collection_name_valid(monkeypatch):
    def mock_to_text(obj, encoding='utf-8', errors=None, nonstring='simplerepr'):
        return str(obj)
    
    monkeypatch.setattr('ansible.module_utils.common.text.converters.to_text', mock_to_text)
    
    assert AnsibleCollectionRef.is_valid_collection_name('valid_ns.valid_name') == True

def test_is_valid_collection_name_invalid_no_dot(monkeypatch):
    def mock_to_text(obj, encoding='utf-8', errors=None, nonstring='simplerepr'):
        return str(obj)
    
    monkeypatch.setattr('ansible.module_utils.common.text.converters.to_text', mock_to_text)
    
    assert AnsibleCollectionRef.is_valid_collection_name('invalid_ns_invalid_name') == False

def test_is_valid_collection_name_invalid_keyword(monkeypatch):
    def mock_to_text(obj, encoding='utf-8', errors=None, nonstring='simplerepr'):
        return str(obj)
    
    monkeypatch.setattr('ansible.module_utils.common.text.converters.to_text', mock_to_text)
    
    assert AnsibleCollectionRef.is_valid_collection_name('for.valid_name') == False

def test_is_valid_collection_name_invalid_identifier(monkeypatch):
    def mock_to_text(obj, encoding='utf-8', errors=None, nonstring='simplerepr'):
        return str(obj)
    
    monkeypatch.setattr('ansible.module_utils.common.text.converters.to_text', mock_to_text)
    
    assert AnsibleCollectionRef.is_valid_collection_name('valid_ns.123invalid') == False
