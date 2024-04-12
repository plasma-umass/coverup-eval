# file mimesis/providers/cryptographic.py:73-86
# lines [73, 74, 86]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

def test_token_bytes():
    # Test default entropy
    default_entropy_bytes = Cryptographic.token_bytes()
    assert len(default_entropy_bytes) == 32, "Default entropy should be 32 bytes"

    # Test custom entropy
    custom_entropy = 16
    custom_entropy_bytes = Cryptographic.token_bytes(custom_entropy)
    assert len(custom_entropy_bytes) == custom_entropy, "Custom entropy should match the specified number of bytes"

    # Test zero entropy
    zero_entropy_bytes = Cryptographic.token_bytes(0)
    assert len(zero_entropy_bytes) == 0, "Zero entropy should return an empty bytes object"

    # Test negative entropy should raise ValueError
    with pytest.raises(ValueError):
        Cryptographic.token_bytes(-1)
