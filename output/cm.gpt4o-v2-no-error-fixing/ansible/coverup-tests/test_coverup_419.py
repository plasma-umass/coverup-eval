# file: lib/ansible/module_utils/common/validation.py:26-39
# asked: {"lines": [26, 36, 37, 39], "branches": [[36, 37], [36, 39]]}
# gained: {"lines": [26, 36, 37, 39], "branches": [[36, 37], [36, 39]]}

import pytest
from ansible.module_utils.common.validation import count_terms
from ansible.module_utils.common.collections import is_iterable

def test_count_terms_with_string(monkeypatch):
    # Mocking is_iterable to return False for strings
    def mock_is_iterable(seq, include_strings=False):
        if isinstance(seq, str):
            return False
        return is_iterable(seq, include_strings)
    
    monkeypatch.setattr('ansible.module_utils.common.collections.is_iterable', mock_is_iterable)
    
    terms = "key1"
    parameters = {"key1": "value1", "key2": "value2"}
    result = count_terms(terms, parameters)
    
    assert result == 1

def test_count_terms_with_iterable(monkeypatch):
    # Mocking is_iterable to return True for lists
    def mock_is_iterable(seq, include_strings=False):
        if isinstance(seq, list):
            return True
        return is_iterable(seq, include_strings)
    
    monkeypatch.setattr('ansible.module_utils.common.collections.is_iterable', mock_is_iterable)
    
    terms = ["key1", "key3"]
    parameters = {"key1": "value1", "key2": "value2"}
    result = count_terms(terms, parameters)
    
    assert result == 1

def test_count_terms_with_no_match(monkeypatch):
    # Mocking is_iterable to return True for lists
    def mock_is_iterable(seq, include_strings=False):
        if isinstance(seq, list):
            return True
        return is_iterable(seq, include_strings)
    
    monkeypatch.setattr('ansible.module_utils.common.collections.is_iterable', mock_is_iterable)
    
    terms = ["key3", "key4"]
    parameters = {"key1": "value1", "key2": "value2"}
    result = count_terms(terms, parameters)
    
    assert result == 0
