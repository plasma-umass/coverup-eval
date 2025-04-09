# file: youtube_dl/aes.py:311-319
# asked: {"lines": [311, 312, 313, 314, 315, 317, 318, 319], "branches": [[313, 314], [313, 319], [315, 317], [315, 318]]}
# gained: {"lines": [311, 312, 313, 314, 315, 317, 318, 319], "branches": [[313, 314], [313, 319], [315, 317], [315, 318]]}

import pytest
from youtube_dl.aes import mix_column, rijndael_mul

def test_mix_column():
    data = [0x57, 0x83, 0x1a, 0xc6]
    matrix = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]
    
    expected_output = [
        rijndael_mul(0x57, 0x02) ^ rijndael_mul(0x83, 0x03) ^ rijndael_mul(0x1a, 0x01) ^ rijndael_mul(0xc6, 0x01),
        rijndael_mul(0x57, 0x01) ^ rijndael_mul(0x83, 0x02) ^ rijndael_mul(0x1a, 0x03) ^ rijndael_mul(0xc6, 0x01),
        rijndael_mul(0x57, 0x01) ^ rijndael_mul(0x83, 0x01) ^ rijndael_mul(0x1a, 0x02) ^ rijndael_mul(0xc6, 0x03),
        rijndael_mul(0x57, 0x03) ^ rijndael_mul(0x83, 0x01) ^ rijndael_mul(0x1a, 0x01) ^ rijndael_mul(0xc6, 0x02)
    ]
    
    result = mix_column(data, matrix)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
