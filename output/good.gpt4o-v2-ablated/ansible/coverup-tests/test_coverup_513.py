# file: lib/ansible/module_utils/common/validation.py:26-39
# asked: {"lines": [37], "branches": [[36, 37]]}
# gained: {"lines": [37], "branches": [[36, 37]]}

import pytest
from ansible.module_utils.common.validation import count_terms

def test_count_terms_single_term():
    parameters = {'key1': 'value1', 'key2': 'value2'}
    assert count_terms('key1', parameters) == 1

def test_count_terms_multiple_terms():
    parameters = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    assert count_terms(['key1', 'key2'], parameters) == 2

def test_count_terms_no_match():
    parameters = {'key1': 'value1', 'key2': 'value2'}
    assert count_terms('key3', parameters) == 0

def test_count_terms_empty_terms():
    parameters = {'key1': 'value1', 'key2': 'value2'}
    assert count_terms([], parameters) == 0

def test_count_terms_empty_parameters():
    parameters = {}
    assert count_terms('key1', parameters) == 0

def test_count_terms_non_iterable_terms():
    parameters = {'key1': 'value1', 'key2': 'value2'}
    assert count_terms('key1', parameters) == 1

def test_count_terms_non_string_terms():
    parameters = {1: 'value1', 2: 'value2'}
    assert count_terms(1, parameters) == 1

def test_count_terms_mixed_terms():
    parameters = {'key1': 'value1', 2: 'value2'}
    assert count_terms(['key1', 2], parameters) == 2
