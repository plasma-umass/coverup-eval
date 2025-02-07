# file: lib/ansible/galaxy/token.py:153-158
# asked: {"lines": [153, 154, 155, 156, 157, 158], "branches": [[156, 157], [156, 158]]}
# gained: {"lines": [153, 154, 155, 156, 157, 158], "branches": [[156, 157], [156, 158]]}

import pytest
from ansible.galaxy.token import GalaxyToken

@pytest.fixture
def galaxy_token():
    return GalaxyToken()

def test_headers_with_token(monkeypatch, galaxy_token):
    def mock_get():
        return "mocked_token"
    
    monkeypatch.setattr(galaxy_token, "get", mock_get)
    headers = galaxy_token.headers()
    assert headers == {'Authorization': 'Token mocked_token'}

def test_headers_without_token(monkeypatch, galaxy_token):
    def mock_get():
        return None
    
    monkeypatch.setattr(galaxy_token, "get", mock_get)
    headers = galaxy_token.headers()
    assert headers == {}
