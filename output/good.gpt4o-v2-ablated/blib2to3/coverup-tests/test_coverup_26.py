# file: src/blib2to3/pgen2/tokenize.py:176-177
# asked: {"lines": [176, 177], "branches": []}
# gained: {"lines": [176, 177], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import TokenError

def test_token_error_inheritance():
    assert issubclass(TokenError, Exception)

def test_token_error_instance():
    error_message = "This is a token error"
    token_error = TokenError(error_message)
    assert isinstance(token_error, TokenError)
    assert str(token_error) == error_message
