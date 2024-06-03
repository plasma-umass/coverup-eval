# file mimesis/providers/cryptographic.py:28-31
# lines [28, 29, 31]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

def test_cryptographic_meta():
    # Create an instance of the Cryptographic provider
    crypto_provider = Cryptographic()
    
    # Check if the Meta class exists
    assert hasattr(crypto_provider, 'Meta')
    
    # Check if the name attribute in Meta class is correct
    assert crypto_provider.Meta.name == 'cryptographic'
