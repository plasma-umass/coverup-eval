# file: typesystem/tokenize/tokens.py:7-13
# asked: {"lines": [7, 8, 10, 11, 12, 13], "branches": []}
# gained: {"lines": [7, 8, 10, 11, 12, 13], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

def test_token_initialization():
    value = "test_value"
    start_index = 0
    end_index = 10
    content = "test_content"
    
    token = Token(value, start_index, end_index, content)
    
    assert token._value == value
    assert token._start_index == start_index
    assert token._end_index == end_index
    assert token._content == content

def test_token_initialization_default_content():
    value = "test_value"
    start_index = 0
    end_index = 10
    
    token = Token(value, start_index, end_index)
    
    assert token._value == value
    assert token._start_index == start_index
    assert token._end_index == end_index
    assert token._content == ""
