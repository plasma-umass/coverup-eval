# file: httpie/core.py:234-247
# asked: {"lines": [234, 243, 244, 245, 246], "branches": []}
# gained: {"lines": [234, 243, 244, 245, 246], "branches": []}

import pytest

from httpie.core import decode_raw_args

def test_decode_raw_args_with_bytes(monkeypatch):
    args = [b'hello', b'world']
    stdin_encoding = 'utf-8'
    result = decode_raw_args(args, stdin_encoding)
    assert result == ['hello', 'world']

def test_decode_raw_args_with_str(monkeypatch):
    args = ['hello', 'world']
    stdin_encoding = 'utf-8'
    result = decode_raw_args(args, stdin_encoding)
    assert result == ['hello', 'world']

def test_decode_raw_args_mixed(monkeypatch):
    args = [b'hello', 'world']
    stdin_encoding = 'utf-8'
    result = decode_raw_args(args, stdin_encoding)
    assert result == ['hello', 'world']

def test_decode_raw_args_different_encoding(monkeypatch):
    args = [b'hello', b'world']
    stdin_encoding = 'ascii'
    result = decode_raw_args(args, stdin_encoding)
    assert result == ['hello', 'world']
