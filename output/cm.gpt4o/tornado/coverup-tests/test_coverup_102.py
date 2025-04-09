# file tornado/escape.py:111-115
# lines [111, 112, 113, 115]
# branches []

import pytest
from tornado.escape import url_unescape

def test_url_unescape_overload():
    # Test with string input
    result = url_unescape("hello%20world", encoding="utf-8", plus=True)
    assert result == "hello world"

    # Test with bytes input
    result = url_unescape(b"hello%20world", encoding="utf-8", plus=True)
    assert result == "hello world"

    # Test with plus=False
    result = url_unescape("hello+world", encoding="utf-8", plus=False)
    assert result == "hello+world"

    # Test with plus=True
    result = url_unescape("hello+world", encoding="utf-8", plus=True)
    assert result == "hello world"
