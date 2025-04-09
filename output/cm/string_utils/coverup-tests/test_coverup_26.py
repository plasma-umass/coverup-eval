# file string_utils/manipulation.py:357-379
# lines [357, 369, 370, 373, 376, 379]
# branches ['369->370', '369->373']

import pytest
from string_utils.manipulation import shuffle
from string_utils.errors import InvalidInputError
import random

def test_shuffle_valid_input(mocker):
    # Mock the random.shuffle method to ensure a predictable outcome
    mocker.patch('random.shuffle', lambda x: x.reverse())

    input_string = 'abcdef'
    expected_result = 'fedcba'  # Expected result if reversed due to mocked shuffle
    result = shuffle(input_string)
    assert result == expected_result, "The shuffle function did not return the expected result."

def test_shuffle_invalid_input():
    with pytest.raises(InvalidInputError):
        shuffle(123)  # Passing a non-string should raise InvalidInputError
