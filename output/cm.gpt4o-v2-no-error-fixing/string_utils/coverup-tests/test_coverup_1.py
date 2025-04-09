# file: string_utils/manipulation.py:357-379
# asked: {"lines": [357, 369, 370, 373, 376, 379], "branches": [[369, 370], [369, 373]]}
# gained: {"lines": [357, 369, 370, 373, 376, 379], "branches": [[369, 370], [369, 373]]}

import pytest
from string_utils.manipulation import shuffle
from string_utils.errors import InvalidInputError
from string_utils.validation import is_string

def test_shuffle_valid_string(monkeypatch):
    input_string = "hello world"
    
    def mock_is_string(s):
        return True
    
    monkeypatch.setattr("string_utils.validation.is_string", mock_is_string)
    
    result = shuffle(input_string)
    assert sorted(result) == sorted(input_string)
    assert result != input_string

def test_shuffle_invalid_string(monkeypatch):
    input_string = 12345
    
    def mock_is_string(s):
        return False
    
    monkeypatch.setattr("string_utils.validation.is_string", mock_is_string)
    
    with pytest.raises(InvalidInputError):
        shuffle(input_string)
