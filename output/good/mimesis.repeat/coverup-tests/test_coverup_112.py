# file mimesis/providers/cryptographic.py:104-117
# lines [104, 105, 117]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

def test_token_urlsafe_default_entropy():
    # Test the default entropy value
    token = Cryptographic.token_urlsafe()
    assert isinstance(token, str)
    assert len(token) >= 32  # The length should be at least 32 characters for the default entropy

def test_token_urlsafe_custom_entropy():
    # Test a custom entropy value
    custom_entropy = 16
    token = Cryptographic.token_urlsafe(custom_entropy)
    assert isinstance(token, str)
    assert len(token) >= custom_entropy  # The length should be at least as long as the custom entropy

def test_token_urlsafe_none_entropy():
    # Test passing None as entropy
    token = Cryptographic.token_urlsafe(None)
    assert isinstance(token, str)
    # We cannot assert the length here because the default is implementation-dependent

def test_token_urlsafe_zero_entropy():
    # Test passing zero as entropy
    token = Cryptographic.token_urlsafe(0)
    assert token == ''  # Zero entropy should return an empty string

def test_token_urlsafe_negative_entropy():
    # Test passing a negative entropy value
    with pytest.raises(ValueError):
        Cryptographic.token_urlsafe(-1)
