# file isort/exceptions.py:93-105
# lines [93, 94, 98, 99, 100, 102, 104, 105]
# branches []

import pytest
from isort.exceptions import LiteralParsingFailure

def test_literal_parsing_failure():
    code = "{'key': 'value'}"
    original_error = ValueError("test error")

    with pytest.raises(LiteralParsingFailure) as exc_info:
        raise LiteralParsingFailure(code, original_error)

    exception = exc_info.value
    assert str(exception) == (
        "isort failed to parse the given literal {'key': 'value'}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        "ast.literal_eval which gave the exception of test error."
    )
    assert exception.code == code
    assert exception.original_error == original_error
