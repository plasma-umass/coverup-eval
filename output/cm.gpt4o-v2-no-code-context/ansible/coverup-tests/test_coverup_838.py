# file: lib/ansible/module_utils/urls.py:1662-1666
# asked: {"lines": [1662, 1666], "branches": []}
# gained: {"lines": [1662, 1666], "branches": []}

import base64
import pytest
from ansible.module_utils._text import to_bytes
from ansible.module_utils.urls import basic_auth_header

def test_basic_auth_header(monkeypatch):
    username = "user"
    password = "pass"
    expected = b"Basic " + base64.b64encode(to_bytes(f"{username}:{password}", errors='surrogate_or_strict'))
    
    result = basic_auth_header(username, password)
    
    assert result == expected
