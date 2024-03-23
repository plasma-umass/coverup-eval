# file mimesis/providers/address.py:251-260
# lines [251, 257, 258, 260]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address():
    return Address()

def test_continent_with_code(address):
    continent_code = address.continent(code=True)
    assert len(continent_code) == 2  # Assuming continent codes are 2-letter codes

def test_continent_without_code(address):
    continent_name = address.continent(code=False)
    assert isinstance(continent_name, str) and len(continent_name) > 0
