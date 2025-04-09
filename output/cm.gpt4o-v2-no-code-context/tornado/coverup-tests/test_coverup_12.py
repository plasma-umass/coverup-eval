# file: tornado/auth.py:588-608
# asked: {"lines": [588, 590, 591, 592, 593, 594, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608], "branches": [[598, 599], [598, 600], [600, 601], [600, 602], [602, 603], [602, 604], [604, 605], [604, 606], [606, 607], [606, 608]]}
# gained: {"lines": [588, 590, 591, 592, 593, 594, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608], "branches": [[598, 599], [598, 600], [600, 601], [600, 602], [602, 603], [602, 604], [604, 605], [604, 606], [606, 607], [606, 608]]}

import pytest
from tornado.auth import OAuth2Mixin
from tornado.httputil import url_concat
from urllib.parse import parse_qs, urlparse

class TestOAuth2Mixin:
    @pytest.fixture
    def oauth_mixin(self):
        class TestOAuth2(OAuth2Mixin):
            _OAUTH_ACCESS_TOKEN_URL = "https://example.com/token"
        return TestOAuth2()

    def test_oauth_request_token_url_all_params(self, oauth_mixin):
        url = oauth_mixin._oauth_request_token_url(
            redirect_uri="http://localhost/callback",
            client_id="test_client_id",
            client_secret="test_client_secret",
            code="test_code",
            extra_params={"scope": "email"}
        )
        expected_url = url_concat(
            "https://example.com/token",
            {
                "redirect_uri": "http://localhost/callback",
                "client_id": "test_client_id",
                "client_secret": "test_client_secret",
                "code": "test_code",
                "scope": "email"
            }
        )
        assert parse_qs(urlparse(url).query) == parse_qs(urlparse(expected_url).query)

    def test_oauth_request_token_url_no_extra_params(self, oauth_mixin):
        url = oauth_mixin._oauth_request_token_url(
            redirect_uri="http://localhost/callback",
            client_id="test_client_id",
            client_secret="test_client_secret",
            code="test_code"
        )
        expected_url = url_concat(
            "https://example.com/token",
            {
                "redirect_uri": "http://localhost/callback",
                "client_id": "test_client_id",
                "client_secret": "test_client_secret",
                "code": "test_code"
            }
        )
        assert parse_qs(urlparse(url).query) == parse_qs(urlparse(expected_url).query)

    def test_oauth_request_token_url_minimal_params(self, oauth_mixin):
        url = oauth_mixin._oauth_request_token_url()
        expected_url = "https://example.com/token"
        assert url == expected_url

    def test_oauth_request_token_url_some_params(self, oauth_mixin):
        url = oauth_mixin._oauth_request_token_url(
            client_id="test_client_id",
            code="test_code"
        )
        expected_url = url_concat(
            "https://example.com/token",
            {
                "client_id": "test_client_id",
                "code": "test_code"
            }
        )
        assert parse_qs(urlparse(url).query) == parse_qs(urlparse(expected_url).query)
