# file dataclasses_json/core.py:96-115
# lines [97, 98, 99, 100, 103, 104, 105, 106, 107, 109, 110, 112, 113, 114, 115]
# branches ['98->99', '98->115', '99->100', '99->112', '103->104', '103->105', '112->113', '112->114']

import pytest
from dataclasses_json.core import _encode_overrides, _encode_json_type

@pytest.fixture
def cleanup_overrides():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_encode_overrides_with_exclusion_and_encoder(cleanup_overrides, mocker):
    # Mock the _encode_json_type function to ensure it is called
    mock_encode_json_type = mocker.patch('dataclasses_json.core._encode_json_type', side_effect=lambda x: x)

    # Define a sample exclusion function and encoder
    def exclude_if_negative(value):
        return value < 0

    def encode_to_string(value):
        return str(value)

    # Define the overrides dictionary with exclusion and encoder
    overrides = {
        'positive_key': mocker.Mock(exclude=None, letter_case=None, encoder=None),
        'negative_key': mocker.Mock(exclude=exclude_if_negative, letter_case=None, encoder=None),
        'encoded_key': mocker.Mock(exclude=None, letter_case=None, encoder=encode_to_string),
    }

    # Define the key-value pairs to be encoded
    kvs = {
        'positive_key': 42,
        'negative_key': -1,
        'encoded_key': 100,
    }

    # Call the function with encode_json set to True
    result = _encode_overrides(kvs, overrides, encode_json=True)

    # Assert that the negative_key is excluded
    assert 'negative_key' not in result

    # Assert that the encoded_key is encoded using the encoder
    assert result['encoded_key'] == '100'

    # Assert that the positive_key is not modified
    assert result['positive_key'] == 42

    # Assert that the _encode_json_type function was called for each key
    assert mock_encode_json_type.call_count == 2

    # Cleanup is handled by the cleanup_overrides fixture
