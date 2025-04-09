# file: typesystem/tokenize/tokens.py:15-16
# asked: {"lines": [15, 16], "branches": []}
# gained: {"lines": [15, 16], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

def test_token_get_value():
    token = Token(value="test", start_index=0, end_index=4)
    with pytest.raises(NotImplementedError):
        token._get_value()
