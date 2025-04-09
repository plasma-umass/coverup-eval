# file: lib/ansible/plugins/lookup/unvault.py:41-63
# asked: {"lines": [41, 43, 45, 47, 49, 50, 53, 54, 55, 56, 57, 58, 59, 61, 63], "branches": [[49, 50], [49, 63], [55, 56], [55, 61]]}
# gained: {"lines": [41, 43, 45, 47, 49, 50, 53, 54, 55, 56, 57, 58, 59, 61, 63], "branches": [[49, 50], [49, 63], [55, 56], [55, 61]]}

import pytest
from ansible.plugins.lookup.unvault import LookupModule
from ansible.errors import AnsibleParserError
from unittest.mock import patch, mock_open, MagicMock

@pytest.fixture
def lookup_module():
    module = LookupModule()
    module._loader = MagicMock()
    module._load_name = 'unvault'
    return module

def test_run_success(lookup_module, monkeypatch):
    terms = ['testfile']
    variables = {}
    kwargs = {}

    def mock_find_file_in_search_path(variables, subdir, term):
        return '/path/to/testfile'

    def mock_get_real_file(lookupfile, decrypt):
        return lookupfile

    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', mock_find_file_in_search_path)
    monkeypatch.setattr(lookup_module._loader, 'get_real_file', mock_get_real_file)
    monkeypatch.setattr('builtins.open', mock_open(read_data=b'test content'))

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ['test content']

def test_run_file_not_found(lookup_module, monkeypatch):
    terms = ['nonexistentfile']
    variables = {}
    kwargs = {}

    def mock_find_file_in_search_path(variables, subdir, term):
        return None

    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', mock_find_file_in_search_path)

    with pytest.raises(AnsibleParserError, match='Unable to find file matching "nonexistentfile"'):
        lookup_module.run(terms, variables, **kwargs)
