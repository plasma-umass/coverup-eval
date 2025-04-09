# file dataclasses_json/core.py:283-292
# lines [291]
# branches []

import pytest
from dataclasses_json.core import _decode_dict_keys
from typing import Any

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Cleanup code if necessary

def test_decode_dict_keys_with_non_none_and_non_any_key_types(cleanup, mocker):
    # Mocking _decode_items to simply return the values it receives
    mocker.patch('dataclasses_json.core._decode_items', side_effect=lambda kt, xs, im: xs)
    
    # Test with int as key_type
    keys = ['1', '2', '3']
    result = list(_decode_dict_keys(int, keys, False))
    assert result == [1, 2, 3], "Decoding with int key_type should convert strings to integers"
