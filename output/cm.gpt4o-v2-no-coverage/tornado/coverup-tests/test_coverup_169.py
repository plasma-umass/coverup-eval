# file: tornado/escape.py:214-216
# asked: {"lines": [214, 215, 216], "branches": []}
# gained: {"lines": [214, 215], "branches": []}

import pytest
from tornado.escape import to_unicode

def test_to_unicode_none():
    assert to_unicode(None) is None
