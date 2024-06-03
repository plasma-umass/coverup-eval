# file httpie/core.py:234-247
# lines [234, 243, 244, 245, 246]
# branches []

import pytest
from httpie.core import decode_raw_args

def test_decode_raw_args():
    # Test with a mix of str and bytes
    args = ['arg1', b'arg2', 'arg3', b'arg4']
    stdin_encoding = 'utf-8'
    expected = ['arg1', 'arg2', 'arg3', 'arg4']
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected

    # Test with only bytes
    args = [b'arg1', b'arg2']
    expected = ['arg1', 'arg2']
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected

    # Test with only str
    args = ['arg1', 'arg2']
    expected = ['arg1', 'arg2']
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected

    # Test with different encoding
    args = [b'\xe4\xbd\xa0\xe5\xa5\xbd']  # "你好" in utf-8
    stdin_encoding = 'utf-8'
    expected = ['你好']
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected

    # Test with empty list
    args = []
    expected = []
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected
