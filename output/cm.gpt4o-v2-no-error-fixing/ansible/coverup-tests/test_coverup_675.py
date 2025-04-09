# file: lib/ansible/module_utils/urls.py:1662-1666
# asked: {"lines": [1662, 1666], "branches": []}
# gained: {"lines": [1662, 1666], "branches": []}

import pytest
from ansible.module_utils.urls import basic_auth_header

def test_basic_auth_header():
    username = "user"
    password = "pass"
    expected = b"Basic dXNlcjpwYXNz"  # base64.b64encode(b"user:pass") = b"dXNlcjpwYXNz"
    
    result = basic_auth_header(username, password)
    
    assert result == expected

