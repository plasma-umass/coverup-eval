# file lib/ansible/plugins/lookup/varnames.py:54-79
# lines [54, 56, 58, 59, 61, 63, 64, 65, 67, 68, 70, 71, 72, 73, 75, 76, 77, 79]
# branches ['58->59', '58->61', '65->67', '65->79', '67->68', '67->70', '75->65', '75->76', '76->75', '76->77']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.varnames import LookupModule
import re

@pytest.fixture
def lookup_module():
    module = LookupModule()
    module._load_name = 'varnames'  # Mock the _load_name attribute
    return module

def test_run_no_variables(lookup_module):
    with pytest.raises(AnsibleError, match='No variables available to search'):
        lookup_module.run(['test'])

def test_run_invalid_term_type(lookup_module):
    with pytest.raises(AnsibleError, match='Invalid setting identifier'):
        lookup_module.run([123], variables={'test_var': 'value'})

def test_run_invalid_regex(lookup_module):
    with pytest.raises(AnsibleError, match='Unable to use'):
        lookup_module.run(['[invalid'], variables={'test_var': 'value'})

def test_run_valid_case(lookup_module):
    variables = {'test_var': 'value', 'another_var': 'value2'}
    terms = ['test_var', 'another_var']
    result = lookup_module.run(terms, variables=variables)
    assert result == ['test_var', 'another_var']

def test_run_partial_match(lookup_module):
    variables = {'test_var': 'value', 'another_var': 'value2'}
    terms = ['test_.*']
    result = lookup_module.run(terms, variables=variables)
    assert result == ['test_var']

def test_run_no_match(lookup_module):
    variables = {'test_var': 'value', 'another_var': 'value2'}
    terms = ['nonexistent_var']
    result = lookup_module.run(terms, variables=variables)
    assert result == []
