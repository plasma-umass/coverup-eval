# file typesystem/tokenize/tokens.py:18-19
# lines [18, 19]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

def test_get_child_token_not_implemented():
    token = Token(value="test", start_index=0, end_index=1)
    with pytest.raises(NotImplementedError):
        token._get_child_token("some_key")
