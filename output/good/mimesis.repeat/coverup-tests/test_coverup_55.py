# file mimesis/providers/address.py:251-260
# lines [251, 257, 258, 260]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis.enums import Gender
from mimesis import Generic

CONTINENT_CODES = ['AF', 'AN', 'AS', 'EU', 'NA', 'OC', 'SA']

@pytest.fixture
def address():
    return Address()

def test_continent_with_code(address):
    continent_code = address.continent(code=True)
    assert continent_code in CONTINENT_CODES

def test_continent_without_code(address):
    generic = Generic('en')
    continent_name = address.continent(code=False)
    assert continent_name in generic.address._data['continent']
