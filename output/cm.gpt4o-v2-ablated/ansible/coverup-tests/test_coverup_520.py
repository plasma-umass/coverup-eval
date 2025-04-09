# file: lib/ansible/plugins/filter/core.py:464-465
# asked: {"lines": [465], "branches": []}
# gained: {"lines": [465], "branches": []}

import base64
import pytest
from ansible.plugins.filter.core import b64decode

def test_b64decode_valid_string():
    encoded_str = base64.b64encode(b'hello world').decode('utf-8')
    decoded_str = b64decode(encoded_str)
    assert decoded_str == 'hello world'

def test_b64decode_invalid_string():
    with pytest.raises(Exception):
        b64decode('invalid_base64')

def test_b64decode_with_different_encoding():
    encoded_str = base64.b64encode('こんにちは'.encode('utf-8')).decode('utf-8')
    decoded_str = b64decode(encoded_str, encoding='utf-8')
    assert decoded_str == 'こんにちは'
