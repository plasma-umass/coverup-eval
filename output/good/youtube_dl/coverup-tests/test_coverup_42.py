# file youtube_dl/aes.py:37-60
# lines [46, 47, 49, 50, 51, 52, 53, 55, 56, 57, 58, 60]
# branches ['51->52', '51->58']

import pytest
from youtube_dl.aes import aes_cbc_decrypt, BLOCK_SIZE_BYTES

@pytest.fixture
def aes_cbc_decrypt_data():
    # Fixture to provide data, key, and iv for the test
    data = [0] * (BLOCK_SIZE_BYTES + 1)  # One more than BLOCK_SIZE to ensure two blocks
    key = [0] * BLOCK_SIZE_BYTES  # 16-byte key for AES-128
    iv = [0] * BLOCK_SIZE_BYTES  # 16-byte IV
    return data, key, iv

def test_aes_cbc_decrypt(aes_cbc_decrypt_data):
    data, key, iv = aes_cbc_decrypt_data
    decrypted_data = aes_cbc_decrypt(data, key, iv)
    
    # Assertions to verify postconditions
    assert isinstance(decrypted_data, list), "Decrypted data should be a list"
    assert len(decrypted_data) == len(data), "Decrypted data should be the same length as input data"
    assert all(isinstance(x, int) for x in decrypted_data), "Decrypted data should contain integers"
    assert decrypted_data != data, "Decrypted data should not be the same as the input data when using zero key and iv"
