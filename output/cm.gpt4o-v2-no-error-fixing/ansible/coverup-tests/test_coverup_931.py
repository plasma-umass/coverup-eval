# file: lib/ansible/utils/jsonrpc.py:75-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    return JsonRpcServer()

def test_register_adds_object(json_rpc_server):
    obj = object()
    json_rpc_server.register(obj)
    assert obj in json_rpc_server._objects

def test_register_does_not_add_duplicate(json_rpc_server):
    obj = object()
    json_rpc_server.register(obj)
    json_rpc_server.register(obj)
    assert list(json_rpc_server._objects).count(obj) == 1
