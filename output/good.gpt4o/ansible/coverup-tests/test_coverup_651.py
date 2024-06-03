# file lib/ansible/galaxy/token.py:106-110
# lines [106, 107, 109, 110]
# branches []

import pytest
from unittest import mock
from ansible.galaxy.token import GalaxyToken
from ansible.module_utils._text import to_bytes
import ansible.constants as C

@pytest.fixture
def mock_constants(mocker):
    mocker.patch.object(C, 'GALAXY_TOKEN_PATH', '/tmp/test_galaxy_token_path')
    yield
    # Cleanup if necessary

def test_galaxy_token_initialization(mock_constants):
    token_value = 'test_token'
    galaxy_token = GalaxyToken(token=token_value)
    
    assert galaxy_token._token == token_value
    assert galaxy_token._config is None
    assert galaxy_token.b_file == to_bytes('/tmp/test_galaxy_token_path', errors='surrogate_or_strict')
