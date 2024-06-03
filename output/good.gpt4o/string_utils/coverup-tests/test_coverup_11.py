# file string_utils/manipulation.py:357-379
# lines [357, 369, 370, 373, 376, 379]
# branches ['369->370', '369->373']

import pytest
from string_utils.manipulation import shuffle, InvalidInputError
import random

def test_shuffle_valid_string(mocker):
    input_string = "hello world"
    mocker.patch('random.shuffle', lambda x: x.reverse())
    result = shuffle(input_string)
    assert result == "dlrow olleh"
    assert set(result) == set(input_string)
    assert len(result) == len(input_string)

def test_shuffle_invalid_input():
    with pytest.raises(InvalidInputError):
        shuffle(12345)

def test_shuffle_empty_string():
    result = shuffle("")
    assert result == ""

def test_shuffle_single_character():
    result = shuffle("a")
    assert result == "a"
