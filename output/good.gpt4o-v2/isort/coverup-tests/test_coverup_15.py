# file: isort/exceptions.py:93-105
# asked: {"lines": [93, 94, 98, 99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [93, 94, 98, 99, 100, 102, 104, 105], "branches": []}

import pytest
from isort.exceptions import LiteralParsingFailure, ISortError

def test_literal_parsing_failure():
    code = "[1, 2, 3"
    original_error = SyntaxError("unexpected EOF while parsing")
    
    with pytest.raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure(code, original_error)
    
    exception = exc_info.value
    assert isinstance(exception, ISortError)
    assert exception.code == code
    assert exception.original_error == original_error
    assert str(exception) == (
        f"isort failed to parse the given literal {code}. It's important to note that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )
