# file: lib/ansible/module_utils/connection.py:112-117
# asked: {"lines": [112, 114, 115, 116, 117], "branches": [[116, 0], [116, 117]]}
# gained: {"lines": [112, 114, 115, 116, 117], "branches": [[116, 0], [116, 117]]}

import pytest
from ansible.module_utils.connection import ConnectionError

def test_connection_error_initialization():
    message = "Test error message"
    kwargs = {'code': 500, 'reason': 'Internal Server Error'}
    
    error = ConnectionError(message, **kwargs)
    
    assert str(error) == message
    assert error.code == 500
    assert error.reason == 'Internal Server Error'
