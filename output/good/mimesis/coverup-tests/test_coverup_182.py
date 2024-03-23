# file mimesis/providers/address.py:175-187
# lines [186, 187]
# branches []

import pytest
from mimesis.enums import CountryCode
from mimesis.providers.address import Address
from mimesis.exceptions import NonEnumerableError

def test_country_code_with_invalid_enum(mocker):
    address = Address()
    invalid_enum = 'invalid_enum'
    mocker.patch.object(address, '_validate_enum', side_effect=NonEnumerableError(invalid_enum))
    
    with pytest.raises(NonEnumerableError):
        address.country_code(fmt=invalid_enum)
    
    address._validate_enum.assert_called_once_with(invalid_enum, CountryCode)
