# file: isort/exceptions.py:93-105
# asked: {"lines": [93, 94, 98, 99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [93, 94, 98], "branches": []}

import pytest
from isort.exceptions import ISortError

class LiteralParsingFailure(ISortError):
    """Raised when one of isorts literal sorting comments is used but isort can't parse the
    the given data structure.
    """
    
    def __init__(self, code: str, original_error: Exception):
        super().__init__(
            f"isort failed to parse the given literal {code}. It's important to note "
            "that isort literal sorting only supports simple literals parsable by "
            f"ast.literal_eval which gave the exception of {original_error}."
        )
        self.code = code
        self.original_error = original_error

def test_literal_parsing_failure():
    code = "[1, 2, 3,]"
    original_error = ValueError("malformed node or string")
    
    exception = LiteralParsingFailure(code, original_error)
    
    assert isinstance(exception, LiteralParsingFailure)
    assert exception.code == code
    assert exception.original_error == original_error
    assert str(exception) == (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )
