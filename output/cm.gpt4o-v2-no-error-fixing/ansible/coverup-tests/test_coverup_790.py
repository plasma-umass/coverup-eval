# file: lib/ansible/galaxy/token.py:153-158
# asked: {"lines": [154, 155, 156, 157, 158], "branches": [[156, 157], [156, 158]]}
# gained: {"lines": [154, 155, 156, 157, 158], "branches": [[156, 157], [156, 158]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.token import GalaxyToken

@pytest.fixture
def mock_config():
    with patch.object(GalaxyToken, 'config', new_callable=MagicMock) as mock_config:
        yield mock_config

def test_headers_with_token(mock_config):
    token_instance = GalaxyToken()
    mock_config.get.return_value = 'test_token'
    token_instance.token_type = 'Bearer'

    headers = token_instance.headers()

    assert headers == {'Authorization': 'Bearer test_token'}

def test_headers_without_token(mock_config):
    token_instance = GalaxyToken()
    mock_config.get.return_value = None

    headers = token_instance.headers()

    assert headers == {}
