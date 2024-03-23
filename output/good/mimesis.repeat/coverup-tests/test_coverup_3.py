# file mimesis/providers/address.py:44-64
# lines [44, 45, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 64]
# branches ['59->60', '59->61', '61->62', '61->64']

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address():
    return Address()

@pytest.mark.parametrize("num, _type, expected", [
    (-73.935242, 'lg', "73º56'6.871\"W"),
    (40.730610, 'lt', "40º43'50.196\"N"),
    (-73.935242, 'unknown', "73º56'6.871\""),
    (40.730610, 'unknown', "40º43'50.196\""),
])
def test_dd_to_dms(address, num, _type, expected):
    result = address._dd_to_dms(num, _type)
    assert result == expected
