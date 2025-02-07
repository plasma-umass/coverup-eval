# file: typesystem/tokenize/tokens.py:15-16
# asked: {"lines": [15, 16], "branches": []}
# gained: {"lines": [15, 16], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

def test_token_get_value_raises_not_implemented_error():
    token = Token(value=None, start_index=0, end_index=0)
    with pytest.raises(NotImplementedError):
        token._get_value()
