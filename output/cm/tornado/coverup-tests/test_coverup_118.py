# file tornado/escape.py:183-185
# lines [183, 184, 185]
# branches []

import pytest
from tornado.escape import utf8

def test_utf8_with_none():
    assert utf8(None) is None
