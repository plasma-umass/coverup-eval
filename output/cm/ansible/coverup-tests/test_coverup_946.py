# file lib/ansible/utils/jsonrpc.py:78-79
# lines [78, 79]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    server = JsonRpcServer()
    server._identifier = 1  # Mock the identifier for the test
    yield server

def test_json_rpc_server_header(json_rpc_server):
    expected_header = {'jsonrpc': '2.0', 'id': 1}
    assert json_rpc_server.header() == expected_header, "The header does not match the expected output"
