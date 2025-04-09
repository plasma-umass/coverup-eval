# file: lib/ansible/module_utils/common/validation.py:26-39
# asked: {"lines": [26, 36, 37, 39], "branches": [[36, 37], [36, 39]]}
# gained: {"lines": [26, 36, 37, 39], "branches": [[36, 37], [36, 39]]}

import pytest
from ansible.module_utils.common.validation import count_terms
from ansible.module_utils.common.collections import is_iterable

def test_count_terms_with_string_key():
    parameters = {'key1': 'value1', 'key2': 'value2'}
    terms = 'key1'
    result = count_terms(terms, parameters)
    assert result == 1

def test_count_terms_with_iterable_keys():
    parameters = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    terms = ['key1', 'key3']
    result = count_terms(terms, parameters)
    assert result == 2

def test_count_terms_with_no_matching_keys():
    parameters = {'key1': 'value1', 'key2': 'value2'}
    terms = ['key3', 'key4']
    result = count_terms(terms, parameters)
    assert result == 0

def test_count_terms_with_non_iterable_terms():
    parameters = {'key1': 'value1', 'key2': 'value2'}
    terms = 123
    result = count_terms(terms, parameters)
    assert result == 0

def test_is_iterable_with_string():
    assert is_iterable('string') == False

def test_is_iterable_with_list():
    assert is_iterable(['list']) == True

def test_is_iterable_with_dict():
    assert is_iterable({'key': 'value'}) == True

def test_is_iterable_with_int():
    assert is_iterable(123) == False
