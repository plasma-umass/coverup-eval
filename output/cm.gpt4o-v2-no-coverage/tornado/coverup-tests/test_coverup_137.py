# file: tornado/util.py:66-73
# asked: {"lines": [66, 67], "branches": []}
# gained: {"lines": [66, 67], "branches": []}

import pytest
from tornado.util import TimeoutError

def test_timeout_error_inheritance():
    with pytest.raises(TimeoutError):
        raise TimeoutError("Test message")

    assert issubclass(TimeoutError, Exception)
