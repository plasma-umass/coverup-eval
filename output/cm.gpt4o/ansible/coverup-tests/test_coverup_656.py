# file lib/ansible/galaxy/token.py:39-42
# lines [39, 40, 41, 42]
# branches []

import pytest
from ansible.galaxy.token import NoTokenSentinel

def test_no_token_sentinel():
    # Create an instance of NoTokenSentinel
    sentinel_instance = NoTokenSentinel()

    # Assert that the instance is the NoTokenSentinel class itself
    assert sentinel_instance is NoTokenSentinel
