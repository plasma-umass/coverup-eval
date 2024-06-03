# file youtube_dl/aes.py:301-302
# lines [302]
# branches []

import pytest
from youtube_dl.aes import xor

def test_xor():
    data1 = [0b10101010, 0b11001100, 0b11110000]
    data2 = [0b01010101, 0b00110011, 0b00001111]
    expected_result = [0b11111111, 0b11111111, 0b11111111]
    
    result = xor(data1, data2)
    
    assert result == expected_result, f"Expected {expected_result}, but got {result}"
