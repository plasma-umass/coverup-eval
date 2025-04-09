# file mimesis/providers/internet.py:144-159
# lines [152, 153, 154, 155, 156, 158, 159]
# branches []

import pytest
from mimesis.providers.internet import Internet

@pytest.fixture
def internet():
    return Internet()

def test_mac_address(internet, mocker):
    # Mock the random.randint method to ensure the lines 154-156 are executed
    mocker.patch.object(internet.random, 'randint', side_effect=[0x1a, 0x2b, 0x3c])
    
    mac = internet.mac_address()
    
    # Verify the format of the MAC address
    assert isinstance(mac, str)
    assert len(mac.split(':')) == 6
    assert all(len(part) == 2 for part in mac.split(':'))
    
    # Verify the mocked values are in the MAC address
    expected_mac_parts = ['00', '16', '3e', '1a', '2b', '3c']
    assert mac.split(':') == expected_mac_parts
