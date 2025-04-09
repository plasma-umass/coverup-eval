# file: src/blib2to3/pgen2/parse.py:42-54
# asked: {"lines": [42, 43, 45, 48, 49, 51, 52, 53, 54], "branches": []}
# gained: {"lines": [42, 43, 45, 48, 49, 51, 52, 53, 54], "branches": []}

import pytest
from blib2to3.pgen2.parse import ParseError

def test_parse_error_initialization():
    msg = "Error message"
    type = 1
    value = "Some value"
    context = "Some context"
    
    error = ParseError(msg, type, value, context)
    
    assert error.msg == msg
    assert error.type == type
    assert error.value == value
    assert error.context == context
    assert str(error) == "Error message: type=1, value='Some value', context='Some context'"

def test_parse_error_no_type():
    msg = "Error message"
    type = None
    value = "Some value"
    context = "Some context"
    
    error = ParseError(msg, type, value, context)
    
    assert error.msg == msg
    assert error.type is None
    assert error.value == value
    assert error.context == context
    assert str(error) == "Error message: type=None, value='Some value', context='Some context'"

def test_parse_error_no_value():
    msg = "Error message"
    type = 1
    value = None
    context = "Some context"
    
    error = ParseError(msg, type, value, context)
    
    assert error.msg == msg
    assert error.type == type
    assert error.value is None
    assert error.context == context
    assert str(error) == "Error message: type=1, value=None, context='Some context'"

def test_parse_error_no_context():
    msg = "Error message"
    type = 1
    value = "Some value"
    context = None
    
    error = ParseError(msg, type, value, context)
    
    assert error.msg == msg
    assert error.type == type
    assert error.value == value
    assert error.context is None
    assert str(error) == "Error message: type=1, value='Some value', context=None"
