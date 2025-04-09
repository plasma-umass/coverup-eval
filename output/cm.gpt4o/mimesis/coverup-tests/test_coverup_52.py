# file mimesis/providers/address.py:251-260
# lines [251, 257, 258, 260]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis.data import CONTINENT_CODES

@pytest.fixture
def address():
    return Address()

def test_continent_name(address):
    continent_name = address.continent(code=False)
    assert continent_name in address._data['continent']

def test_continent_code(address):
    continent_code = address.continent(code=True)
    assert continent_code in CONTINENT_CODES
