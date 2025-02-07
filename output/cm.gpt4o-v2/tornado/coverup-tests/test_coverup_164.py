# file: tornado/util.py:66-73
# asked: {"lines": [66, 67], "branches": []}
# gained: {"lines": [66, 67], "branches": []}

import pytest
from tornado.util import TimeoutError

def test_timeout_error():
    with pytest.raises(TimeoutError):
        raise TimeoutError("This is a timeout error")

