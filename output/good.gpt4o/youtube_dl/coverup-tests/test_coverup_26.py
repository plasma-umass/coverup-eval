# file youtube_dl/aes.py:285-286
# lines [286]
# branches []

import pytest
from youtube_dl.aes import sub_bytes_inv

# Mock SBOX_INV for testing purposes
@pytest.fixture
def mock_sbox_inv(mocker):
    mock_sbox_inv = mocker.patch('youtube_dl.aes.SBOX_INV', new={i: 255 - i for i in range(256)})
    return mock_sbox_inv

def test_sub_bytes_inv(mock_sbox_inv):
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_output = [255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245]
    
    result = sub_bytes_inv(data)
    
    assert result == expected_output
