# file: lib/ansible/module_utils/connection.py:104-109
# asked: {"lines": [104, 105, 106, 107, 109], "branches": []}
# gained: {"lines": [104, 105, 106, 107, 109], "branches": []}

import pytest
import uuid
from ansible.module_utils.connection import request_builder

def test_request_builder(monkeypatch):
    # Mock uuid4 to return a fixed value
    class MockUUID:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

    mock_uuid = MockUUID("1234-5678-9012")
    monkeypatch.setattr(uuid, "uuid4", lambda: mock_uuid)

    # Test with no args and no kwargs
    req = request_builder("test_method")
    assert req == {
        'jsonrpc': '2.0',
        'method': 'test_method',
        'id': '1234-5678-9012',
        'params': ((), {})
    }

    # Test with args
    req = request_builder("test_method", 1, 2, 3)
    assert req == {
        'jsonrpc': '2.0',
        'method': 'test_method',
        'id': '1234-5678-9012',
        'params': ((1, 2, 3), {})
    }

    # Test with kwargs
    req = request_builder("test_method", key1="value1", key2="value2")
    assert req == {
        'jsonrpc': '2.0',
        'method': 'test_method',
        'id': '1234-5678-9012',
        'params': ((), {'key1': 'value1', 'key2': 'value2'})
    }

    # Test with both args and kwargs
    req = request_builder("test_method", 1, 2, key1="value1", key2="value2")
    assert req == {
        'jsonrpc': '2.0',
        'method': 'test_method',
        'id': '1234-5678-9012',
        'params': ((1, 2), {'key1': 'value1', 'key2': 'value2'})
    }
