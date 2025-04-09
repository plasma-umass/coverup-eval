# file mimesis/providers/address.py:175-187
# lines [175, 186, 187]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis.enums import CountryCode
from mimesis.exceptions import NonEnumerableError

def test_country_code_a2():
    address = Address()
    code = address.country_code(CountryCode.A2)
    assert len(code) == 2  # ISO 3166-1-alpha2 codes are 2 characters long

def test_country_code_a3():
    address = Address()
    code = address.country_code(CountryCode.A3)
    assert len(code) == 3  # ISO 3166-1-alpha3 codes are 3 characters long

def test_country_code_numeric():
    address = Address()
    code = address.country_code(CountryCode.NUMERIC)
    assert code.isdigit()  # Numeric country codes should be digits

def test_country_code_invalid_enum():
    address = Address()
    with pytest.raises(NonEnumerableError):
        address.country_code("INVALID_ENUM")

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Mock any global state or cleanup if necessary
    yield
    # Perform cleanup actions if needed
