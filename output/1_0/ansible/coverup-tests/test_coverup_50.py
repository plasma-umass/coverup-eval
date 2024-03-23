# file lib/ansible/utils/sentinel.py:49-68
# lines [68]
# branches []

import pytest
from ansible.utils.sentinel import Sentinel

def test_sentinel_identity_and_equality():
    # Test for both identity and equality
    assert Sentinel is Sentinel(), "Sentinel identity check failed"
    assert Sentinel == Sentinel(), "Sentinel equality check failed"
