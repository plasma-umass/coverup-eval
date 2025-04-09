# file: lib/ansible/module_utils/urls.py:1230-1233
# asked: {"lines": [1230, 1231, 1232, 1233], "branches": [[1231, 1232], [1231, 1233]]}
# gained: {"lines": [1230, 1231, 1232, 1233], "branches": [[1231, 1232], [1231, 1233]]}

import pytest
from ansible.module_utils.urls import Request

class TestRequest:
    def test_fallback_with_none_value(self):
        req = Request()
        assert req._fallback(None, 'fallback_value') == 'fallback_value'

    def test_fallback_with_non_none_value(self):
        req = Request()
        assert req._fallback('value', 'fallback_value') == 'value'
