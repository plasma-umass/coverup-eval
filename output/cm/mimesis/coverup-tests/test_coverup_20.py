# file mimesis/providers/address.py:44-64
# lines [44, 45, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 64]
# branches ['59->60', '59->61', '61->62', '61->64']

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address():
    return Address()

def test_dd_to_dms_longitude(address):
    longitude = -73.935242
    dms_longitude = address._dd_to_dms(longitude, 'lg')
    assert dms_longitude == "73º56'6.871\"W"

def test_dd_to_dms_latitude(address):
    latitude = 40.730610
    dms_latitude = address._dd_to_dms(latitude, 'lt')
    assert dms_latitude == "40º43'50.196\"N"

def test_dd_to_dms_no_direction(address):
    number = 15.7833
    dms_number = address._dd_to_dms(number, '')
    assert dms_number == "15º46'59.880\""
