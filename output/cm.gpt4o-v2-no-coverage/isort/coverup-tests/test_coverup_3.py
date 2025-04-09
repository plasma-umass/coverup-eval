# file: isort/exceptions.py:93-105
# asked: {"lines": [93, 94, 98, 99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [93, 94, 98, 99, 100, 102, 104, 105], "branches": []}

import pytest
from isort.exceptions import LiteralParsingFailure

def test_literal_parsing_failure():
    code = "[1, 2, 3"
    original_error = SyntaxError("unexpected EOF while parsing")
    
    exception = LiteralParsingFailure(code, original_error)
    
    assert exception.code == code
    assert exception.original_error == original_error
    assert str(exception) == (
        "isort failed to parse the given literal [1, 2, 3. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of unexpected EOF while parsing."
    )
