# file: lib/ansible/module_utils/connection.py:104-109
# asked: {"lines": [104, 105, 106, 107, 109], "branches": []}
# gained: {"lines": [104, 105, 106, 107, 109], "branches": []}

import pytest
import uuid
from ansible.module_utils.connection import request_builder

def test_request_builder(mocker):
    # Mock uuid.uuid4 to return a fixed value
    mock_uuid = mocker.patch('uuid.uuid4', return_value=uuid.UUID('12345678123456781234567812345678'))
    
    method = 'test_method'
    args = (1, 2, 3)
    kwargs = {'key': 'value'}
    
    expected_reqid = '12345678-1234-5678-1234-567812345678'
    expected_request = {
        'jsonrpc': '2.0',
        'method': method,
        'id': expected_reqid,
        'params': (args, kwargs)
    }
    
    # Call the function
    result = request_builder(method, *args, **kwargs)
    
    # Assertions
    assert result == expected_request
    mock_uuid.assert_called_once()

