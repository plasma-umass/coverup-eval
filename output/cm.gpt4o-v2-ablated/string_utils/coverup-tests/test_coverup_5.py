# file: string_utils/manipulation.py:357-379
# asked: {"lines": [357, 369, 370, 373, 376, 379], "branches": [[369, 370], [369, 373]]}
# gained: {"lines": [357, 369, 370, 373, 376, 379], "branches": [[369, 370], [369, 373]]}

import pytest
import random
from string_utils.manipulation import shuffle, InvalidInputError, is_string

def test_shuffle_valid_string(monkeypatch):
    input_string = "hello world"
    
    def mock_shuffle(lst):
        lst[:] = ['l', ' ', 'w', 'o', 'd', 'h', 'e', 'o', 'r', 'l', 'l']
    
    monkeypatch.setattr(random, 'shuffle', mock_shuffle)
    result = shuffle(input_string)
    assert result == "l wodheorll"
    assert sorted(result) == sorted(input_string)

def test_shuffle_empty_string(monkeypatch):
    input_string = ""
    
    def mock_shuffle(lst):
        lst[:] = []
    
    monkeypatch.setattr(random, 'shuffle', mock_shuffle)
    result = shuffle(input_string)
    assert result == ""
    assert sorted(result) == sorted(input_string)

def test_shuffle_invalid_input():
    with pytest.raises(InvalidInputError):
        shuffle(12345)

def test_shuffle_non_string_input():
    with pytest.raises(InvalidInputError):
        shuffle(None)
