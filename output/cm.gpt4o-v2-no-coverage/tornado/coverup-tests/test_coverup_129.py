# file: tornado/escape.py:106-108
# asked: {"lines": [106, 107, 108], "branches": []}
# gained: {"lines": [106, 107], "branches": []}

import pytest
from tornado.escape import url_unescape

def test_url_unescape_bytes():
    result = url_unescape(b'hello%20world', encoding=None, plus=True)
    assert result == b'hello world'

def test_url_unescape_str():
    result = url_unescape('hello%20world', encoding=None, plus=True)
    assert result == b'hello world'

def test_url_unescape_plus():
    result = url_unescape('hello+world', encoding=None, plus=True)
    assert result == b'hello world'

def test_url_unescape_no_plus():
    result = url_unescape('hello+world', encoding=None, plus=False)
    assert result == b'hello+world'
