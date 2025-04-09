# file lib/ansible/utils/vars.py:185-210
# lines [185, 186, 187, 188, 189, 190, 191, 193, 195, 196, 197, 198, 200, 203, 205, 206, 208, 210]
# branches ['187->188', '187->210', '190->191', '190->193', '193->195', '193->196', '196->197', '196->198', '198->200', '198->203', '205->206', '205->208']

import pytest
from unittest.mock import MagicMock, patch
from ansible.utils.vars import load_extra_vars
from ansible.errors import AnsibleOptionsError
from collections.abc import MutableMapping

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_context(mocker):
    return mocker.patch('ansible.utils.vars.context', autospec=True)

def test_load_extra_vars_empty(mock_loader, mock_context):
    mock_context.CLIARGS = {'extra_vars': ()}
    result = load_extra_vars(mock_loader)
    assert result == {}

def test_load_extra_vars_file(mock_loader, mock_context):
    mock_context.CLIARGS = {'extra_vars': ('@file.yml',)}
    mock_loader.load_from_file.return_value = {'key': 'value'}
    result = load_extra_vars(mock_loader)
    assert result == {'key': 'value'}
    mock_loader.load_from_file.assert_called_once_with('file.yml')

def test_load_extra_vars_invalid_file(mock_loader, mock_context):
    mock_context.CLIARGS = {'extra_vars': ('/file.yml',)}
    with pytest.raises(AnsibleOptionsError, match="Please prepend extra_vars filename '/file.yml' with '@'"):
        load_extra_vars(mock_loader)

def test_load_extra_vars_yaml(mock_loader, mock_context):
    mock_context.CLIARGS = {'extra_vars': ('{"key": "value"}',)}
    mock_loader.load.return_value = {'key': 'value'}
    result = load_extra_vars(mock_loader)
    assert result == {'key': 'value'}
    mock_loader.load.assert_called_once_with('{"key": "value"}')

def test_load_extra_vars_kv(mock_loader, mock_context):
    mock_context.CLIARGS = {'extra_vars': ('key=value',)}
    with patch('ansible.utils.vars.parse_kv', return_value={'key': 'value'}) as mock_parse_kv:
        result = load_extra_vars(mock_loader)
        assert result == {'key': 'value'}
        mock_parse_kv.assert_called_once_with('key=value')

def test_load_extra_vars_invalid_data(mock_loader, mock_context):
    mock_context.CLIARGS = {'extra_vars': ('key=value',)}
    with patch('ansible.utils.vars.parse_kv', return_value='invalid_data'):
        with pytest.raises(AnsibleOptionsError, match="Invalid extra vars data supplied. 'key=value' could not be made into a dictionary"):
            load_extra_vars(mock_loader)
