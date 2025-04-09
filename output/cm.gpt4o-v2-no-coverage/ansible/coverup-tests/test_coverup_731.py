# file: lib/ansible/galaxy/token.py:39-42
# asked: {"lines": [39, 40, 41, 42], "branches": []}
# gained: {"lines": [39, 40, 41, 42], "branches": []}

import pytest
from ansible.galaxy.token import NoTokenSentinel

def test_no_token_sentinel_new():
    instance = NoTokenSentinel()
    assert instance == NoTokenSentinel

