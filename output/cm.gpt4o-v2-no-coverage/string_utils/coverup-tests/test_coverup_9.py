# file: string_utils/manipulation.py:357-379
# asked: {"lines": [357, 369, 370, 373, 376, 379], "branches": [[369, 370], [369, 373]]}
# gained: {"lines": [357, 369, 370, 373, 376, 379], "branches": [[369, 370], [369, 373]]}

import pytest
from string_utils.manipulation import shuffle
from string_utils.errors import InvalidInputError

def test_shuffle_valid_string(monkeypatch):
    input_string = "hello world"
    
    def mock_shuffle(lst):
        lst[:] = list("dlrow olleh")
    
    monkeypatch.setattr("random.shuffle", mock_shuffle)
    result = shuffle(input_string)
    assert result == "dlrow olleh"
    assert sorted(result) == sorted(input_string)

def test_shuffle_empty_string():
    input_string = ""
    result = shuffle(input_string)
    assert result == ""

def test_shuffle_invalid_input():
    with pytest.raises(InvalidInputError) as excinfo:
        shuffle(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'
