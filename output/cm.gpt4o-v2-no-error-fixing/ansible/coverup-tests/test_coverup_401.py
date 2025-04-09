# file: lib/ansible/module_utils/urls.py:1230-1233
# asked: {"lines": [1230, 1231, 1232, 1233], "branches": [[1231, 1232], [1231, 1233]]}
# gained: {"lines": [1230, 1231, 1232, 1233], "branches": [[1231, 1232], [1231, 1233]]}

import pytest
from ansible.module_utils.urls import Request

def test_fallback_with_none():
    req = Request()
    assert req._fallback(None, 'fallback_value') == 'fallback_value'

def test_fallback_with_value():
    req = Request()
    assert req._fallback('actual_value', 'fallback_value') == 'actual_value'
