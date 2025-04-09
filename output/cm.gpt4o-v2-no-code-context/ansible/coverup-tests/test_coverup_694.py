# file: lib/ansible/module_utils/common/network.py:152-161
# asked: {"lines": [152, 160, 161], "branches": []}
# gained: {"lines": [152, 160, 161], "branches": []}

import re
import pytest

from ansible.module_utils.common.network import is_mac

def test_is_mac_valid_mac():
    assert is_mac("00:1a:2b:3c:4d:5e") == True
    assert is_mac("00-1a-2b-3c-4d-5e") == True

def test_is_mac_invalid_mac():
    assert is_mac("00:1a:2b:3c:4d:5") == False
    assert is_mac("00-1a-2b-3c-4d-5") == False
    assert is_mac("001a:2b:3c:4d:5e") == False
    assert is_mac("00:1a:2b:3c:4d:5g") == False
    assert is_mac("00:1a:2b:3c:4d:5e:6f") == False
    assert is_mac("00:1a:2b:3c:4d") == False
    assert is_mac("00:1a:2b:3c:4d:5e:") == False
    assert is_mac("00:1a:2b:3c:4d:5e-") == False
    assert is_mac("00:1a:2b:3c:4d:5e:00") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e-") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e-00") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e-00-") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e-00-1a") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e-00-1a-") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e-00-1a-2b") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e-00-1a-2b-") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e-00-1a-2b-3c") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e-00-1a-2b-3c-") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e-00-1a-2b-3c-4d") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e-00-1a-2b-3c-4d-") == False
    assert is_mac("00:1a:2b:3c:4d:5e-00-1a-2b-3c-4d-5e-00-1a-2b-3c-4d-5e") == False
