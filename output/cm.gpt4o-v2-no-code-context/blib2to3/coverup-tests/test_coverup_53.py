# file: src/blib2to3/pgen2/tokenize.py:176-177
# asked: {"lines": [176, 177], "branches": []}
# gained: {"lines": [176, 177], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import TokenError

def test_token_error_inheritance():
    with pytest.raises(TokenError):
        raise TokenError("This is a token error")

def test_token_error_message():
    try:
        raise TokenError("This is a token error")
    except TokenError as e:
        assert str(e) == "This is a token error"
