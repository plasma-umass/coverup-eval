# file typesystem/tokenize/tokens.py:74-79
# lines [74, 75, 76, 78, 79]
# branches []

import pytest
from typesystem.tokenize.tokens import ScalarToken

@pytest.fixture
def scalar_token():
    token = ScalarToken(value=123, start_index=0, end_index=3)
    yield token
    # No cleanup needed for this simple object

def test_scalar_token_hash(scalar_token):
    # Test the __hash__ method
    assert isinstance(hash(scalar_token), int), "Hash must be an integer"

def test_scalar_token_get_value(scalar_token):
    # Test the _get_value method
    assert scalar_token._get_value() == 123, "The value should be equal to the initialized value"
