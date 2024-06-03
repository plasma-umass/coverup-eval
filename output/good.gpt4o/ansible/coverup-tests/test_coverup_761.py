# file lib/ansible/module_utils/common/network.py:152-161
# lines [152, 160, 161]
# branches []

import pytest
import re
from ansible.module_utils.common.network import is_mac

def test_is_mac_valid_mac():
    assert is_mac("00:1A:2B:3C:4D:5E") == True
    assert is_mac("00-1A-2B-3C-4D-5E") == True
    assert is_mac("00:1a:2b:3c:4d:5e") == True
    assert is_mac("00-1a-2b-3c-4d-5e") == True

def test_is_mac_invalid_mac():
    assert is_mac("001A:2B:3C:4D:5E") == False
    assert is_mac("00:1A:2B:3C:4D:5E:6F") == False
    assert is_mac("00:1A:2B:3C:4D") == False
    assert is_mac("00:1A:2B:3C:4D:5G") == False
    assert is_mac("00-1A-2B-3C-4D-5E-6F") == False
    assert is_mac("00-1A-2B-3C-4D") == False
    assert is_mac("00-1A-2B-3C-4D-5G") == False
    assert is_mac("001A2B3C4D5E") == False
    assert is_mac("00:1A:2B:3C:4D:5E:") == False
    assert is_mac(":00:1A:2B:3C:4D:5E") == False
    assert is_mac("00:1A:2B:3C:4D:5E:00") == False
    assert is_mac("00:1A:2B:3C:4D:5E:00:1A") == False
