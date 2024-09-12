# file: lib/ansible/module_utils/connection.py:104-109
# asked: {"lines": [104, 105, 106, 107, 109], "branches": []}
# gained: {"lines": [104, 105, 106, 107, 109], "branches": []}

import pytest
import uuid
from ansible.module_utils.connection import request_builder

def test_request_builder(monkeypatch):
    def mock_uuid4():
        return uuid.UUID('12345678123456781234567812345678')
    
    monkeypatch.setattr(uuid, 'uuid4', mock_uuid4)
    
    method = 'test_method'
    args = ('arg1', 'arg2')
    kwargs = {'key1': 'value1', 'key2': 'value2'}
    
    expected_reqid = '12345678-1234-5678-1234-567812345678'
    expected_req = {
        'jsonrpc': '2.0',
        'method': method,
        'id': expected_reqid,
        'params': (args, kwargs)
    }
    
    req = request_builder(method, *args, **kwargs)
    
    assert req == expected_req
