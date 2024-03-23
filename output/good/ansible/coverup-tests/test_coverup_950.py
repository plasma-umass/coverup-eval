# file lib/ansible/utils/jsonrpc.py:75-76
# lines [75, 76]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    return JsonRpcServer()

def test_register(json_rpc_server):
    class MockObject:
        pass

    mock_obj = MockObject()
    json_rpc_server._objects = set()  # Initialize the set to ensure a clean state
    json_rpc_server.register(mock_obj)
    assert mock_obj in json_rpc_server._objects, "Object was not registered in the JsonRpcServer"
