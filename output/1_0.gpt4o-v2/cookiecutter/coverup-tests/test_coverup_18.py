# file: cookiecutter/exceptions.py:110-130
# asked: {"lines": [110, 111, 118, 120, 121, 122, 124, 126, 127, 130], "branches": []}
# gained: {"lines": [110, 111, 118, 120, 121, 122, 124, 126, 127, 130], "branches": []}

import pytest
from cookiecutter.exceptions import UndefinedVariableInTemplate

class MockError:
    def __init__(self, message):
        self.message = message

def test_UndefinedVariableInTemplate_init():
    message = "Variable not defined"
    error = MockError("Some error")
    context = {"key": "value"}
    
    exception = UndefinedVariableInTemplate(message, error, context)
    
    assert exception.message == message
    assert exception.error == error
    assert exception.context == context

def test_UndefinedVariableInTemplate_str():
    message = "Variable not defined"
    error = MockError("Some error")
    context = {"key": "value"}
    
    exception = UndefinedVariableInTemplate(message, error, context)
    expected_str = "Variable not defined. Error message: Some error. Context: {'key': 'value'}"
    
    assert str(exception) == expected_str
