# file: tornado/escape.py:118-144
# asked: {"lines": [118, 119, 137, 138, 140, 141, 143, 144], "branches": [[137, 138], [137, 143], [138, 140], [138, 141]]}
# gained: {"lines": [118, 119, 137, 138, 140, 141, 143, 144], "branches": [[137, 138], [137, 143], [138, 140], [138, 141]]}

import pytest
from tornado.escape import url_unescape

def test_url_unescape_bytes_no_encoding_plus():
    value = b'hello+world'
    result = url_unescape(value, encoding=None, plus=True)
    assert result == b'hello world'

def test_url_unescape_bytes_no_encoding_no_plus():
    value = b'hello%20world'
    result = url_unescape(value, encoding=None, plus=False)
    assert result == b'hello world'

def test_url_unescape_str_with_encoding_plus():
    value = 'hello+world'
    result = url_unescape(value, encoding='utf-8', plus=True)
    assert result == 'hello world'

def test_url_unescape_str_with_encoding_no_plus():
    value = 'hello%20world'
    result = url_unescape(value, encoding='utf-8', plus=False)
    assert result == 'hello world'
