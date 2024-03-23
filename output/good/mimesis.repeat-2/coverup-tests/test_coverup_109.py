# file mimesis/providers/cryptographic.py:104-117
# lines [104, 105, 117]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

def test_token_urlsafe_default_entropy():
    cryptographic = Cryptographic()
    token = cryptographic.token_urlsafe()
    assert isinstance(token, str)
    assert len(token) >= 32  # Base64 encoding can be longer than the number of bytes

def test_token_urlsafe_custom_entropy():
    cryptographic = Cryptographic()
    custom_entropy = 16
    token = cryptographic.token_urlsafe(entropy=custom_entropy)
    assert isinstance(token, str)
    assert len(token) >= custom_entropy  # Base64 encoding can be longer than the number of bytes

def test_token_urlsafe_none_entropy():
    cryptographic = Cryptographic()
    token = cryptographic.token_urlsafe(entropy=None)
    assert isinstance(token, str)
    # Can't assert on length since None defaults to a "reasonable default" which is not specified
