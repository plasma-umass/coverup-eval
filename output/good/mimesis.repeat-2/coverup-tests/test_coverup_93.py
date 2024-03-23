# file mimesis/providers/cryptographic.py:88-102
# lines [88, 89, 102]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

def test_token_hex_default_entropy():
    cryptographic = Cryptographic()
    token = cryptographic.token_hex()
    assert len(token) == 64  # 32 bytes * 2 hex chars per byte

def test_token_hex_custom_entropy():
    cryptographic = Cryptographic()
    custom_entropy = 16
    token = cryptographic.token_hex(custom_entropy)
    assert len(token) == custom_entropy * 2  # custom_entropy bytes * 2 hex chars per byte

def test_token_hex_zero_entropy():
    cryptographic = Cryptographic()
    token = cryptographic.token_hex(0)
    assert token == ''  # zero entropy should return an empty string

def test_token_hex_negative_entropy():
    cryptographic = Cryptographic()
    with pytest.raises(ValueError):
        cryptographic.token_hex(-1)  # negative entropy should raise a ValueError
