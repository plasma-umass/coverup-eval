# file: tornado/escape.py:111-115
# asked: {"lines": [111, 112, 113, 115], "branches": []}
# gained: {"lines": [111, 112, 113], "branches": []}

import pytest
from tornado.escape import url_unescape

def test_url_unescape_overload_str():
    # This test is to cover the overload where encoding is a string
    result = url_unescape("test%20string", encoding="utf-8", plus=True)
    assert result == "test string"

def test_url_unescape_overload_bytes():
    # This test is to cover the overload where encoding is None
    result = url_unescape(b"test%20string", encoding=None, plus=True)
    assert result == b"test string"
