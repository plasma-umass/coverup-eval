# file lib/ansible/galaxy/token.py:39-42
# lines [39, 40, 41, 42]
# branches []

import pytest
from ansible.galaxy.token import NoTokenSentinel

def test_no_token_sentinel_singleton_behavior():
    # Test that NoTokenSentinel always returns the same instance (singleton behavior)
    sentinel_instance_1 = NoTokenSentinel()
    sentinel_instance_2 = NoTokenSentinel()

    assert sentinel_instance_1 is NoTokenSentinel
    assert sentinel_instance_2 is NoTokenSentinel
