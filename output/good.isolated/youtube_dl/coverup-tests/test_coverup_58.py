# file youtube_dl/aes.py:285-286
# lines [286]
# branches []

import pytest
from youtube_dl.aes import sub_bytes_inv, SBOX_INV

def test_sub_bytes_inv():
    # Setup: Define the expected inverse of the SBOX
    expected_inv_sbox = [SBOX_INV[x] for x in range(256)]

    # Exercise: Apply the sub_bytes_inv function to a range of byte values
    result = sub_bytes_inv(list(range(256)))

    # Verify: Check if the result matches the expected inverse SBOX
    assert result == expected_inv_sbox, "The inverse SBOX does not match the expected values"

    # Cleanup: Nothing to clean up in this test as no external resources are modified
