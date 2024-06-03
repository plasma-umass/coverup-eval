# file lib/ansible/module_utils/common/network.py:19-29
# lines [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# branches ['21->22', '21->23', '23->24', '23->29', '25->23', '25->26']

import pytest
from ansible.module_utils.common.network import is_netmask

def test_is_netmask_valid():
    assert is_netmask('255.255.255.0') == True
    assert is_netmask('255.255.0.0') == True
    assert is_netmask('255.0.0.0') == True

def test_is_netmask_invalid():
    assert is_netmask('255.255.255.256') == False
    assert is_netmask('255.255.255') == False
    assert is_netmask('255.255.255.0.0') == False
    assert is_netmask('255.255.255.a') == False
    assert is_netmask('255.255.255.-1') == False

@pytest.fixture(autouse=True)
def cleanup():
    # Any necessary cleanup code can be added here
    yield
    # Cleanup code to ensure no side effects
