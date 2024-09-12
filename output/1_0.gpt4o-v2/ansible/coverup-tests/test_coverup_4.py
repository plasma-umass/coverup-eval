# file: lib/ansible/utils/sentinel.py:49-68
# asked: {"lines": [49, 68], "branches": []}
# gained: {"lines": [49, 68], "branches": []}

import pytest
from ansible.utils.sentinel import Sentinel

def test_sentinel_identity():
    a = Sentinel
    assert a is Sentinel
    assert Sentinel is Sentinel()
    assert Sentinel == Sentinel()

def test_sentinel_equality():
    assert Sentinel() is Sentinel
    assert Sentinel() == Sentinel
