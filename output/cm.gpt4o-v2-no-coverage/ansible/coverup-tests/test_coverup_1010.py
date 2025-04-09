# file: lib/ansible/module_utils/urls.py:1662-1666
# asked: {"lines": [1662, 1666], "branches": []}
# gained: {"lines": [1662, 1666], "branches": []}

import pytest
import base64
from ansible.module_utils._text import to_bytes
from ansible.module_utils.urls import basic_auth_header

def test_basic_auth_header():
    username = "user"
    password = "pass"
    expected = b"Basic " + base64.b64encode(to_bytes(f"{username}:{password}", errors='surrogate_or_strict'))
    assert basic_auth_header(username, password) == expected

    # Test with empty username and password
    username = ""
    password = ""
    expected = b"Basic " + base64.b64encode(to_bytes(f"{username}:{password}", errors='surrogate_or_strict'))
    assert basic_auth_header(username, password) == expected

    # Test with special characters
    username = "user!@#"
    password = "pass$%^"
    expected = b"Basic " + base64.b64encode(to_bytes(f"{username}:{password}", errors='surrogate_or_strict'))
    assert basic_auth_header(username, password) == expected

    # Test with non-ASCII characters
    username = "usér"
    password = "päss"
    expected = b"Basic " + base64.b64encode(to_bytes(f"{username}:{password}", errors='surrogate_or_strict'))
    assert basic_auth_header(username, password) == expected
