# file mimesis/providers/cryptographic.py:17-19
# lines [17, 18]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

def test_cryptographic_class_instantiation():
    # Test instantiation of the Cryptographic class
    crypto_provider = Cryptographic()
    assert isinstance(crypto_provider, Cryptographic)
