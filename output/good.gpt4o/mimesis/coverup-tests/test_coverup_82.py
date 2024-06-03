# file mimesis/providers/cryptographic.py:73-86
# lines [73, 74, 86]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

def test_token_bytes():
    entropy = 32
    result = Cryptographic.token_bytes(entropy)
    
    # Verify the length of the result
    assert len(result) == entropy
    
    # Verify the type of the result
    assert isinstance(result, bytes)

    # Verify that different calls produce different results
    result2 = Cryptographic.token_bytes(entropy)
    assert result != result2

    # Verify with a different entropy value
    entropy = 16
    result = Cryptographic.token_bytes(entropy)
    assert len(result) == entropy
    assert isinstance(result, bytes)
