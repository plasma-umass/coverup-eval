# file: tornado/escape.py:106-108
# asked: {"lines": [106, 107, 108], "branches": []}
# gained: {"lines": [106, 107], "branches": []}

import pytest
from tornado.escape import url_unescape

def test_url_unescape_bytes():
    # Test unescaping bytes with plus=True
    result = url_unescape(b'hello+world', encoding=None, plus=True)
    assert result == b'hello world'

    # Test unescaping bytes with plus=False
    result = url_unescape(b'hello%20world', encoding=None, plus=False)
    assert result == b'hello world'

def test_url_unescape_str():
    # Test unescaping string with plus=True
    result = url_unescape('hello+world', encoding='utf-8', plus=True)
    assert result == 'hello world'

    # Test unescaping string with plus=False
    result = url_unescape('hello%20world', encoding='utf-8', plus=False)
    assert result == 'hello world'

def test_url_unescape_invalid_encoding():
    with pytest.raises(LookupError):
        url_unescape('hello%20world', encoding='invalid-encoding', plus=False)
