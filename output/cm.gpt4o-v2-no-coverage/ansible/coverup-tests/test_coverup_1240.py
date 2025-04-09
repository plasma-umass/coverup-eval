# file: lib/ansible/plugins/filter/core.py:464-465
# asked: {"lines": [465], "branches": []}
# gained: {"lines": [465], "branches": []}

import pytest
import base64
from ansible.plugins.filter.core import b64decode

def test_b64decode_valid_string():
    encoded_str = "SGVsbG8gV29ybGQh"
    decoded_str = b64decode(encoded_str)
    assert decoded_str == "Hello World!"

def test_b64decode_invalid_string():
    with pytest.raises(Exception):
        b64decode("Invalid base64 string")

def test_b64decode_with_encoding():
    encoded_str = "w6nDpMOtw6w="
    decoded_bytes = base64.b64decode(encoded_str)
    decoded_str = b64decode(encoded_str, encoding='latin-1')
    assert decoded_str == decoded_bytes.decode('latin-1')

def test_b64decode_empty_string():
    decoded_str = b64decode("")
    assert decoded_str == ""

def test_b64decode_non_utf8_encoding():
    encoded_str = "w6nDpMOtw6w="
    decoded_bytes = base64.b64decode(encoded_str)
    decoded_str = b64decode(encoded_str, encoding='latin-1')
    assert decoded_str == decoded_bytes.decode('latin-1')
