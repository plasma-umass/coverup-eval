# file tornado/escape.py:67-75
# lines [67, 75]
# branches []

import pytest
from tornado.escape import json_encode

def test_json_encode_escapes_forward_slashes():
    # Test that json_encode escapes forward slashes correctly
    input_value = "</script>"
    expected_output = '"<\\/script>"'  # json_encode returns a JSON-encoded string
    assert json_encode(input_value) == expected_output

def test_json_encode_with_non_string_input():
    # Test that json_encode works with non-string input
    input_value = {"key": "value</script>"}
    expected_output = '{"key": "value<\\/script>"}'
    assert json_encode(input_value) == expected_output

def test_json_encode_with_no_escaping_needed():
    # Test that json_encode does not alter strings without forward slashes
    input_value = "no escaping needed"
    expected_output = '"no escaping needed"'  # json_encode returns a JSON-encoded string
    assert json_encode(input_value) == expected_output
