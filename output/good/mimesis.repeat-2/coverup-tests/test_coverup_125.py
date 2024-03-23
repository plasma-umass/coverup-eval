# file mimesis/providers/address.py:175-187
# lines [175, 186, 187]
# branches []

import pytest
from mimesis.enums import CountryCode
from mimesis.providers.address import Address
from mimesis.exceptions import NonEnumerableError

def test_country_code_with_unsupported_format():
    address = Address()
    with pytest.raises(NonEnumerableError):
        address.country_code(fmt='unsupported_format')

def test_country_code_with_supported_format():
    address = Address()
    supported_formats = [CountryCode.A2, CountryCode.A3, CountryCode.NUMERIC]
    for fmt in supported_formats:
        code = address.country_code(fmt=fmt)
        assert len(code) > 0  # Simple check to ensure a code is returned

def test_country_code_with_none_format():
    address = Address()
    code = address.country_code(fmt=None)
    assert len(code) > 0  # Simple check to ensure a code is returned
