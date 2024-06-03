# file youtube_dl/aes.py:281-282
# lines [282]
# branches []

import pytest
from youtube_dl.aes import sub_bytes

# Mock SBOX for testing purposes
SBOX = list(range(256))

@pytest.fixture
def mock_sbox(mocker):
    mocker.patch('youtube_dl.aes.SBOX', SBOX)

def test_sub_bytes(mock_sbox):
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_output = [SBOX[x] for x in data]
    result = sub_bytes(data)
    assert result == expected_output
