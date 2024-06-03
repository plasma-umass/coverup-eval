# file mimesis/providers/address.py:23-29
# lines [23, 24]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis import Generic

@pytest.fixture
def address_provider():
    return Address()

def test_address_provider_initialization(address_provider):
    assert isinstance(address_provider, Address)

def test_address_provider_methods(address_provider):
    # Assuming Address class has methods like street_name, city, etc.
    street_name = address_provider.street_name()
    city = address_provider.city()
    
    assert isinstance(street_name, str)
    assert isinstance(city, str)
    assert street_name != ""
    assert city != ""

def test_generic_address_provider():
    generic = Generic()
    address = generic.address
    
    assert isinstance(address, Address)
    street_name = address.street_name()
    city = address.city()
    
    assert isinstance(street_name, str)
    assert isinstance(city, str)
    assert street_name != ""
    assert city != ""
