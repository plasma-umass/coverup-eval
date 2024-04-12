# file lib/ansible/module_utils/urls.py:1662-1666
# lines [1662, 1666]
# branches []

import base64
import pytest
from ansible.module_utils.urls import basic_auth_header

def test_basic_auth_header():
    username = 'user'
    password = 'pass'
    expected_auth = b'Basic ' + base64.b64encode(f"{username}:{password}".encode('utf-8'))
    
    auth_header = basic_auth_header(username, password)
    
    assert auth_header == expected_auth, "The generated basic auth header does not match the expected value."
