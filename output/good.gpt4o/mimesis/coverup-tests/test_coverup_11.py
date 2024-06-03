# file mimesis/providers/address.py:44-64
# lines [44, 45, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 64]
# branches ['59->60', '59->61', '61->62', '61->64']

import pytest
from mimesis.providers.address import Address

def test_dd_to_dms():
    address = Address()

    # Test for longitude
    result_lg = address._dd_to_dms(-73.935242, 'lg')
    assert result_lg == "73º56'6.871\"W"

    result_lg = address._dd_to_dms(73.935242, 'lg')
    assert result_lg == "73º56'6.871\"E"

    # Test for latitude
    result_lt = address._dd_to_dms(-40.712776, 'lt')
    assert result_lt == "40º42'45.994\"S"

    result_lt = address._dd_to_dms(40.712776, 'lt')
    assert result_lt == "40º42'45.994\"N"

    # Test edge cases
    result_edge = address._dd_to_dms(0, 'lg')
    assert result_edge == "0º0'0.000\"E"

    result_edge = address._dd_to_dms(0, 'lt')
    assert result_edge == "0º0'0.000\"N"
