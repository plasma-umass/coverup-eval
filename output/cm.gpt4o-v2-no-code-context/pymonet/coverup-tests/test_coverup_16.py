# file: pymonet/monad_try.py:79-90
# asked: {"lines": [79, 88, 89, 90], "branches": [[88, 89], [88, 90]]}
# gained: {"lines": [79, 88, 89, 90], "branches": [[88, 89], [88, 90]]}

import pytest
from pymonet.monad_try import Try

def test_try_on_fail_success(monkeypatch):
    class MockTry(Try):
        def __init__(self, is_success, value):
            self.is_success = is_success
            self.value = value

    def mock_fail_callback(value):
        assert value == "failure_value"

    try_instance = MockTry(is_success=False, value="failure_value")
    result = try_instance.on_fail(mock_fail_callback)
    assert result == try_instance

def test_try_on_fail_no_fail(monkeypatch):
    class MockTry(Try):
        def __init__(self, is_success, value):
            self.is_success = is_success
            self.value = value

    def mock_fail_callback(value):
        pytest.fail("fail_callback should not be called")

    try_instance = MockTry(is_success=True, value="success_value")
    result = try_instance.on_fail(mock_fail_callback)
    assert result == try_instance
