# file lib/ansible/module_utils/common/network.py:51-61
# lines [51, 53, 54, 56, 57, 58, 59, 61]
# branches ['53->54', '53->56', '57->58', '57->61']

import pytest
from ansible.module_utils.common.network import to_masklen

def is_netmask(val):
    # Mocked is_netmask function to control the flow of to_masklen
    if val == "255.255.255.0":
        return True
    elif val == "invalid":
        return False
    else:
        raise ValueError("Unexpected value")

@pytest.fixture
def mock_is_netmask(mocker):
    # Patch the is_netmask function with our mock
    mocker.patch('ansible.module_utils.common.network.is_netmask', side_effect=is_netmask)

def test_to_masklen_valid(mock_is_netmask):
    # Test a valid netmask conversion
    masklen = to_masklen("255.255.255.0")
    assert masklen == 24, "Expected mask length of 24"

def test_to_masklen_invalid(mock_is_netmask):
    # Test an invalid netmask conversion
    with pytest.raises(ValueError) as excinfo:
        to_masklen("invalid")
    assert 'invalid value for netmask' in str(excinfo.value), "Expected a ValueError for an invalid netmask"
