# file mimesis/providers/cryptographic.py:28-31
# lines [28, 29, 31]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

def test_cryptographic_meta():
    cryptographic_provider = Cryptographic()
    assert cryptographic_provider.Meta.name == 'cryptographic'
