# file: tornado/escape.py:118-144
# asked: {"lines": [118, 119, 137, 138, 140, 141, 143, 144], "branches": [[137, 138], [137, 143], [138, 140], [138, 141]]}
# gained: {"lines": [118, 119, 137, 138, 140, 141, 143, 144], "branches": [[137, 138], [137, 143], [138, 140], [138, 141]]}

import pytest
import urllib.parse
from tornado.escape import url_unescape

def test_url_unescape_bytes_with_plus():
    value = b'hello+world'
    result = url_unescape(value, encoding=None, plus=True)
    assert result == b'hello world'

def test_url_unescape_bytes_without_plus():
    value = b'hello%20world'
    result = url_unescape(value, encoding=None, plus=False)
    assert result == b'hello world'

def test_url_unescape_str_with_plus():
    value = 'hello+world'
    result = url_unescape(value, encoding='utf-8', plus=True)
    assert result == 'hello world'

def test_url_unescape_str_without_plus():
    value = 'hello%20world'
    result = url_unescape(value, encoding='utf-8', plus=False)
    assert result == 'hello world'

def test_url_unescape_str_with_plus_and_special_chars():
    value = 'hello+world%21'
    result = url_unescape(value, encoding='utf-8', plus=True)
    assert result == 'hello world!'

def test_url_unescape_str_without_plus_and_special_chars():
    value = 'hello%20world%21'
    result = url_unescape(value, encoding='utf-8', plus=False)
    assert result == 'hello world!'

def test_url_unescape_bytes_with_plus_and_special_chars():
    value = b'hello+world%21'
    result = url_unescape(value, encoding=None, plus=True)
    assert result == b'hello world!'

def test_url_unescape_bytes_without_plus_and_special_chars():
    value = b'hello%20world%21'
    result = url_unescape(value, encoding=None, plus=False)
    assert result == b'hello world!'
