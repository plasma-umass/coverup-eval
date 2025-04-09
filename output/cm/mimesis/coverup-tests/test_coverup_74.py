# file mimesis/providers/address.py:39-42
# lines [39, 40, 42]
# branches []

import pytest
from mimesis.providers.address import Address

def test_address_meta():
    address = Address()
    assert address.Meta.name == 'address'
