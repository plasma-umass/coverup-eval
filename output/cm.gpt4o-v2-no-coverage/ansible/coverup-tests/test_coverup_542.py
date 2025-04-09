# file: lib/ansible/galaxy/token.py:153-158
# asked: {"lines": [153, 154, 155, 156, 157, 158], "branches": [[156, 157], [156, 158]]}
# gained: {"lines": [153, 154, 155, 156, 157, 158], "branches": [[156, 157], [156, 158]]}

import pytest
from unittest.mock import patch
from ansible.galaxy.token import GalaxyToken

@pytest.fixture
def galaxy_token():
    return GalaxyToken()

def test_headers_with_token(galaxy_token):
    with patch.object(GalaxyToken, 'get', return_value='test_token'):
        headers = galaxy_token.headers()
        assert headers == {'Authorization': 'Token test_token'}

def test_headers_without_token(galaxy_token):
    with patch.object(GalaxyToken, 'get', return_value=None):
        headers = galaxy_token.headers()
        assert headers == {}
