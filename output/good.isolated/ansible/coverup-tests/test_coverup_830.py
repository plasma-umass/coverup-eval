# file lib/ansible/module_utils/common/network.py:152-161
# lines [152, 160, 161]
# branches []

import pytest
import re
from ansible.module_utils.common.network import is_mac

@pytest.fixture(scope="function")
def cleanup():
    # No cleanup is necessary for this test as it does not modify any state
    yield

def test_is_mac_valid(cleanup):
    assert is_mac("00:1A:2B:3C:4D:5E") == True
    assert is_mac("00-1A-2B-3C-4D-5E") == True

def test_is_mac_invalid(cleanup):
    assert is_mac("00:1A:2B:3C:4D:5Z") == False
    assert is_mac("00-1A-2B-3C-4D-5E-6F") == False
    assert is_mac("001A:2B:3C:4D:5E") == False
    assert is_mac("00:1A:2B:3C:4D") == False
    assert is_mac("00:1A:2B:3C:4D:5E:6F") == False
    assert is_mac("00:1A:2B:3C:4D:5E6F") == False
    assert is_mac("001A2B3C4D5E") == False
    assert is_mac("G0:1A:2B:3C:4D:5E") == False
    assert is_mac("00:1A:2B:3C:4D:5E ") == False
    assert is_mac(" 00:1A:2B:3C:4D:5E") == False
    assert is_mac("") == False
