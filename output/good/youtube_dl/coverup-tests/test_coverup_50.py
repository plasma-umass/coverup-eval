# file youtube_dl/aes.py:147-165
# lines [155, 157, 158, 159, 160, 161, 162, 163, 165]
# branches ['157->158', '157->163', '159->160', '159->161']

import pytest
from youtube_dl.aes import aes_decrypt

# Assuming BLOCK_SIZE_BYTES is defined in the module
BLOCK_SIZE_BYTES = 16

@pytest.fixture
def expanded_key_192():
    # 192-bit key (expanded to 208 bytes for 13 rounds)
    return [0] * 208

def test_aes_decrypt_rounds_coverage(expanded_key_192):
    # Create a 16-byte cipher data block
    data = [0] * BLOCK_SIZE_BYTES
    # Decrypt using a 192-bit key, which should trigger the missing coverage
    decrypted_data = aes_decrypt(data, expanded_key_192)
    # Assert postconditions here if applicable
    # For example, if the function is supposed to return the original data
    # when decrypting with an all-zero key and data, uncomment the following line:
    # assert decrypted_data == data
