# file youtube_dl/aes.py:91-123
# lines [98, 99, 100, 101, 103, 104, 105, 106, 107, 109, 110, 111, 113, 114, 115, 116, 118, 119, 120, 121, 123]
# branches ['103->104', '103->121', '109->110', '109->113', '113->114', '113->118', '118->103', '118->119']

import pytest
from youtube_dl.aes import key_expansion

BLOCK_SIZE_BYTES = 16

def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]

def key_schedule_core(word, iteration):
    # This is a stub implementation for the test
    return [((x + iteration) % 256) for x in word]

def sub_bytes(word):
    # This is a stub implementation for the test
    return [(x + 1) % 256 for x in word]

@pytest.fixture
def mock_xor(mocker):
    return mocker.patch('youtube_dl.aes.xor', side_effect=xor)

@pytest.fixture
def mock_key_schedule_core(mocker):
    return mocker.patch('youtube_dl.aes.key_schedule_core', side_effect=key_schedule_core)

@pytest.fixture
def mock_sub_bytes(mocker):
    return mocker.patch('youtube_dl.aes.sub_bytes', side_effect=sub_bytes)

def test_key_expansion_16_bytes(mock_xor, mock_key_schedule_core, mock_sub_bytes):
    key = [0x00] * 16
    expanded_key = key_expansion(key)
    assert len(expanded_key) == 176
    assert mock_xor.call_count > 0
    assert mock_key_schedule_core.call_count > 0
    assert mock_sub_bytes.call_count == 0  # Should not be called for 16-byte keys

def test_key_expansion_24_bytes(mock_xor, mock_key_schedule_core, mock_sub_bytes):
    key = [0x00] * 24
    expanded_key = key_expansion(key)
    assert len(expanded_key) == 208
    assert mock_xor.call_count > 0
    assert mock_key_schedule_core.call_count > 0
    assert mock_sub_bytes.call_count == 0  # Should not be called for 24-byte keys

def test_key_expansion_32_bytes(mock_xor, mock_key_schedule_core, mock_sub_bytes):
    key = [0x00] * 32
    expanded_key = key_expansion(key)
    assert len(expanded_key) == 240
    assert mock_xor.call_count > 0
    assert mock_key_schedule_core.call_count > 0
    assert mock_sub_bytes.call_count > 0  # Should be called for 32-byte keys
