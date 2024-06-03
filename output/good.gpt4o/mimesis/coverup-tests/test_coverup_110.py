# file mimesis/providers/payment.py:70-83
# lines [70, 81, 82, 83]
# branches []

import pytest
from mimesis.providers.payment import Payment

def test_ethereum_address(mocker):
    payment = Payment()
    
    # Mock the random.getrandbits method to ensure deterministic output
    mocker.patch.object(payment.random, 'getrandbits', return_value=0x3a0c92075c0dbf3b8acbc5f96ce3f0ad2)
    
    address = payment.ethereum_address()
    
    # Verify the address format and content
    assert address.startswith('0x')
    assert len(address) == 42  # 2 characters for '0x' and 40 for the hex representation
    assert address == '0x00000003a0c92075c0dbf3b8acbc5f96ce3f0ad2'
