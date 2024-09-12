# file: lib/ansible/utils/jsonrpc.py:100-101
# asked: {"lines": [100, 101], "branches": []}
# gained: {"lines": [100, 101], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    return JsonRpcServer()

def test_parse_error(json_rpc_server, mocker):
    mock_error = mocker.patch.object(json_rpc_server, 'error', return_value='mocked_error')
    result = json_rpc_server.parse_error(data='test_data')
    mock_error.assert_called_once_with(-32700, 'Parse error', 'test_data')
    assert result == 'mocked_error'
