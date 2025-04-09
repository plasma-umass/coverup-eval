# file: lib/ansible/module_utils/common/network.py:19-29
# asked: {"lines": [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], "branches": [[21, 22], [21, 23], [23, 24], [23, 29], [25, 23], [25, 26]]}
# gained: {"lines": [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], "branches": [[21, 22], [21, 23], [23, 24], [23, 29], [25, 23], [25, 26]]}

import pytest
from ansible.module_utils.common.network import is_netmask

VALID_MASKS = {0, 128, 192, 224, 240, 248, 252, 254, 255}

def test_is_netmask_valid():
    assert is_netmask('255.255.255.0') == True
    assert is_netmask('255.255.0.0') == True
    assert is_netmask('255.0.0.0') == True

def test_is_netmask_invalid_length():
    assert is_netmask('255.255.255') == False
    assert is_netmask('255.255.255.255.0') == False

def test_is_netmask_invalid_characters():
    assert is_netmask('255.255.255.a') == False
    assert is_netmask('255.255.255.-1') == False

def test_is_netmask_invalid_values():
    assert is_netmask('255.255.255.256') == False
    assert is_netmask('255.255.255.127') == False
