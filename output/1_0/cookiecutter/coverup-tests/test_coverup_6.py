# file cookiecutter/exceptions.py:110-130
# lines [110, 111, 118, 120, 121, 122, 124, 126, 127, 130]
# branches []

import pytest
from cookiecutter.exceptions import UndefinedVariableInTemplate

def test_undefined_variable_in_template_exception():
    message = "Undefined variable found"
    error_message = "Variable 'foo' is not defined"
    context = {'bar': 'baz'}

    class MockError:
        def __init__(self, message):
            self.message = message

    error = MockError(error_message)
    exception = UndefinedVariableInTemplate(message, error, context)

    assert str(exception) == (
        f"{message}. Error message: {error_message}. Context: {context}"
    )
