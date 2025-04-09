# file: tornado/util.py:66-73
# asked: {"lines": [66, 67], "branches": []}
# gained: {"lines": [66, 67], "branches": []}

import pytest
from tornado.util import TimeoutError

def test_timeout_error_inheritance():
    assert issubclass(TimeoutError, Exception)

def test_timeout_error_message():
    try:
        raise TimeoutError("Test message")
    except TimeoutError as e:
        assert str(e) == "Test message"
