# file dataclasses_json/core.py:96-115
# lines []
# branches ['99->112', '112->114']

import pytest
from unittest.mock import Mock

# Assuming _encode_json_type is a function in the same module
from dataclasses_json.core import _encode_overrides, _encode_json_type

def test_encode_overrides_with_encode_json(mocker):
    # Mock the _encode_json_type function
    mock_encode_json_type = mocker.patch('dataclasses_json.core._encode_json_type', side_effect=lambda x: f"encoded_{x}")

    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {
        'key1': Mock(exclude=None, letter_case=None, encoder=None),
        'key2': Mock(exclude=None, letter_case=None, encoder=None)
    }

    result = _encode_overrides(kvs, overrides, encode_json=True)

    # Assertions to verify the postconditions
    assert result == {'key1': 'encoded_value1', 'key2': 'encoded_value2'}
    mock_encode_json_type.assert_any_call('value1')
    mock_encode_json_type.assert_any_call('value2')

def test_encode_overrides_with_exclude(mocker):
    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {
        'key1': Mock(exclude=lambda x: x == 'value1', letter_case=None, encoder=None),
        'key2': Mock(exclude=None, letter_case=None, encoder=None)
    }

    result = _encode_overrides(kvs, overrides, encode_json=False)

    # Assertions to verify the postconditions
    assert result == {'key2': 'value2'}

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Cleanup code if necessary
