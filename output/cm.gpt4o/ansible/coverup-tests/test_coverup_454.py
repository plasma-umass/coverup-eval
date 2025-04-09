# file lib/ansible/module_utils/connection.py:184-202
# lines [184, 194, 196, 197, 198, 199, 200, 202]
# branches ['196->197', '196->202']

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_text

class TestConnection:
    @patch.object(Connection, '_exec_jsonrpc')
    def test_rpc_success(self, mock_exec_jsonrpc):
        # Mock the response to simulate a successful RPC call
        mock_exec_jsonrpc.return_value = {'result': 'success'}

        conn = Connection(socket_path='dummy_path')
        result = conn.__rpc__('test_method', 'arg1', 'arg2', key='value')

        assert result == 'success'
        mock_exec_jsonrpc.assert_called_once_with('test_method', 'arg1', 'arg2', key='value')

    @patch.object(Connection, '_exec_jsonrpc')
    def test_rpc_error(self, mock_exec_jsonrpc):
        # Mock the response to simulate an error in the RPC call
        mock_exec_jsonrpc.return_value = {
            'error': {
                'message': 'An error occurred',
                'code': 123,
                'data': 'Error data'
            }
        }

        conn = Connection(socket_path='dummy_path')

        with pytest.raises(ConnectionError) as excinfo:
            conn.__rpc__('test_method', 'arg1', 'arg2', key='value')

        assert str(excinfo.value) == to_text('Error data', errors='surrogate_then_replace')
        assert excinfo.value.code == 123
        mock_exec_jsonrpc.assert_called_once_with('test_method', 'arg1', 'arg2', key='value')
