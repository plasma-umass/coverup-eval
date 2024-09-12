# file: lib/ansible/plugins/filter/core.py:464-465
# asked: {"lines": [464, 465], "branches": []}
# gained: {"lines": [464, 465], "branches": []}

import pytest
import base64
from ansible.module_utils._text import to_bytes, to_text
from ansible.plugins.filter.core import b64decode

def test_b64decode_valid_string():
    encoded_str = base64.b64encode(b"hello world").decode('utf-8')
    decoded_str = b64decode(encoded_str)
    assert decoded_str == "hello world"

def test_b64decode_invalid_string():
    invalid_str = "invalid_base64"
    with pytest.raises(Exception):
        b64decode(invalid_str)

def test_b64decode_with_encoding():
    encoded_str = base64.b64encode("你好，世界".encode('utf-8')).decode('utf-8')
    decoded_str = b64decode(encoded_str, encoding='utf-8')
    assert decoded_str == "你好，世界"
