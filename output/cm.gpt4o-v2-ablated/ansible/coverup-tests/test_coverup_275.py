# file: lib/ansible/galaxy/token.py:106-110
# asked: {"lines": [106, 107, 109, 110], "branches": []}
# gained: {"lines": [106, 107, 109, 110], "branches": []}

import pytest
from ansible.galaxy.token import GalaxyToken
from ansible.module_utils._text import to_bytes
import ansible.constants as C

@pytest.fixture
def mock_constants(monkeypatch):
    monkeypatch.setattr(C, 'GALAXY_TOKEN_PATH', '/tmp/test_galaxy_token_path')

def test_galaxy_token_init_with_token(mock_constants):
    token_value = 'test_token'
    token = GalaxyToken(token=token_value)
    assert token._token == token_value
    assert token.b_file == to_bytes('/tmp/test_galaxy_token_path', errors='surrogate_or_strict')
    assert token._config is None

def test_galaxy_token_init_without_token(mock_constants):
    token = GalaxyToken()
    assert token._token is None
    assert token.b_file == to_bytes('/tmp/test_galaxy_token_path', errors='surrogate_or_strict')
    assert token._config is None
