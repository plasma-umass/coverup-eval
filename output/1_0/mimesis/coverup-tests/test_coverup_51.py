# file mimesis/enums.py:146-156
# lines [146, 147, 152, 153, 154, 155, 156]
# branches []

import pytest
from mimesis.enums import CountryCode

def test_country_code_enum():
    assert CountryCode.A2.value == 'a2'
    assert CountryCode.A3.value == 'a3'
    assert CountryCode.NUMERIC.value == 'numeric'
    assert CountryCode.IOC.value == 'ioc'
    assert CountryCode.FIFA.value == 'fifa'

    # Ensure all enum members are tested
    for country_code in CountryCode:
        assert country_code.value in [member.value for member in CountryCode]
