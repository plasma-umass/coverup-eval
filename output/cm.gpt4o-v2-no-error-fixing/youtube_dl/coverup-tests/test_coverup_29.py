# file: youtube_dl/aes.py:285-286
# asked: {"lines": [286], "branches": []}
# gained: {"lines": [286], "branches": []}

import pytest
from youtube_dl.aes import sub_bytes_inv, SBOX_INV

def test_sub_bytes_inv():
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [SBOX_INV[x] for x in data]
    result = sub_bytes_inv(data)
    assert result == expected
