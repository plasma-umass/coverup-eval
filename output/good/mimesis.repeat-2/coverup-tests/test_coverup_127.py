# file mimesis/providers/address.py:66-72
# lines [66, 72]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis import Generic

@pytest.fixture
def address_provider():
    return Generic().address

def test_street_number_default(address_provider):
    # Test the default maximum value
    street_number = address_provider.street_number()
    assert street_number.isdigit()
    assert 1 <= int(street_number) <= 1400

def test_street_number_custom_max(address_provider):
    # Test a custom maximum value
    custom_max = 2000
    street_number = address_provider.street_number(maximum=custom_max)
    assert street_number.isdigit()
    assert 1 <= int(street_number) <= custom_max

def test_street_number_edge_case(address_provider):
    # Test the edge case where maximum is 1
    street_number = address_provider.street_number(maximum=1)
    assert street_number == '1'
