# file: typesystem/tokenize/tokens.py:74-79
# asked: {"lines": [76, 79], "branches": []}
# gained: {"lines": [76, 79], "branches": []}

import pytest
from typesystem.tokenize.tokens import ScalarToken

def test_scalar_token_hash():
    scalar_token = ScalarToken(value="test_value", start_index=0, end_index=10)
    assert hash(scalar_token) == hash("test_value")

def test_scalar_token_get_value():
    scalar_token = ScalarToken(value="test_value", start_index=0, end_index=10)
    assert scalar_token._get_value() == "test_value"
