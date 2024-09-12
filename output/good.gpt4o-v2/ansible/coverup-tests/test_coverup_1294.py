# file: lib/ansible/utils/jsonrpc.py:75-76
# asked: {"lines": [76], "branches": []}
# gained: {"lines": [76], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

def test_register():
    server = JsonRpcServer()
    obj = object()
    
    # Register the object
    server.register(obj)
    
    # Assert the object is in the _objects set
    assert obj in server._objects

    # Clean up
    server._objects.remove(obj)
    assert obj not in server._objects
