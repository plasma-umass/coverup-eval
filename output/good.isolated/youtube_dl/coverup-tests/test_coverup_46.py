# file youtube_dl/aes.py:126-144
# lines [134, 136, 137, 138, 139, 140, 141, 142, 144]
# branches ['137->138', '137->144', '140->141', '140->142']

import pytest
from youtube_dl.aes import aes_encrypt

# Constants for the test
BLOCK_SIZE_BYTES = 16

@pytest.fixture
def expanded_key_192():
    # 192-bit key (24 bytes) expanded to 208 bytes (13 rounds)
    return [i for i in range(208)]

@pytest.fixture
def expanded_key_256():
    # 256-bit key (32 bytes) expanded to 240 bytes (15 rounds)
    return [i for i in range(240)]

def test_aes_encrypt_with_192_bit_key(expanded_key_192):
    data = [i for i in range(BLOCK_SIZE_BYTES)]
    encrypted_data = aes_encrypt(data, expanded_key_192)
    assert len(encrypted_data) == BLOCK_SIZE_BYTES
    # Add more assertions here to verify the correctness of the encryption if necessary

def test_aes_encrypt_with_256_bit_key(expanded_key_256):
    data = [i for i in range(BLOCK_SIZE_BYTES)]
    encrypted_data = aes_encrypt(data, expanded_key_256)
    assert len(encrypted_data) == BLOCK_SIZE_BYTES
    # Add more assertions here to verify the correctness of the encryption if necessary
