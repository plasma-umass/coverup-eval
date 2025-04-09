# file lib/ansible/module_utils/common/validation.py:26-39
# lines [26, 36, 37, 39]
# branches ['36->37', '36->39']

import pytest
from ansible.module_utils.common.validation import count_terms

def test_count_terms_single_term():
    parameters = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    term = 'key1'
    assert count_terms(term, parameters) == 1

def test_count_terms_multiple_terms():
    parameters = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    terms = ['key1', 'key2']
    assert count_terms(terms, parameters) == 2

def test_count_terms_no_match():
    parameters = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    terms = ['key4', 'key5']
    assert count_terms(terms, parameters) == 0

def test_count_terms_empty_parameters():
    parameters = {}
    terms = ['key1', 'key2']
    assert count_terms(terms, parameters) == 0

def test_count_terms_empty_terms():
    parameters = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    terms = []
    assert count_terms(terms, parameters) == 0

def test_count_terms_non_iterable_term():
    parameters = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    term = 123  # Non-iterable term
    assert count_terms(term, parameters) == 0

def test_count_terms_term_is_none():
    parameters = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    term = None  # None should be treated as a non-iterable term
    assert count_terms(term, parameters) == 0

def test_count_terms_parameters_contains_none():
    parameters = {'key1': 'value1', 'key2': 'value2', 'key3': None}
    terms = ['key3']
    assert count_terms(terms, parameters) == 1

# Mocking is_iterable to force the branch where it returns False
def test_count_terms_with_mocked_is_iterable(mocker):
    mocker.patch('ansible.module_utils.common.validation.is_iterable', return_value=False)
    parameters = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    term = 'key1'  # Use a single term to avoid TypeError with unhashable list
    assert count_terms(term, parameters) == 1
