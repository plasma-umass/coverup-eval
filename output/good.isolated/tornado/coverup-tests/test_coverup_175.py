# file tornado/escape.py:78-83
# lines [78, 83]
# branches []

import pytest
from tornado.escape import json_decode

def test_json_decode_with_str_input():
    # Test with str input
    input_str = '{"key": "value"}'
    expected_output = {"key": "value"}
    assert json_decode(input_str) == expected_output

def test_json_decode_with_bytes_input():
    # Test with bytes input
    input_bytes = b'{"key": "value"}'
    expected_output = {"key": "value"}
    assert json_decode(input_bytes) == expected_output

def test_json_decode_with_invalid_input():
    # Test with invalid input that raises an exception
    with pytest.raises(ValueError):
        json_decode("not a valid json")
