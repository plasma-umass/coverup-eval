# file: typesystem/tokenize/tokens.py:28-30
# asked: {"lines": [28, 29, 30], "branches": []}
# gained: {"lines": [28, 29, 30], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

class TestToken:
    def test_value_property(self):
        class TestToken(Token):
            def _get_value(self):
                return "test_value"

        token = TestToken(value="test", start_index=0, end_index=4)
        assert token.value == "test_value"

    def test_value_property_not_implemented(self):
        token = Token(value="test", start_index=0, end_index=4)
        with pytest.raises(NotImplementedError):
            _ = token.value
