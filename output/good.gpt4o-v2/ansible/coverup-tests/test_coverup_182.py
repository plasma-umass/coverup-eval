# file: lib/ansible/plugins/lookup/unvault.py:41-63
# asked: {"lines": [41, 43, 45, 47, 49, 50, 53, 54, 55, 56, 57, 58, 59, 61, 63], "branches": [[49, 50], [49, 63], [55, 56], [55, 61]]}
# gained: {"lines": [41, 43, 45, 47, 49, 50, 53, 54, 55, 56, 57, 58, 59, 61, 63], "branches": [[49, 50], [49, 63], [55, 56], [55, 61]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.lookup.unvault import LookupModule
from ansible.module_utils._text import to_text
from unittest.mock import patch, mock_open, MagicMock

@pytest.fixture
def lookup_module():
    return LookupModule(loader=MagicMock())

def test_run_success(lookup_module, monkeypatch):
    terms = ['testfile']
    variables = {}

    def mock_set_options(var_options=None, direct=None):
        pass

    def mock_find_file_in_search_path(variables, subdir, term):
        return '/path/to/testfile'

    def mock_get_real_file(lookupfile, decrypt=False):
        return lookupfile

    monkeypatch.setattr(lookup_module, 'set_options', mock_set_options)
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', mock_find_file_in_search_path)
    monkeypatch.setattr(lookup_module._loader, 'get_real_file', mock_get_real_file)

    with patch('builtins.open', mock_open(read_data=b'test content')) as mock_file:
        result = lookup_module.run(terms, variables)
        mock_file.assert_called_once_with('/path/to/testfile', 'rb')
        assert result == ['test content']

def test_run_file_not_found(lookup_module, monkeypatch):
    terms = ['nonexistentfile']
    variables = {}

    def mock_set_options(var_options=None, direct=None):
        pass

    def mock_find_file_in_search_path(variables, subdir, term):
        return None

    monkeypatch.setattr(lookup_module, 'set_options', mock_set_options)
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', mock_find_file_in_search_path)

    with pytest.raises(AnsibleParserError, match='Unable to find file matching "nonexistentfile"'):
        lookup_module.run(terms, variables)
