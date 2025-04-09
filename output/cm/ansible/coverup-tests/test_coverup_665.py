# file lib/ansible/module_utils/connection.py:104-109
# lines [104, 105, 106, 107, 109]
# branches []

import pytest
import uuid
from unittest.mock import patch
from ansible.module_utils.connection import request_builder

# Test function to cover request_builder
def test_request_builder():
    method_ = 'test_method'
    args = ('arg1', 'arg2')
    kwargs = {'key1': 'value1', 'key2': 'value2'}

    with patch('uuid.uuid4') as mock_uuid:
        mock_uuid.return_value = '1234-5678-9012-3456'
        request = request_builder(method_, *args, **kwargs)

    assert request['jsonrpc'] == '2.0'
    assert request['method'] == method_
    assert request['id'] == '1234-5678-9012-3456'
    assert request['params'] == (args, kwargs)
