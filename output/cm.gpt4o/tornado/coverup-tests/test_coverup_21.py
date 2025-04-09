# file tornado/auth.py:588-608
# lines [588, 590, 591, 592, 593, 594, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608]
# branches ['598->599', '598->600', '600->601', '600->602', '602->603', '602->604', '604->605', '604->606', '606->607', '606->608']

import pytest
from tornado.auth import OAuth2Mixin
from tornado.httputil import url_concat
from urllib.parse import unquote

class TestOAuth2Mixin:
    @pytest.fixture
    def oauth2_mixin(self, mocker):
        class TestOAuth2(OAuth2Mixin):
            _OAUTH_ACCESS_TOKEN_URL = "https://example.com/token"
        
        return TestOAuth2()

    def test_oauth_request_token_url(self, oauth2_mixin):
        redirect_uri = "https://example.com/redirect"
        client_id = "test_client_id"
        client_secret = "test_client_secret"
        code = "test_code"
        extra_params = {"scope": "email", "state": "xyz"}

        expected_params = {
            "redirect_uri": redirect_uri,
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "scope": "email",
            "state": "xyz"
        }

        result_url = oauth2_mixin._oauth_request_token_url(
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            extra_params=extra_params
        )

        result_base_url, result_query = result_url.split('?', 1)
        result_params = {param.split('=')[0]: unquote(param.split('=')[1]) for param in result_query.split('&')}

        assert result_base_url == "https://example.com/token"
        assert result_params == expected_params
