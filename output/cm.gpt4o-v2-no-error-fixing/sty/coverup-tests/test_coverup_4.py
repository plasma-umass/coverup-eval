# file: sty/primitive.py:195-200
# asked: {"lines": [195, 199, 200], "branches": []}
# gained: {"lines": [195, 199, 200], "branches": []}

import pytest
from collections import namedtuple
from sty.primitive import Register

def test_as_namedtuple(monkeypatch):
    # Create a mock Register object
    reg = Register()
    
    # Mock the as_dict method to return a specific dictionary
    def mock_as_dict():
        return {'color1': 'red', 'color2': 'blue'}
    
    monkeypatch.setattr(reg, 'as_dict', mock_as_dict)
    
    # Call the as_namedtuple method
    result = reg.as_namedtuple()
    
    # Verify the result is a namedtuple with the expected values
    expected = namedtuple("StyleRegister", ['color1', 'color2'])('red', 'blue')
    assert result == expected
    assert result.color1 == 'red'
    assert result.color2 == 'blue'
