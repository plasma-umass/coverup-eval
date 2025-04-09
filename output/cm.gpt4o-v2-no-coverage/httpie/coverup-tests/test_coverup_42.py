# file: httpie/core.py:234-247
# asked: {"lines": [234, 243, 244, 245, 246], "branches": []}
# gained: {"lines": [234, 243, 244, 245, 246], "branches": []}

import pytest

from httpie.core import decode_raw_args

def test_decode_raw_args_with_bytes():
    args = [b'hello', b'world']
    stdin_encoding = 'utf-8'
    expected = ['hello', 'world']
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected

def test_decode_raw_args_with_str():
    args = ['hello', 'world']
    stdin_encoding = 'utf-8'
    expected = ['hello', 'world']
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected

def test_decode_raw_args_with_mixed():
    args = [b'hello', 'world']
    stdin_encoding = 'utf-8'
    expected = ['hello', 'world']
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected

def test_decode_raw_args_with_different_encoding():
    args = [b'hello', b'world']
    stdin_encoding = 'latin-1'
    expected = ['hello', 'world']
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected
