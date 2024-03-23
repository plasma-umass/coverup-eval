# file mimesis/providers/cryptographic.py:73-86
# lines [73, 74, 86]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

@pytest.fixture
def cryptographic_provider():
    return Cryptographic()

def test_token_bytes(cryptographic_provider):
    # Test default entropy
    default_entropy_bytes = cryptographic_provider.token_bytes()
    assert len(default_entropy_bytes) == 32, "Default entropy should be 32 bytes"

    # Test custom entropy
    custom_entropy = 16
    custom_entropy_bytes = cryptographic_provider.token_bytes(custom_entropy)
    assert len(custom_entropy_bytes) == custom_entropy, "Custom entropy should match the specified number of bytes"

    # Test that the output is bytes
    assert isinstance(default_entropy_bytes, bytes), "Output should be bytes"
    assert isinstance(custom_entropy_bytes, bytes), "Output should be bytes"
