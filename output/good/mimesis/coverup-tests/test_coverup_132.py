# file mimesis/providers/address.py:130-135
# lines [130, 135]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis import Generic


@pytest.fixture
def address():
    generic = Generic('en')
    return generic.address


def test_region(address, mocker):
    mocker.patch.object(Address, 'state', return_value='Alabama')
    region_result = address.region()
    state_result = address.state()
    assert region_result == state_result, "Region should be an alias for state"
