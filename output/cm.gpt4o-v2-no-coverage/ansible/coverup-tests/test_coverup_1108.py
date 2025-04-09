# file: lib/ansible/utils/vars.py:185-210
# asked: {"lines": [188, 189, 190, 191, 193, 195, 196, 197, 198, 200, 203, 205, 206, 208], "branches": [[187, 188], [190, 191], [190, 193], [193, 195], [193, 196], [196, 197], [196, 198], [198, 200], [198, 203], [205, 206], [205, 208]]}
# gained: {"lines": [188, 189, 190, 193, 195, 196, 197, 198, 200, 203, 205, 206, 208], "branches": [[187, 188], [190, 193], [193, 195], [193, 196], [196, 197], [196, 198], [198, 200], [198, 203], [205, 206], [205, 208]]}

import pytest
from unittest.mock import Mock, patch
from ansible.errors import AnsibleOptionsError
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.parsing.splitter import parse_kv
from ansible.utils.vars import load_extra_vars, combine_vars

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_context(monkeypatch):
    mock_cliargs = {'extra_vars': []}
    monkeypatch.setattr('ansible.context.CLIARGS', mock_cliargs)
    return mock_cliargs

def test_load_extra_vars_empty(mock_loader, mock_context):
    result = load_extra_vars(mock_loader)
    assert result == {}

def test_load_extra_vars_yaml_file(mock_loader, mock_context):
    mock_context['extra_vars'] = ['@/path/to/file.yml']
    mock_loader.load_from_file.return_value = {'key': 'value'}
    result = load_extra_vars(mock_loader)
    assert result == {'key': 'value'}
    mock_loader.load_from_file.assert_called_once_with('/path/to/file.yml')

def test_load_extra_vars_invalid_file_path(mock_loader, mock_context):
    mock_context['extra_vars'] = ['/path/to/file.yml']
    with pytest.raises(AnsibleOptionsError, match="Please prepend extra_vars filename '/path/to/file.yml' with '@'"):
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

def test_combine_vars_merge():
    a = {'key1': 'value1'}
    b = {'key2': 'value2'}
    with patch('ansible.utils.vars.merge_hash', return_value={'key1': 'value1', 'key2': 'value2'}) as mock_merge_hash:
        result = combine_vars(a, b, merge=True)
        assert result == {'key1': 'value1', 'key2': 'value2'}
        mock_merge_hash.assert_called_once_with(a, b)

def test_combine_vars_no_merge():
    a = {'key1': 'value1'}
    b = {'key2': 'value2'}
    result = combine_vars(a, b, merge=False)
    assert result == {'key1': 'value1', 'key2': 'value2'}
