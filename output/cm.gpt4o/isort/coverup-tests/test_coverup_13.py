# file isort/exceptions.py:93-105
# lines [93, 94, 98, 99, 100, 102, 104, 105]
# branches []

import pytest
from isort.exceptions import LiteralParsingFailure

def test_literal_parsing_failure():
    code = "[1, 2, 3"
    original_error = SyntaxError("unexpected EOF while parsing")
    
    # Create an instance of LiteralParsingFailure
    exception = LiteralParsingFailure(code, original_error)
    
    # Assert that the exception message is correctly formatted
    expected_message = (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )
    assert str(exception) == expected_message
    
    # Assert that the code and original_error attributes are correctly set
    assert exception.code == code
    assert exception.original_error == original_error
