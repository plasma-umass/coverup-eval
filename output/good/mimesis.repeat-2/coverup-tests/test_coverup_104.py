# file mimesis/providers/cryptographic.py:17-19
# lines [17, 18]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

def test_cryptographic_class_initialization():
    # Test the initialization of the Cryptographic class
    cryptographic = Cryptographic()
    assert isinstance(cryptographic, Cryptographic)
