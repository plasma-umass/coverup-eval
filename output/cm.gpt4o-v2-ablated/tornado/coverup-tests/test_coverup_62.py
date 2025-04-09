# file: tornado/escape.py:183-185
# asked: {"lines": [183, 184, 185], "branches": []}
# gained: {"lines": [183, 184], "branches": []}

import pytest
from tornado.escape import utf8

def test_utf8_none():
    result = utf8(None)
    assert result is None
