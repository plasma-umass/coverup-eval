# file tornado/util.py:66-73
# lines [66, 67]
# branches []

import pytest
from tornado.util import TimeoutError

def test_timeout_error():
    try:
        raise TimeoutError("Timeout occurred")
    except TimeoutError as e:
        assert str(e) == "Timeout occurred"
