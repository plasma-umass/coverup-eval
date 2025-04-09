# file: lib/ansible/module_utils/common/validation.py:26-39
# asked: {"lines": [26, 36, 37, 39], "branches": [[36, 37], [36, 39]]}
# gained: {"lines": [26, 36, 37, 39], "branches": [[36, 37], [36, 39]]}

import pytest
from ansible.module_utils.common.validation import count_terms

def test_count_terms_with_string_key():
    terms = 'key1'
    parameters = {'key1': 'value1', 'key2': 'value2'}
    result = count_terms(terms, parameters)
    assert result == 1

def test_count_terms_with_iterable_keys():
    terms = ['key1', 'key3']
    parameters = {'key1': 'value1', 'key2': 'value2'}
    result = count_terms(terms, parameters)
    assert result == 1

def test_count_terms_with_no_match():
    terms = 'key3'
    parameters = {'key1': 'value1', 'key2': 'value2'}
    result = count_terms(terms, parameters)
    assert result == 0

def test_count_terms_with_multiple_matches():
    terms = ['key1', 'key2']
    parameters = {'key1': 'value1', 'key2': 'value2'}
    result = count_terms(terms, parameters)
    assert result == 2
