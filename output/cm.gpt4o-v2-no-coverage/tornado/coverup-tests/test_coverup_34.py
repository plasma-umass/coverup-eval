# file: tornado/escape.py:118-144
# asked: {"lines": [118, 119, 137, 138, 140, 141, 143, 144], "branches": [[137, 138], [137, 143], [138, 140], [138, 141]]}
# gained: {"lines": [118, 119, 137, 138, 140, 141, 143, 144], "branches": [[137, 138], [137, 143], [138, 140], [138, 141]]}

import pytest
from tornado.escape import url_unescape

def test_url_unescape_bytes_encoding_none_plus_true():
    result = url_unescape(b'abc+def', encoding=None, plus=True)
    assert result == b'abc def'

def test_url_unescape_bytes_encoding_none_plus_false():
    result = url_unescape(b'abc%20def', encoding=None, plus=False)
    assert result == b'abc def'

def test_url_unescape_str_encoding_utf8_plus_true():
    result = url_unescape('abc+def', encoding='utf-8', plus=True)
    assert result == 'abc def'

def test_url_unescape_str_encoding_utf8_plus_false():
    result = url_unescape('abc%20def', encoding='utf-8', plus=False)
    assert result == 'abc def'

def test_url_unescape_str_encoding_none_plus_true():
    result = url_unescape('abc+def', encoding=None, plus=True)
    assert result == b'abc def'

def test_url_unescape_str_encoding_none_plus_false():
    result = url_unescape('abc%20def', encoding=None, plus=False)
    assert result == b'abc def'
