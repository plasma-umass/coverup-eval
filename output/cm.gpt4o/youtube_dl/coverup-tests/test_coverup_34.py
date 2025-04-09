# file youtube_dl/aes.py:330-331
# lines [331]
# branches []

import pytest
from youtube_dl.aes import mix_columns_inv, mix_columns, MIX_COLUMN_MATRIX_INV

def test_mix_columns_inv(mocker):
    # Mock the mix_columns function to ensure it is called with the correct parameters
    mock_mix_columns = mocker.patch('youtube_dl.aes.mix_columns', return_value='mocked_result')
    
    data = b'\x00' * 16  # Example data, adjust as necessary for your test case
    result = mix_columns_inv(data)
    
    # Verify that mix_columns was called with the correct parameters
    mock_mix_columns.assert_called_once_with(data, MIX_COLUMN_MATRIX_INV)
    
    # Verify the result is as expected
    assert result == 'mocked_result'
