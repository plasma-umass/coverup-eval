# file mimesis/providers/payment.py:57-68
# lines [57, 65, 66, 67, 68]
# branches []

import pytest
from mimesis.providers.payment import Payment
import string

@pytest.fixture
def payment_provider():
    return Payment()

def test_bitcoin_address(payment_provider):
    address = payment_provider.bitcoin_address()
    
    # Check the length of the address
    assert len(address) == 34
    
    # Check the first character is either '1' or '3'
    assert address[0] in ['1', '3']
    
    # Check the rest of the address contains only valid characters
    valid_chars = string.ascii_letters + string.digits
    for char in address[1:]:
        assert char in valid_chars
