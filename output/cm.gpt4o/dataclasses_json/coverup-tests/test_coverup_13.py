# file dataclasses_json/core.py:96-115
# lines [96, 97, 98, 99, 100, 103, 104, 105, 106, 107, 109, 110, 112, 113, 114, 115]
# branches ['98->99', '98->115', '99->100', '99->112', '103->104', '103->105', '112->113', '112->114']

import pytest
from unittest.mock import Mock

# Assuming _encode_json_type is a function in the same module
from dataclasses_json.core import _encode_overrides, _encode_json_type

def test_encode_overrides(mocker):
    # Mocking _encode_json_type
    mock_encode_json_type = mocker.patch('dataclasses_json.core._encode_json_type', side_effect=lambda x: f"encoded_{x}")

    # Test data
    kvs = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }

    # Mocking overrides
    overrides = {
        'key1': Mock(exclude=lambda x: False, letter_case=str.upper, encoder=lambda x: f"encoded_{x}"),
        'key2': Mock(exclude=lambda x: True, letter_case=None, encoder=None),
        'key3': Mock(exclude=lambda x: False, letter_case=None, encoder=None)
    }

    # Call the function with encode_json=True
    result = _encode_overrides(kvs, overrides, encode_json=True)

    # Assertions
    assert result == {
        'KEY1': 'encoded_encoded_value1',
        'key3': 'encoded_value3'
    }

    # Verify that _encode_json_type was called correctly
    mock_encode_json_type.assert_any_call('encoded_value1')
    mock_encode_json_type.assert_any_call('value3')
    assert mock_encode_json_type.call_count == 2

    # Clean up
    mocker.stopall()
