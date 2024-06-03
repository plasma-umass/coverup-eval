# file lib/ansible/utils/jsonrpc.py:75-76
# lines [76]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    server = JsonRpcServer()
    server._objects = set()  # Initialize the _objects attribute
    yield server
    server._objects.clear()  # Clean up after the test

def test_register_adds_object(json_rpc_server):
    obj = object()
    json_rpc_server.register(obj)
    assert obj in json_rpc_server._objects
