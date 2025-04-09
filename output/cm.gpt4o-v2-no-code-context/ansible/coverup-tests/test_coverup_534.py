# file: lib/ansible/module_utils/urls.py:1230-1233
# asked: {"lines": [1230, 1231, 1232, 1233], "branches": [[1231, 1232], [1231, 1233]]}
# gained: {"lines": [1230, 1231, 1232, 1233], "branches": [[1231, 1232], [1231, 1233]]}

import pytest
from ansible.module_utils.urls import Request

@pytest.fixture
def request_instance():
    return Request()

def test_fallback_with_none_value(request_instance):
    result = request_instance._fallback(None, 'fallback_value')
    assert result == 'fallback_value', "Expected fallback_value when value is None"

def test_fallback_with_non_none_value(request_instance):
    result = request_instance._fallback('actual_value', 'fallback_value')
    assert result == 'actual_value', "Expected actual_value when value is not None"
