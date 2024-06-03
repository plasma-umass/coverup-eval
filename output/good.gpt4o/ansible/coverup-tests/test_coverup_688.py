# file lib/ansible/galaxy/token.py:101-105
# lines [101, 102, 104]
# branches []

import pytest
from ansible.galaxy.token import GalaxyToken

def test_galaxy_token_initialization():
    # Test the initialization of GalaxyToken class
    token = GalaxyToken()
    assert token.token_type == 'Token'
