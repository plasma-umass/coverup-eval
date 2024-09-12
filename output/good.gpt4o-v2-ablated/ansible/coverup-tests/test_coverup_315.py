# file: lib/ansible/module_utils/common/network.py:152-161
# asked: {"lines": [152, 160, 161], "branches": []}
# gained: {"lines": [152, 160, 161], "branches": []}

import pytest
import re
from ansible.module_utils.common.network import is_mac

def test_is_mac_valid_colon():
    assert is_mac("01:23:45:67:89:ab") == True

def test_is_mac_valid_dash():
    assert is_mac("01-23-45-67-89-ab") == True

def test_is_mac_invalid_length():
    assert is_mac("01:23:45:67:89") == False

def test_is_mac_invalid_characters():
    assert is_mac("01:23:45:67:89:az") == False

def test_is_mac_invalid_separator():
    assert is_mac("01:23:45:67:89:ab:cd") == False

def test_is_mac_mixed_case():
    assert is_mac("01:23:45:67:89:AB") == True

def test_is_mac_empty_string():
    assert is_mac("") == False

def test_is_mac_no_separator():
    assert is_mac("0123456789ab") == False
