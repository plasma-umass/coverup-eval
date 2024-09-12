# file: lib/ansible/plugins/lookup/first_found.py:206-236
# asked: {"lines": [208, 215, 217, 218, 220, 221, 222, 223, 226, 229, 230, 233, 235, 236], "branches": [[218, 220], [218, 233], [229, 218], [229, 230], [233, 235], [233, 236]]}
# gained: {"lines": [208, 215, 217, 218, 220, 221, 226, 229, 230, 233, 235, 236], "branches": [[218, 220], [218, 233], [229, 218], [229, 230], [233, 235], [233, 236]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.first_found import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_run_all_lines_executed(lookup_module, monkeypatch):
    terms = ['testfile']
    variables = {'ansible_search_path': ['/tmp']}
    kwargs = {}

    # Mocking _process_terms to return specific values
    monkeypatch.setattr(lookup_module, '_process_terms', lambda terms, variables, kwargs: (['/tmp/testfile'], False))
    
    # Mocking _templar.template to return the filename as is
    templar_mock = MagicMock()
    templar_mock.template = lambda x: x
    monkeypatch.setattr(lookup_module, '_templar', templar_mock)
    
    # Mocking find_file_in_search_path to return a specific path
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', lambda variables, subdir, fn, ignore_missing: '/tmp/testfile')

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ['/tmp/testfile']

def test_run_no_file_found(lookup_module, monkeypatch):
    terms = ['testfile']
    variables = {'ansible_search_path': ['/tmp']}
    kwargs = {}

    # Mocking _process_terms to return specific values
    monkeypatch.setattr(lookup_module, '_process_terms', lambda terms, variables, kwargs: (['/tmp/testfile'], False))
    
    # Mocking _templar.template to return the filename as is
    templar_mock = MagicMock()
    templar_mock.template = lambda x: x
    monkeypatch.setattr(lookup_module, '_templar', templar_mock)
    
    # Mocking find_file_in_search_path to return None
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', lambda variables, subdir, fn, ignore_missing: None)

    with pytest.raises(AnsibleLookupError, match="No file was found when using first_found."):
        lookup_module.run(terms, variables, **kwargs)

def test_run_skip(lookup_module, monkeypatch):
    terms = ['testfile']
    variables = {'ansible_search_path': ['/tmp']}
    kwargs = {}

    # Mocking _process_terms to return specific values with skip=True
    monkeypatch.setattr(lookup_module, '_process_terms', lambda terms, variables, kwargs: (['/tmp/testfile'], True))
    
    # Mocking _templar.template to return the filename as is
    templar_mock = MagicMock()
    templar_mock.template = lambda x: x
    monkeypatch.setattr(lookup_module, '_templar', templar_mock)
    
    # Mocking find_file_in_search_path to return None
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', lambda variables, subdir, fn, ignore_missing: None)

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == []
