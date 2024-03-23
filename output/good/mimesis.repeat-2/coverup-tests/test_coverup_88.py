# file mimesis/providers/address.py:251-260
# lines [251, 257, 258, 260]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_continent_with_code(address_provider):
    continent_code = address_provider.continent(code=True)
    assert len(continent_code) == 2  # Assuming continent codes are 2-letter codes

def test_continent_without_code(address_provider):
    continent_name = address_provider.continent(code=False)
    assert isinstance(continent_name, str) and continent_name
    assert continent_name in address_provider._data['continent']
