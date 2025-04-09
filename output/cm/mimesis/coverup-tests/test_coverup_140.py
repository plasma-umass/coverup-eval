# file mimesis/providers/address.py:224-230
# lines [224, 230]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_latitude_dms_format(address_provider):
    latitude_dms = address_provider.latitude(dms=True)
    assert isinstance(latitude_dms, str)
    # The latitude in DMS format should contain degrees, minutes, and seconds
    # Adjusting the split character to match the actual format used by mimesis
    dms_parts = latitude_dms.split('º')
    assert len(dms_parts) == 2
    minutes_seconds = dms_parts[1].split("'")
    assert len(minutes_seconds) == 2
    # Adjusting the assertion to check for the correct cardinal direction suffix
    assert minutes_seconds[1][-1] in ['N', 'S']

def test_latitude_decimal_format(address_provider):
    latitude_decimal = address_provider.latitude(dms=False)
    assert isinstance(latitude_decimal, float)
    # The latitude in decimal format should be within the valid range
    assert -90 <= latitude_decimal <= 90
