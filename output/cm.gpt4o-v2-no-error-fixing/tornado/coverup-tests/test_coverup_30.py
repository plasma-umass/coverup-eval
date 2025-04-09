# file: tornado/escape.py:118-144
# asked: {"lines": [118, 119, 137, 138, 140, 141, 143, 144], "branches": [[137, 138], [137, 143], [138, 140], [138, 141]]}
# gained: {"lines": [118, 119, 137, 138, 140, 141, 143, 144], "branches": [[137, 138], [137, 143], [138, 140], [138, 141]]}

import pytest
from tornado.escape import url_unescape

def test_url_unescape_with_encoding_and_plus():
    assert url_unescape("hello+world", encoding="utf-8", plus=True) == "hello world"

def test_url_unescape_with_encoding_and_no_plus():
    assert url_unescape("hello%20world", encoding="utf-8", plus=False) == "hello world"

def test_url_unescape_without_encoding_and_plus():
    assert url_unescape(b"hello+world", encoding=None, plus=True) == b"hello world"

def test_url_unescape_without_encoding_and_no_plus():
    assert url_unescape(b"hello%20world", encoding=None, plus=False) == b"hello world"
