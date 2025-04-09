# file: lib/ansible/plugins/lookup/first_found.py:206-236
# asked: {"lines": [208, 215, 217, 218, 220, 221, 222, 223, 226, 229, 230, 233, 235, 236], "branches": [[218, 220], [218, 233], [229, 218], [229, 230], [233, 235], [233, 236]]}
# gained: {"lines": [208, 215, 217, 218, 220, 221, 222, 223, 226, 229, 230, 233, 235, 236], "branches": [[218, 220], [218, 233], [229, 218], [229, 230], [233, 235], [233, 236]]}

import pytest
from ansible.plugins.lookup.first_found import LookupModule
from ansible.errors import AnsibleLookupError, AnsibleUndefinedVariable
from jinja2 import UndefinedError

@pytest.fixture
def lookup_module():
    module = LookupModule()
    module._templar = MockTemplar()
    return module

class MockTemplar:
    def template(self, fn):
        return fn

def test_run_all_paths_found(monkeypatch, lookup_module):
    terms = ['file1', 'file2']
    variables = {}
    kwargs = {}

    def mock_process_terms(terms, variables, kwargs):
        return (['file1', 'file2'], False)

    def mock_find_file_in_search_path(variables, subdir, fn, ignore_missing=True):
        if fn == 'file1':
            return '/path/to/file1'
        return None

    monkeypatch.setattr(lookup_module, '_process_terms', mock_process_terms)
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', mock_find_file_in_search_path)

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ['/path/to/file1']

def test_run_no_file_found_with_skip(monkeypatch, lookup_module):
    terms = ['file1', 'file2']
    variables = {}
    kwargs = {}

    def mock_process_terms(terms, variables, kwargs):
        return (['file1', 'file2'], True)

    def mock_find_file_in_search_path(variables, subdir, fn, ignore_missing=True):
        return None

    monkeypatch.setattr(lookup_module, '_process_terms', mock_process_terms)
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', mock_find_file_in_search_path)

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == []

def test_run_no_file_found_without_skip(monkeypatch, lookup_module):
    terms = ['file1', 'file2']
    variables = {}
    kwargs = {}

    def mock_process_terms(terms, variables, kwargs):
        return (['file1', 'file2'], False)

    def mock_find_file_in_search_path(variables, subdir, fn, ignore_missing=True):
        return None

    monkeypatch.setattr(lookup_module, '_process_terms', mock_process_terms)
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', mock_find_file_in_search_path)

    with pytest.raises(AnsibleLookupError, match="No file was found when using first_found."):
        lookup_module.run(terms, variables, **kwargs)

def test_run_template_error(monkeypatch, lookup_module):
    terms = ['file1', 'file2']
    variables = {}
    kwargs = {}

    def mock_process_terms(terms, variables, kwargs):
        return (['file1', 'file2'], False)

    class MockTemplar:
        def template(self, fn):
            raise AnsibleUndefinedVariable()

    templar = MockTemplar()
    lookup_module._templar = templar

    def mock_find_file_in_search_path(variables, subdir, fn, ignore_missing=True):
        return None

    monkeypatch.setattr(lookup_module, '_process_terms', mock_process_terms)
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', mock_find_file_in_search_path)

    with pytest.raises(AnsibleLookupError, match="No file was found when using first_found."):
        lookup_module.run(terms, variables, **kwargs)
