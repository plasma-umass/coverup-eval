# file tornado/escape.py:118-144
# lines [118, 119, 137, 138, 140, 141, 143, 144]
# branches ['137->138', '137->143', '138->140', '138->141']

import pytest
from tornado.escape import url_unescape
from urllib.parse import quote_plus, quote

@pytest.mark.parametrize("input_string,encoding,plus,expected", [
    ("hello+world%21", "utf-8", True, "hello world!"),
    ("hello+world%21", "utf-8", False, "hello+world!"),
    ("hello%20world%21", None, True, b"hello world!"),
    ("hello+world%21", None, True, b"hello world!"),
    ("hello+world%21", None, False, b"hello+world!"),
])
def test_url_unescape(input_string, encoding, plus, expected):
    assert url_unescape(input_string, encoding, plus) == expected

@pytest.mark.parametrize("input_string,encoding,plus,expected", [
    (quote_plus("hello world!"), "utf-8", True, "hello world!"),
    (quote("hello+world!"), "utf-8", False, "hello+world!"),
    (quote_plus("hello world!"), None, True, b"hello world!"),
    (quote("hello+world!"), None, False, b"hello+world!"),
])
def test_url_unescape_with_quoting(input_string, encoding, plus, expected):
    assert url_unescape(input_string, encoding, plus) == expected
