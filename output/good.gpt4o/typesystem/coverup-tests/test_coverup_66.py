# file typesystem/tokenize/tokens.py:15-16
# lines [15, 16]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

def test_token_get_value_not_implemented(mocker):
    mocker.patch.object(Token, '__init__', lambda self: None)
    token = Token()
    with pytest.raises(NotImplementedError):
        token._get_value()
