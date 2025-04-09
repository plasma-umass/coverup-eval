# file: lib/ansible/galaxy/token.py:106-110
# asked: {"lines": [106, 107, 109, 110], "branches": []}
# gained: {"lines": [106, 107, 109, 110], "branches": []}

import pytest
from ansible.galaxy.token import GalaxyToken
from ansible.module_utils._text import to_bytes
import ansible.constants as C

@pytest.fixture
def mock_constants(monkeypatch):
    mock_path = "/mock/path/to/token"
    monkeypatch.setattr(C, 'GALAXY_TOKEN_PATH', mock_path)
    yield mock_path

def test_galaxy_token_init_with_token(mock_constants):
    token_value = "test_token"
    token_instance = GalaxyToken(token=token_value)
    
    assert token_instance._token == token_value
    assert token_instance.b_file == to_bytes(mock_constants, errors='surrogate_or_strict')
    assert token_instance._config is None

def test_galaxy_token_init_without_token(mock_constants):
    token_instance = GalaxyToken()
    
    assert token_instance._token is None
    assert token_instance.b_file == to_bytes(mock_constants, errors='surrogate_or_strict')
    assert token_instance._config is None
