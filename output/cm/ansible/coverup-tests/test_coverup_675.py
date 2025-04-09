# file lib/ansible/module_utils/common/network.py:32-36
# lines [32, 33, 34, 35, 36]
# branches []

import pytest
from ansible.module_utils.common.network import is_masklen

def test_is_masklen_valid():
    assert is_masklen('24') is True
    assert is_masklen('0') is True
    assert is_masklen('32') is True

def test_is_masklen_invalid():
    assert is_masklen('33') is False
    assert is_masklen('-1') is False
    assert is_masklen('invalid') is False
