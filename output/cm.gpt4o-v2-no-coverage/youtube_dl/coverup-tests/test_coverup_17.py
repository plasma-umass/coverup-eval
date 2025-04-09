# file: youtube_dl/aes.py:285-286
# asked: {"lines": [286], "branches": []}
# gained: {"lines": [286], "branches": []}

import pytest
from youtube_dl.aes import sub_bytes_inv, SBOX_INV

def test_sub_bytes_inv():
    data = [0, 1, 2, 3, 255]
    expected_output = [SBOX_INV[0], SBOX_INV[1], SBOX_INV[2], SBOX_INV[3], SBOX_INV[255]]
    assert sub_bytes_inv(data) == expected_output

    # Test with empty data
    data = []
    expected_output = []
    assert sub_bytes_inv(data) == expected_output

    # Test with maximum value in data
    data = [255]
    expected_output = [SBOX_INV[255]]
    assert sub_bytes_inv(data) == expected_output

    # Test with repeated values
    data = [1, 1, 1]
    expected_output = [SBOX_INV[1], SBOX_INV[1], SBOX_INV[1]]
    assert sub_bytes_inv(data) == expected_output
