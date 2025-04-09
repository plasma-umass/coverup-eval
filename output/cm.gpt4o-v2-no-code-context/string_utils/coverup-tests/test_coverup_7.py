# file: string_utils/manipulation.py:357-379
# asked: {"lines": [357, 369, 370, 373, 376, 379], "branches": [[369, 370], [369, 373]]}
# gained: {"lines": [357, 369, 370, 373, 376, 379], "branches": [[369, 370], [369, 373]]}

import pytest
from string_utils.manipulation import shuffle, InvalidInputError
from string_utils.validation import is_string
import random

def test_shuffle_valid_string(monkeypatch):
    input_string = "hello world"
    
    def mock_shuffle(lst):
        lst[:] = ['l', ' ', 'w', 'o', 'd', 'h', 'e', 'o', 'r', 'l', 'l']
    
    monkeypatch.setattr(random, 'shuffle', mock_shuffle)
    
    result = shuffle(input_string)
    assert result == "l wodheorll"
    assert sorted(result) == sorted(input_string)

def test_shuffle_invalid_input():
    with pytest.raises(InvalidInputError):
        shuffle(12345)

def test_shuffle_empty_string():
    result = shuffle("")
    assert result == ""

def test_shuffle_single_character():
    result = shuffle("a")
    assert result == "a"
