# file lib/ansible/galaxy/token.py:106-110
# lines [106, 107, 109, 110]
# branches []

import os
import pytest
from unittest.mock import MagicMock
from ansible.constants import GALAXY_TOKEN_PATH
from ansible.galaxy.token import GalaxyToken
from ansible.module_utils._text import to_bytes

# Assuming the existence of a configuration file path constant
# GALAXY_TOKEN_PATH in ansible.constants, which is used in the
# GalaxyToken class.

@pytest.fixture
def galaxy_token_path_mock(mocker, tmp_path):
    # Mock the GALAXY_TOKEN_PATH to a temporary file to avoid
    # altering the actual configuration file during testing.
    temp_file = tmp_path / "temp_galaxy_token"
    mocker.patch('ansible.constants.GALAXY_TOKEN_PATH', str(temp_file))
    return str(temp_file)

def test_galaxy_token_init(galaxy_token_path_mock):
    # Test the __init__ method of GalaxyToken to ensure it sets
    # the _token attribute and creates a byte string for the file path.
    token_value = 'test_token'
    galaxy_token = GalaxyToken(token=token_value)

    # Verify that the _token attribute is set correctly
    assert galaxy_token._token == token_value

    # Verify that the byte string for the file path is created correctly
    expected_b_file = to_bytes(galaxy_token_path_mock, errors='surrogate_or_strict')
    assert galaxy_token.b_file == expected_b_file

    # Clean up is handled by the tmp_path fixture
