# file: string_utils/manipulation.py:598-608
# asked: {"lines": [598, 608], "branches": []}
# gained: {"lines": [598, 608], "branches": []}

import pytest
from string_utils.manipulation import decompress, compress

def test_decompress():
    original_string = "This is a test string to compress and decompress."
    compressed_string = compress(original_string)
    decompressed_string = decompress(compressed_string)
    
    assert decompressed_string == original_string

