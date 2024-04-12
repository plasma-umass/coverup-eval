# file mimesis/providers/cryptographic.py:88-102
# lines [88, 89, 102]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

def test_token_hex_default_entropy():
    # Test the default entropy value
    token = Cryptographic.token_hex()
    assert len(token) == 64  # 32 bytes * 2 hex chars per byte

def test_token_hex_custom_entropy():
    # Test a custom entropy value
    custom_entropy = 16
    token = Cryptographic.token_hex(custom_entropy)
    assert len(token) == custom_entropy * 2  # custom_entropy bytes * 2 hex chars per byte

def test_token_hex_zero_entropy():
    # Test zero entropy
    token = Cryptographic.token_hex(0)
    assert token == ''  # Zero entropy should return an empty string

def test_token_hex_negative_entropy():
    # Test negative entropy, which should raise a ValueError
    with pytest.raises(ValueError):
        Cryptographic.token_hex(-1)
