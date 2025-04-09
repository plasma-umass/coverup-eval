# file tornado/util.py:441-454
# lines [441, 450, 451, 452, 453, 454]
# branches ['452->453', '452->454']

import pytest
from tornado.util import _websocket_mask_python

def test_websocket_mask_python():
    # Test with non-empty mask and data
    mask = b'\x01\x02\x03\x04'
    data = b'Hello, World!'
    expected_masked_data = bytes(b ^ mask[i % 4] for i, b in enumerate(data))
    masked_data = _websocket_mask_python(mask, data)
    assert masked_data == expected_masked_data

    # Test with empty data
    data_empty = b''
    expected_masked_data_empty = b''
    masked_data_empty = _websocket_mask_python(mask, data_empty)
    assert masked_data_empty == expected_masked_data_empty

    # Test with empty mask (should not alter data)
    mask_empty = b'\x00\x00\x00\x00'
    expected_masked_data_no_mask = data
    masked_data_no_mask = _websocket_mask_python(mask_empty, data)
    assert masked_data_no_mask == expected_masked_data_no_mask

    # Test with mask and data of same length (4 bytes)
    data_same_length = b'test'
    expected_masked_data_same_length = bytes(b ^ mask[i % 4] for i, b in enumerate(data_same_length))
    masked_data_same_length = _websocket_mask_python(mask, data_same_length)
    assert masked_data_same_length == expected_masked_data_same_length

    # Test with longer data than mask
    long_data = b'Longer data string for testing'
    expected_masked_long_data = bytes(b ^ mask[i % 4] for i, b in enumerate(long_data))
    masked_long_data = _websocket_mask_python(mask, long_data)
    assert masked_long_data == expected_masked_long_data

# No top-level code is included as per the instructions.
