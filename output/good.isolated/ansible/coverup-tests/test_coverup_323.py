# file lib/ansible/utils/jsonrpc.py:81-89
# lines [81, 82, 83, 84, 85, 86, 87, 88, 89]
# branches ['83->84', '83->85', '85->86', '85->88']

import pytest
from ansible.utils.jsonrpc import JsonRpcServer
from ansible.module_utils._text import to_bytes, to_text
import pickle

# Assuming binary_type and text_type are defined as follows for Python 3 compatibility:
binary_type = bytes
text_type = str

class MockJsonRpcServer(JsonRpcServer):
    def header(self):
        return {'jsonrpc': '2.0', 'id': 1}

@pytest.fixture
def json_rpc_server():
    return MockJsonRpcServer()

def test_response_with_binary_type(json_rpc_server):
    binary_data = to_bytes('binary data')
    response = json_rpc_server.response(binary_data)
    assert response['result'] == to_text(binary_data)
    assert 'result_type' not in response

def test_response_with_non_text_non_binary_type(json_rpc_server):
    non_text_data = {'key': 'value'}
    response = json_rpc_server.response(non_text_data)
    assert response['result_type'] == 'pickle'
    assert response['result'] == to_text(pickle.dumps(non_text_data, protocol=0))
