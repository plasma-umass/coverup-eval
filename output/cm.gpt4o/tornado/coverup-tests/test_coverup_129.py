# file tornado/escape.py:91-103
# lines [91, 102, 103]
# branches []

import pytest
from tornado.escape import url_escape

def test_url_escape():
    # Test with a string containing spaces and special characters
    value = "hello world!@#"
    escaped_value = url_escape(value)
    assert escaped_value == "hello+world%21%40%23"

    # Test with a string containing spaces and special characters, without plus
    escaped_value_no_plus = url_escape(value, plus=False)
    assert escaped_value_no_plus == "hello%20world%21%40%23"

    # Test with bytes input
    value_bytes = b"hello world!@#"
    escaped_value_bytes = url_escape(value_bytes)
    assert escaped_value_bytes == "hello+world%21%40%23"

    # Test with bytes input, without plus
    escaped_value_bytes_no_plus = url_escape(value_bytes, plus=False)
    assert escaped_value_bytes_no_plus == "hello%20world%21%40%23"

    # Test with an empty string
    empty_value = ""
    escaped_empty_value = url_escape(empty_value)
    assert escaped_empty_value == ""

    # Test with an empty string, without plus
    escaped_empty_value_no_plus = url_escape(empty_value, plus=False)
    assert escaped_empty_value_no_plus == ""

    # Test with an empty bytes
    empty_value_bytes = b""
    escaped_empty_value_bytes = url_escape(empty_value_bytes)
    assert escaped_empty_value_bytes == ""

    # Test with an empty bytes, without plus
    escaped_empty_value_bytes_no_plus = url_escape(empty_value_bytes, plus=False)
    assert escaped_empty_value_bytes_no_plus == ""
