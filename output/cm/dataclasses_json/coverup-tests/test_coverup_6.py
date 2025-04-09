# file dataclasses_json/core.py:283-292
# lines [283, 290, 291, 292]
# branches []

import pytest
from dataclasses_json.core import _decode_dict_keys
from typing import Any

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Cleanup if necessary

def test_decode_dict_keys_with_none_and_any_key_types(cleanup, mocker):
    # Mocking _decode_items to control its behavior
    mocker.patch('dataclasses_json.core._decode_items', return_value=['1', '2', '3'])

    # Test with key_type as None
    result_none = list(_decode_dict_keys(None, {}, False))
    assert result_none == ['1', '2', '3'], "Decoding with None key_type failed"

    # Test with key_type as Any
    result_any = list(_decode_dict_keys(Any, {}, False))
    assert result_any == ['1', '2', '3'], "Decoding with Any key_type failed"
