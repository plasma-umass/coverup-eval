# file src/blib2to3/pgen2/tokenize.py:176-177
# lines [176, 177]
# branches []

import pytest
from blib2to3.pgen2.tokenize import TokenError

def test_token_error():
    with pytest.raises(TokenError) as exc_info:
        raise TokenError("test error message")
    assert str(exc_info.value) == "test error message"
