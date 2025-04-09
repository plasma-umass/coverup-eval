# file lib/ansible/plugins/lookup/first_found.py:146-159
# lines [146, 149, 150, 151, 152, 153, 156, 157, 159]
# branches ['150->151', '150->156', '151->152', '151->153', '156->157', '156->159']

import pytest
from ansible.plugins.lookup.first_found import _split_on
from ansible.module_utils.six import string_types

def test_split_on_with_string_input(mocker):
    terms = "file1.yml,file2.yml file3.yml:file4.yml"
    spliters = ', :'
    expected_terms = ['file1.yml', 'file2.yml', 'file3.yml', 'file4.yml']
    
    mocker.patch('ansible.plugins.lookup.first_found.string_types', new=(str,))
    
    result = _split_on(terms, spliters)
    assert result == expected_terms

def test_split_on_with_list_input(mocker):
    terms = ["file1.yml,file2.yml", "file3.yml:file4.yml"]
    spliters = ', :'
    expected_terms = ['file1.yml', 'file2.yml', 'file3.yml', 'file4.yml']
    
    mocker.patch('ansible.plugins.lookup.first_found.string_types', new=(str,))
    
    result = _split_on(terms, spliters)
    assert result == expected_terms
