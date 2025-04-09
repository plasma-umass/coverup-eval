# file: lib/ansible/module_utils/common/network.py:32-36
# asked: {"lines": [33, 34, 35, 36], "branches": []}
# gained: {"lines": [33, 34, 35, 36], "branches": []}

import pytest

from ansible.module_utils.common.network import is_masklen

def test_is_masklen_valid():
    assert is_masklen(0) == True
    assert is_masklen(32) == True
    assert is_masklen(16) == True

def test_is_masklen_invalid():
    assert is_masklen(-1) == False
    assert is_masklen(33) == False
    assert is_masklen("invalid") == False

def test_is_masklen_non_integer():
    assert is_masklen("10") == True
    assert is_masklen("33") == False
    assert is_masklen("abc") == False
