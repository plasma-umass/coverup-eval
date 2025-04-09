# file: lib/ansible/plugins/lookup/unvault.py:41-63
# asked: {"lines": [41, 43, 45, 47, 49, 50, 53, 54, 55, 56, 57, 58, 59, 61, 63], "branches": [[49, 50], [49, 63], [55, 56], [55, 61]]}
# gained: {"lines": [41, 43, 45, 47, 49, 50, 53, 54, 55, 56, 57, 58, 59, 61, 63], "branches": [[49, 50], [49, 63], [55, 56], [55, 61]]}

import pytest
from unittest.mock import patch, mock_open, MagicMock
from ansible.errors import AnsibleParserError
from ansible.plugins.lookup.unvault import LookupModule
from ansible.module_utils._text import to_text

@pytest.fixture
def lookup_module():
    loader = MagicMock()
    return LookupModule(loader=loader)

def test_run_success(lookup_module, monkeypatch):
    terms = ['testfile']
    variables = {}
    kwargs = {}

    # Mock methods
    monkeypatch.setattr(lookup_module, 'set_options', lambda var_options, direct: None)
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', lambda variables, subdir, term: '/path/to/testfile')
    monkeypatch.setattr(lookup_module._loader, 'get_real_file', lambda path, decrypt: path)

    # Mock file content
    mock_file_content = b'Test content'
    with patch('builtins.open', mock_open(read_data=mock_file_content)) as mock_file:
        result = lookup_module.run(terms, variables, **kwargs)
        mock_file.assert_called_once_with('/path/to/testfile', 'rb')
        assert result == [to_text(mock_file_content)]

def test_run_file_not_found(lookup_module, monkeypatch):
    terms = ['nonexistentfile']
    variables = {}
    kwargs = {}

    # Mock methods
    monkeypatch.setattr(lookup_module, 'set_options', lambda var_options, direct: None)
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', lambda variables, subdir, term: None)

    with pytest.raises(AnsibleParserError, match='Unable to find file matching "nonexistentfile"'):
        lookup_module.run(terms, variables, **kwargs)
