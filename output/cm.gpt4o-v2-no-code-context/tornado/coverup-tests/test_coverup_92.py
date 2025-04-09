# file: tornado/escape.py:111-115
# asked: {"lines": [111, 112, 113, 115], "branches": []}
# gained: {"lines": [111, 112, 113], "branches": []}

import pytest
from tornado.escape import url_unescape

def test_url_unescape_str():
    result = url_unescape("hello%20world", encoding="utf-8", plus=True)
    assert result == "hello world"

def test_url_unescape_bytes():
    result = url_unescape(b"hello%20world", encoding="utf-8", plus=True)
    assert result == "hello world"

def test_url_unescape_plus():
    result = url_unescape("hello+world", encoding="utf-8", plus=True)
    assert result == "hello world"

def test_url_unescape_no_plus():
    result = url_unescape("hello+world", encoding="utf-8", plus=False)
    assert result == "hello+world"
