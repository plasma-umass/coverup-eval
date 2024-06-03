# file lib/ansible/utils/jsonrpc.py:19-22
# lines [19, 21]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

def test_jsonrpcserver_objects():
    # Ensure the _objects set is initially empty
    assert len(JsonRpcServer._objects) == 0

    # Add an object to the _objects set
    obj = object()
    JsonRpcServer._objects.add(obj)
    assert obj in JsonRpcServer._objects

    # Remove the object from the _objects set
    JsonRpcServer._objects.remove(obj)
    assert obj not in JsonRpcServer._objects

    # Clean up to ensure no side effects for other tests
    JsonRpcServer._objects.clear()
    assert len(JsonRpcServer._objects) == 0
