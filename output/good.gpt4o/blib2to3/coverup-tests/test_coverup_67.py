# file src/blib2to3/pgen2/tokenize.py:176-177
# lines [176, 177]
# branches []

import pytest
from blib2to3.pgen2.tokenize import TokenError

def test_token_error():
    with pytest.raises(TokenError):
        raise TokenError("This is a token error")

    # Ensure the exception message is correct
    try:
        raise TokenError("This is a token error")
    except TokenError as e:
        assert str(e) == "This is a token error"
