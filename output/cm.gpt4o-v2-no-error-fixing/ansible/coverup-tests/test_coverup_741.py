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
    terms = ['testfile1', 'testfile2']
    variables = {'ansible_search_path': ['/some/path']}
    kwargs = {}

    # Mocking _process_terms to return specific values
    monkeypatch.setattr(lookup_module, '_process_terms', lambda terms, variables, kwargs: (['testfile1', 'testfile2'], False))
    
    # Mocking _templar.template to return the same value
    mock_templar = MagicMock()
    mock_templar.template = lambda x: x
    lookup_module._templar = mock_templar

    # Mocking find_file_in_search_path to return None for the first file and a path for the second
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', lambda variables, subdir, fn, ignore_missing: None if fn == 'testfile1' else '/some/path/testfile2')

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ['/some/path/testfile2']

def test_run_no_file_found(lookup_module, monkeypatch):
    terms = ['testfile1', 'testfile2']
    variables = {'ansible_search_path': ['/some/path']}
    kwargs = {}

    # Mocking _process_terms to return specific values
    monkeypatch.setattr(lookup_module, '_process_terms', lambda terms, variables, kwargs: (['testfile1', 'testfile2'], False))
    
    # Mocking _templar.template to return the same value
    mock_templar = MagicMock()
    mock_templar.template = lambda x: x
    lookup_module._templar = mock_templar

    # Mocking find_file_in_search_path to return None for both files
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', lambda variables, subdir, fn, ignore_missing: None)

    with pytest.raises(AnsibleLookupError, match="No file was found when using first_found."):
        lookup_module.run(terms, variables, **kwargs)

def test_run_skip(lookup_module, monkeypatch):
    terms = ['testfile1', 'testfile2']
    variables = {'ansible_search_path': ['/some/path']}
    kwargs = {}

    # Mocking _process_terms to return specific values with skip=True
    monkeypatch.setattr(lookup_module, '_process_terms', lambda terms, variables, kwargs: (['testfile1', 'testfile2'], True))
    
    # Mocking _templar.template to return the same value
    mock_templar = MagicMock()
    mock_templar.template = lambda x: x
    lookup_module._templar = mock_templar

    # Mocking find_file_in_search_path to return None for both files
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', lambda variables, subdir, fn, ignore_missing: None)

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == []
