# file: tornado/escape.py:111-115
# asked: {"lines": [111, 112, 113, 115], "branches": []}
# gained: {"lines": [111, 112, 113], "branches": []}

import pytest
from tornado.escape import url_unescape

@pytest.mark.parametrize("value, encoding, plus, expected", [
    ("hello%20world", "utf-8", True, "hello world"),
    ("hello+world", "utf-8", True, "hello world"),
    ("hello%2Bworld", "utf-8", True, "hello+world"),
    ("hello%2Bworld", "utf-8", False, "hello+world"),
    (b"hello%20world", "utf-8", True, "hello world"),
    (b"hello+world", "utf-8", True, "hello world"),
    (b"hello%2Bworld", "utf-8", True, "hello+world"),
    (b"hello%2Bworld", "utf-8", False, "hello+world"),
])
def test_url_unescape(value, encoding, plus, expected):
    result = url_unescape(value, encoding, plus)
    assert result == expected
