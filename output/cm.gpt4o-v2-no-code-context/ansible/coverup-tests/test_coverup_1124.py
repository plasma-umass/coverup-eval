# file: lib/ansible/plugins/lookup/first_found.py:164-204
# asked: {"lines": [166, 167, 170, 171, 172, 173, 174, 175, 176, 177, 178, 180, 182, 183, 186, 189, 190, 193, 194, 195, 196, 197, 198, 200, 202, 204], "branches": [[170, 171], [170, 204], [171, 172], [171, 173], [173, 174], [173, 175], [175, 176], [175, 180], [193, 194], [193, 198], [194, 170], [194, 195], [195, 194], [195, 196], [198, 200], [198, 202]]}
# gained: {"lines": [166, 167, 170, 171, 172, 173, 174, 175, 176, 177, 178, 180, 182, 183, 186, 189, 190, 193, 194, 195, 196, 197, 204], "branches": [[170, 171], [170, 204], [171, 172], [171, 173], [173, 174], [173, 175], [175, 176], [175, 180], [193, 194], [194, 170], [194, 195], [195, 194], [195, 196]]}

import pytest
from ansible.plugins.lookup.first_found import LookupModule
from ansible.errors import AnsibleLookupError
from collections.abc import Mapping, Sequence
from ansible.utils.vars import load_extra_vars
import os

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_process_terms_with_mapping(lookup_module, monkeypatch):
    terms = [{'files': 'file1,file2', 'paths': 'path1:path2', 'skip': True}]
    variables = {}
    kwargs = {}
    
    monkeypatch.setattr(lookup_module, 'set_options', lambda var_options, direct: None)
    monkeypatch.setattr(lookup_module, 'get_option', lambda option: terms[0][option])
    
    total_search, skip = lookup_module._process_terms(terms, variables, kwargs)
    
    assert skip is True
    assert total_search == ['path1/file1', 'path1/file2', 'path2/file1', 'path2/file2']

def test_process_terms_with_string(lookup_module, monkeypatch):
    terms = ['file1,file2']
    variables = {}
    kwargs = {'files': 'file1,file2', 'paths': 'path1:path2', 'skip': False}
    
    monkeypatch.setattr(lookup_module, 'set_options', lambda var_options, direct: None)
    monkeypatch.setattr(lookup_module, 'get_option', lambda option: kwargs[option])
    
    total_search, skip = lookup_module._process_terms(terms, variables, kwargs)
    
    assert skip is False
    assert total_search == ['path1/file1', 'path1/file2', 'path2/file1', 'path2/file2']

def test_process_terms_with_sequence(lookup_module, monkeypatch):
    terms = [['file1,file2']]
    variables = {}
    kwargs = {'files': 'file1,file2', 'paths': 'path1:path2', 'skip': False}
    
    monkeypatch.setattr(lookup_module, 'set_options', lambda var_options, direct: None)
    monkeypatch.setattr(lookup_module, 'get_option', lambda option: kwargs[option])
    
    total_search, skip = lookup_module._process_terms(terms, variables, kwargs)
    
    assert skip is False
    assert total_search == ['path1/file1', 'path1/file2', 'path2/file1', 'path2/file2']

def test_process_terms_with_invalid_term(lookup_module):
    terms = [42]
    variables = {}
    kwargs = {}
    
    with pytest.raises(AnsibleLookupError, match="Invalid term supplied, can handle string, mapping or list of strings but got: <class 'int'> for 42"):
        lookup_module._process_terms(terms, variables, kwargs)

def test_process_terms_with_empty_paths(lookup_module, monkeypatch):
    terms = ['file1,file2']
    variables = {}
    kwargs = {'files': 'file1,file2', 'paths': '', 'skip': False}
    
    monkeypatch.setattr(lookup_module, 'set_options', lambda var_options, direct: None)
    monkeypatch.setattr(lookup_module, 'get_option', lambda option: kwargs[option])
    
    total_search, skip = lookup_module._process_terms(terms, variables, kwargs)
    
    assert skip is False
    assert total_search == ['file1', 'file2']
