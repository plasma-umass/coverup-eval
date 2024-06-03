# file lib/ansible/plugins/lookup/unvault.py:41-63
# lines [41, 43, 45, 47, 49, 50, 53, 54, 55, 56, 57, 58, 59, 61, 63]
# branches ['49->50', '49->63', '55->56', '55->61']

import pytest
from unittest.mock import patch, mock_open, MagicMock
from ansible.plugins.lookup.unvault import LookupModule
from ansible.errors import AnsibleParserError

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_run_success(lookup_module, mocker):
    terms = ['testfile']
    variables = {'files': '/path/to/files'}
    kwargs = {}

    mocker.patch.object(lookup_module, 'set_options')
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value='/path/to/files/testfile')
    
    # Mock the _loader attribute and its get_real_file method
    mock_loader = mocker.patch.object(lookup_module, '_loader', autospec=True)
    mock_loader.get_real_file.return_value = '/path/to/files/testfile'
    
    mock_open_obj = mock_open(read_data=b'secret data')
    mocker.patch('builtins.open', mock_open_obj)

    result = lookup_module.run(terms, variables, **kwargs)

    lookup_module.set_options.assert_called_once_with(var_options=variables, direct=kwargs)
    lookup_module.find_file_in_search_path.assert_called_once_with(variables, 'files', 'testfile')
    mock_loader.get_real_file.assert_called_once_with('/path/to/files/testfile', decrypt=True)
    mock_open_obj.assert_called_once_with('/path/to/files/testfile', 'rb')
    assert result == ['secret data']

def test_run_file_not_found(lookup_module, mocker):
    terms = ['nonexistentfile']
    variables = {'files': '/path/to/files'}
    kwargs = {}

    mocker.patch.object(lookup_module, 'set_options')
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value=None)

    with pytest.raises(AnsibleParserError, match='Unable to find file matching "nonexistentfile"'):
        lookup_module.run(terms, variables, **kwargs)

    lookup_module.set_options.assert_called_once_with(var_options=variables, direct=kwargs)
    lookup_module.find_file_in_search_path.assert_called_once_with(variables, 'files', 'nonexistentfile')
