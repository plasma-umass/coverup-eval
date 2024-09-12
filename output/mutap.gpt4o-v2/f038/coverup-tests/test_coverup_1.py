# file: f038/__init__.py:10-12
# asked: {"lines": [10, 12], "branches": []}
# gained: {"lines": [10, 12], "branches": []}

import pytest
from f038 import decode_cyclic, encode_cyclic

def test_decode_cyclic():
    # Test with a simple string
    original_string = "abcdef"
    encoded_once = encode_cyclic(original_string)
    decoded_string = decode_cyclic(encoded_once)
    
    # Ensure the decoded string matches the original
    assert decoded_string == original_string

    # Test with an empty string
    original_string = ""
    decoded_string = decode_cyclic(original_string)
    
    # Ensure the decoded string matches the original
    assert decoded_string == original_string

    # Test with a string of length 1
    original_string = "a"
    decoded_string = decode_cyclic(original_string)
    
    # Ensure the decoded string matches the original
    assert decoded_string == original_string

    # Test with a string of length 2
    original_string = "ab"
    decoded_string = decode_cyclic(original_string)
    
    # Ensure the decoded string matches the original
    assert decoded_string == original_string
