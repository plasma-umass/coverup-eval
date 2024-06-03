# file lib/ansible/module_utils/connection.py:104-109
# lines [105, 106, 107, 109]
# branches []

import pytest
import uuid
from unittest.mock import patch
from ansible.module_utils.connection import request_builder

def test_request_builder(mocker):
    mock_uuid = mocker.patch('uuid.uuid4', return_value=uuid.UUID('12345678123456781234567812345678'))
    
    method_ = 'test_method'
    args = ('arg1', 'arg2')
    kwargs = {'key1': 'value1', 'key2': 'value2'}
    
    expected_reqid = '12345678-1234-5678-1234-567812345678'
    expected_req = {
        'jsonrpc': '2.0',
        'method': method_,
        'id': expected_reqid,
        'params': (args, kwargs)
    }
    
    req = request_builder(method_, *args, **kwargs)
    
    assert req['id'] == expected_reqid
    assert req == expected_req
