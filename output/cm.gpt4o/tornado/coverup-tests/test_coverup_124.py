# file tornado/escape.py:214-216
# lines [214, 215, 216]
# branches []

import pytest
from tornado.escape import to_unicode

def test_to_unicode_none():
    result = to_unicode(None)
    assert result is None
