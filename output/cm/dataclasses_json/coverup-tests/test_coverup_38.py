# file dataclasses_json/core.py:90-93
# lines [91, 92, 93]
# branches ['91->92', '91->93']

import pytest
from dataclasses_json.core import _ExtendedEncoder, Json
from unittest.mock import Mock
from typing import Union

# Assuming the Json type is a Union or similar that can be mocked
# to have __args__ attribute for the purpose of this test.

@pytest.fixture
def mock_json_type(mocker):
    Json.__args__ = (int, str)  # Mocking as if Json.__args__ is (int, str)
    yield
    del Json.__args__  # Clean up after the test

def test_encode_json_type_with_json_args(mock_json_type):
    # Test to cover lines 91-93
    from dataclasses_json.core import _encode_json_type

    # Mocking a value that is an instance of Json.__args__
    value = 42  # int is part of the mocked Json.__args__

    # Call the function with the mocked value
    result = _encode_json_type(value)

    # Assert the result is the same as the value, meaning it was returned directly
    assert result == value

def test_encode_json_type_with_non_json_args(mock_json_type):
    # Test to cover lines 91-93
    from dataclasses_json.core import _encode_json_type

    # Mocking a value that is NOT an instance of Json.__args__
    value = 42.0  # float is not part of Json.__args__

    # Mocking the default function to return a specific value
    default_mock = Mock()
    default_mock.return_value = 'default_value'

    # Call the function with the mocked value and default function
    result = _encode_json_type(value, default=default_mock)

    # Assert the default function was called with the value
    default_mock.assert_called_once_with(value)

    # Assert the result is what the default function returned
    assert result == 'default_value'
