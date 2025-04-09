# file: lib/ansible/plugins/lookup/first_found.py:164-204
# asked: {"lines": [164, 166, 167, 170, 171, 172, 173, 174, 175, 176, 177, 178, 180, 182, 183, 186, 189, 190, 193, 194, 195, 196, 197, 198, 200, 202, 204], "branches": [[170, 171], [170, 204], [171, 172], [171, 173], [173, 174], [173, 175], [175, 176], [175, 180], [193, 194], [193, 198], [194, 170], [194, 195], [195, 194], [195, 196], [198, 200], [198, 202]]}
# gained: {"lines": [164, 166, 167, 170, 171, 172, 173, 174, 175, 176, 177, 178, 180, 182, 183, 186, 189, 190, 193, 194, 195, 196, 197, 204], "branches": [[170, 171], [170, 204], [171, 172], [171, 173], [173, 174], [173, 175], [175, 176], [175, 180], [193, 194], [194, 170], [194, 195], [195, 194], [195, 196]]}

import os
import pytest
from ansible.errors import AnsibleLookupError
from ansible.module_utils.common._collections_compat import Mapping, Sequence
from ansible.module_utils.six import string_types
from ansible.plugins.lookup.first_found import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_process_terms_string(lookup_module, mocker):
    mocker.patch.object(lookup_module, 'set_options')
    mocker.patch.object(lookup_module, 'get_option', side_effect=lambda x: {'files': 'file1,file2', 'paths': 'path1:path2', 'skip': False}[x])
    
    terms = ['string_term']
    variables = {}
    kwargs = {}
    
    result, skip = lookup_module._process_terms(terms, variables, kwargs)
    
    assert result == ['path1/file1', 'path1/file2', 'path2/file1', 'path2/file2']
    assert skip is False

def test_process_terms_mapping(lookup_module, mocker):
    mocker.patch.object(lookup_module, 'set_options')
    mocker.patch.object(lookup_module, 'get_option', side_effect=lambda x: {'files': 'file1,file2', 'paths': 'path1:path2', 'skip': False}[x])
    
    terms = [{'key': 'value'}]
    variables = {}
    kwargs = {}
    
    result, skip = lookup_module._process_terms(terms, variables, kwargs)
    
    assert result == ['path1/file1', 'path1/file2', 'path2/file1', 'path2/file2']
    assert skip is False

def test_process_terms_sequence(lookup_module, mocker):
    mocker.patch.object(lookup_module, 'set_options')
    mocker.patch.object(lookup_module, 'get_option', side_effect=lambda x: {'files': 'file1,file2', 'paths': 'path1:path2', 'skip': False}[x])
    
    terms = [['string_term']]
    variables = {}
    kwargs = {}
    
    result, skip = lookup_module._process_terms(terms, variables, kwargs)
    
    assert result == ['path1/file1', 'path1/file2', 'path2/file1', 'path2/file2']
    assert skip is False

def test_process_terms_invalid(lookup_module):
    terms = [42]
    variables = {}
    kwargs = {}
    
    with pytest.raises(AnsibleLookupError, match="Invalid term supplied, can handle string, mapping or list of strings but got: <class 'int'> for 42"):
        lookup_module._process_terms(terms, variables, kwargs)

def test_process_terms_no_paths(lookup_module, mocker):
    mocker.patch.object(lookup_module, 'set_options')
    mocker.patch.object(lookup_module, 'get_option', side_effect=lambda x: {'files': 'file1,file2', 'paths': '', 'skip': False}[x])
    
    terms = ['string_term']
    variables = {}
    kwargs = {}
    
    result, skip = lookup_module._process_terms(terms, variables, kwargs)
    
    assert result == ['file1', 'file2']
    assert skip is False

def test_process_terms_no_files(lookup_module, mocker):
    mocker.patch.object(lookup_module, 'set_options')
    mocker.patch.object(lookup_module, 'get_option', side_effect=lambda x: {'files': '', 'paths': 'path1:path2', 'skip': False}[x])
    
    terms = ['string_term']
    variables = {}
    kwargs = {}
    
    result, skip = lookup_module._process_terms(terms, variables, kwargs)
    
    assert result == ['path1/', 'path2/']
    assert skip is False
