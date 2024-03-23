# file lib/ansible/galaxy/token.py:112-121
# lines [114, 115, 118, 119, 121]
# branches ['114->115', '114->118', '118->119', '118->121']

import pytest
from ansible.galaxy.token import GalaxyToken, NoTokenSentinel

class TestGalaxyToken:
    @pytest.fixture
    def mock_read(self, mocker):
        mocker.patch.object(GalaxyToken, '_read', return_value={})

    @pytest.fixture
    def token_instance(self, mock_read):
        token = GalaxyToken()
        token._config = None
        return token

    def test_config_with_no_token(self, token_instance):
        assert token_instance.config == {}, "Config should be empty dictionary when no token is set"

    def test_config_with_token_sentinel(self, token_instance):
        token_instance._token = NoTokenSentinel
        assert token_instance.config == {'token': None}, "Config should have 'token' set to None when NoTokenSentinel is used"

    def test_config_with_actual_token(self, token_instance):
        token_instance._token = 'actual_token'
        assert token_instance.config == {'token': 'actual_token'}, "Config should have 'token' set to the actual token value"
