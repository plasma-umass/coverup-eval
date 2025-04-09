# file: lib/ansible/utils/vars.py:185-210
# asked: {"lines": [185, 186, 187, 188, 189, 190, 191, 193, 195, 196, 197, 198, 200, 203, 205, 206, 208, 210], "branches": [[187, 188], [187, 210], [190, 191], [190, 193], [193, 195], [193, 196], [196, 197], [196, 198], [198, 200], [198, 203], [205, 206], [205, 208]]}
# gained: {"lines": [185, 186, 187, 188, 189, 190, 193, 195, 196, 197, 198, 200, 203, 205, 206, 208, 210], "branches": [[187, 188], [187, 210], [190, 193], [193, 195], [193, 196], [196, 197], [196, 198], [198, 200], [198, 203], [205, 206], [205, 208]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleOptionsError
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.parsing.splitter import parse_kv
from ansible.utils.vars import load_extra_vars

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_context(mocker):
    return mocker.patch('ansible.context.CLIARGS', {})

def test_load_extra_vars_empty(mock_loader, mock_context):
    mock_context['extra_vars'] = []
    result = load_extra_vars(mock_loader)
    assert result == {}

def test_load_extra_vars_yaml_file(mock_loader, mock_context):
    mock_context['extra_vars'] = ['@/path/to/file']
    mock_loader.load_from_file.return_value = {'key': 'value'}
    result = load_extra_vars(mock_loader)
    assert result == {'key': 'value'}
    mock_loader.load_from_file.assert_called_once_with('/path/to/file')

def test_load_extra_vars_invalid_filename(mock_loader, mock_context):
    mock_context['extra_vars'] = ['/invalid/path']
    with pytest.raises(AnsibleOptionsError, match="Please prepend extra_vars filename '/invalid/path' with '@'"):
        load_extra_vars(mock_loader)

def test_load_extra_vars_yaml_data(mock_loader, mock_context):
    mock_context['extra_vars'] = ['{"key": "value"}']
    mock_loader.load.return_value = {'key': 'value'}
    result = load_extra_vars(mock_loader)
    assert result == {'key': 'value'}
    mock_loader.load.assert_called_once_with('{"key": "value"}')

def test_load_extra_vars_kv_data(mock_loader, mock_context):
    mock_context['extra_vars'] = ['key=value']
    with patch('ansible.utils.vars.parse_kv', return_value={'key': 'value'}) as mock_parse_kv:
        result = load_extra_vars(mock_loader)
        assert result == {'key': 'value'}
        mock_parse_kv.assert_called_once_with('key=value')

def test_load_extra_vars_invalid_data(mock_loader, mock_context):
    mock_context['extra_vars'] = ['key=value']
    with patch('ansible.utils.vars.parse_kv', return_value='invalid_data'):
        with pytest.raises(AnsibleOptionsError, match="Invalid extra vars data supplied. 'key=value' could not be made into a dictionary"):
            load_extra_vars(mock_loader)
