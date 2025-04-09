# file: youtube_dl/aes.py:330-331
# asked: {"lines": [331], "branches": []}
# gained: {"lines": [331], "branches": []}

import pytest
from youtube_dl.aes import mix_columns_inv, mix_columns, MIX_COLUMN_MATRIX_INV

def test_mix_columns_inv():
    data = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F]
    expected_output = mix_columns(data, MIX_COLUMN_MATRIX_INV)
    
    result = mix_columns_inv(data)
    
    assert result == expected_output
