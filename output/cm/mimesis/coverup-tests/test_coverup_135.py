# file mimesis/providers/address.py:262-267
# lines [262, 267]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis.data import CALLING_CODES

def test_calling_code():
    address = Address()
    result = address.calling_code()
    assert result in CALLING_CODES
