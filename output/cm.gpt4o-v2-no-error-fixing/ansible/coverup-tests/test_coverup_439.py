# file: lib/ansible/module_utils/connection.py:104-109
# asked: {"lines": [104, 105, 106, 107, 109], "branches": []}
# gained: {"lines": [104, 105, 106, 107, 109], "branches": []}

import pytest
import uuid
from ansible.module_utils.connection import request_builder

def test_request_builder():
    method = "test_method"
    args = ("arg1", "arg2")
    kwargs = {"key1": "value1", "key2": "value2"}

    req = request_builder(method, *args, **kwargs)

    assert req['jsonrpc'] == '2.0'
    assert req['method'] == method
    assert 'id' in req
    assert isinstance(req['id'], str)
    assert uuid.UUID(req['id'])  # Validate UUID format
    assert req['params'] == (args, kwargs)
