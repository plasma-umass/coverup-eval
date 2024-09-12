# file: string_utils/manipulation.py:357-379
# asked: {"lines": [357, 369, 370, 373, 376, 379], "branches": [[369, 370], [369, 373]]}
# gained: {"lines": [357, 369, 370, 373, 376, 379], "branches": [[369, 370], [369, 373]]}

import pytest
from string_utils.manipulation import shuffle
from string_utils.errors import InvalidInputError

def test_shuffle_valid_string():
    input_string = "hello world"
    result = shuffle(input_string)
    assert sorted(result) == sorted(input_string)
    assert result != input_string  # There's a very small chance this could fail if the shuffle returns the same order

def test_shuffle_empty_string():
    input_string = ""
    result = shuffle(input_string)
    assert result == input_string

def test_shuffle_invalid_input():
    with pytest.raises(InvalidInputError) as excinfo:
        shuffle(12345)
    assert str(excinfo.value) == 'Expected "str", received "int"'
