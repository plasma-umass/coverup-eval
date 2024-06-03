# file typesystem/tokenize/tokens.py:21-22
# lines [21, 22]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

def test_get_key_token_not_implemented():
    token = Token(value="test", start_index=0, end_index=1)
    with pytest.raises(NotImplementedError):
        token._get_key_token("some_key")
