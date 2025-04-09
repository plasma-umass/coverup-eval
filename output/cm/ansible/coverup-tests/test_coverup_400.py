# file lib/ansible/module_utils/common/network.py:39-48
# lines [39, 41, 42, 44, 45, 46, 48]
# branches ['41->42', '41->44', '45->46', '45->48']

import pytest
from ansible.module_utils.common.network import to_netmask
from socket import inet_ntoa
from struct import pack

# Test function to cover to_netmask function
def test_to_netmask():
    # Test with valid masklen
    assert to_netmask(8) == inet_ntoa(pack('>I', 0xFF000000))
    assert to_netmask(16) == inet_ntoa(pack('>I', 0xFFFF0000))
    assert to_netmask(24) == inet_ntoa(pack('>I', 0xFFFFFF00))
    assert to_netmask(32) == inet_ntoa(pack('>I', 0xFFFFFFFF))

    # Test with invalid masklen
    with pytest.raises(ValueError):
        to_netmask(33)
    with pytest.raises(ValueError):
        to_netmask(-1)
    with pytest.raises(ValueError):
        to_netmask('invalid')

# Mock function to simulate is_masklen behavior
def mock_is_masklen(val):
    try:
        val = int(val)
        return 0 <= val <= 32
    except ValueError:
        return False

# Patch the is_masklen function in the module with the mock
@pytest.fixture(autouse=True)
def mock_is_masklen_fixture(mocker):
    mocker.patch('ansible.module_utils.common.network.is_masklen', side_effect=mock_is_masklen)

# Run the test function
def test_to_netmask_with_mock():
    test_to_netmask()
