# file mimesis/providers/cryptographic.py:88-102
# lines [88, 89, 102]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

def test_token_hex_default_entropy():
    crypto = Cryptographic()
    token = crypto.token_hex()
    assert isinstance(token, str)
    assert len(token) == 64  # 32 bytes * 2 hex digits per byte

def test_token_hex_custom_entropy():
    crypto = Cryptographic()
    entropy = 16
    token = crypto.token_hex(entropy)
    assert isinstance(token, str)
    assert len(token) == entropy * 2  # 16 bytes * 2 hex digits per byte

def test_token_hex_zero_entropy():
    crypto = Cryptographic()
    token = crypto.token_hex(0)
    assert isinstance(token, str)
    assert len(token) == 0  # 0 bytes * 2 hex digits per byte

def test_token_hex_negative_entropy():
    crypto = Cryptographic()
    with pytest.raises(ValueError):
        crypto.token_hex(-1)
