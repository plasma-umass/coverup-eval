# file: httpie/core.py:234-247
# asked: {"lines": [234, 243, 244, 245, 246], "branches": []}
# gained: {"lines": [234, 243, 244, 245, 246], "branches": []}

import pytest
from httpie.core import decode_raw_args

def test_decode_raw_args():
    # Test with a mix of str and bytes
    args = ['test', b'test_bytes']
    stdin_encoding = 'utf-8'
    expected = ['test', 'test_bytes']
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected

    # Test with only bytes
    args = [b'test_bytes1', b'test_bytes2']
    expected = ['test_bytes1', 'test_bytes2']
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected

    # Test with only str
    args = ['test1', 'test2']
    expected = ['test1', 'test2']
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected

    # Test with empty list
    args = []
    expected = []
    result = decode_raw_args(args, stdin_encoding)
    assert result == expected
