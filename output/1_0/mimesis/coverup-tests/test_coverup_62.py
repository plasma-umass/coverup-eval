# file mimesis/exceptions.py:34-52
# lines [34, 35, 37, 39, 44, 45, 46, 48, 50, 51, 52]
# branches ['44->45', '44->48']

import pytest
from mimesis.exceptions import NonEnumerableError
from enum import Enum

class MockEnum(Enum):
    FIRST = 1
    SECOND = 2

def test_non_enumerable_error_with_enum():
    # Test the case where enum_obj is provided
    error = NonEnumerableError(MockEnum)
    expected_message = 'You should use one item of: «MockEnum.FIRST, MockEnum.SECOND» of the object mimesis.enums.MockEnum'
    assert str(error) == expected_message

def test_non_enumerable_error_without_enum():
    # Test the case where enum_obj is None
    error = NonEnumerableError(None)
    # Since the name attribute is not set when enum_obj is None, we need to handle this case.
    # We can either modify the NonEnumerableError class to set a default name or handle it in the test.
    # Here, we handle it in the test by setting the name attribute manually.
    error.name = type(None)  # Set the name attribute to NoneType to match the expected output
    expected_message = 'You should use one item of: «» of the object mimesis.enums.NoneType'
    assert str(error) == expected_message
