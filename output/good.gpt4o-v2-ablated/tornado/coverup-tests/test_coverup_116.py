# file: tornado/auth.py:588-608
# asked: {"lines": [596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608], "branches": [[598, 599], [598, 600], [600, 601], [600, 602], [602, 603], [602, 604], [604, 605], [604, 606], [606, 607], [606, 608]]}
# gained: {"lines": [596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608], "branches": [[598, 599], [598, 600], [600, 601], [600, 602], [602, 603], [602, 604], [604, 605], [604, 606], [606, 607], [606, 608]]}

import pytest
from tornado.auth import OAuth2Mixin
from tornado.httputil import url_concat

class TestOAuth2Mixin:
    @pytest.fixture
    def oauth2_mixin(self):
        class TestOAuth2(OAuth2Mixin):
            _OAUTH_ACCESS_TOKEN_URL = "https://example.com/token"
        return TestOAuth2()

    def test_oauth_request_token_url_no_params(self, oauth2_mixin):
        url = oauth2_mixin._oauth_request_token_url()
        assert url == "https://example.com/token"

    def test_oauth_request_token_url_with_redirect_uri(self, oauth2_mixin):
        url = oauth2_mixin._oauth_request_token_url(redirect_uri="https://example.com/redirect")
        assert url == "https://example.com/token?redirect_uri=https%3A%2F%2Fexample.com%2Fredirect"

    def test_oauth_request_token_url_with_code(self, oauth2_mixin):
        url = oauth2_mixin._oauth_request_token_url(code="test_code")
        assert url == "https://example.com/token?code=test_code"

    def test_oauth_request_token_url_with_client_id(self, oauth2_mixin):
        url = oauth2_mixin._oauth_request_token_url(client_id="test_client_id")
        assert url == "https://example.com/token?client_id=test_client_id"

    def test_oauth_request_token_url_with_client_secret(self, oauth2_mixin):
        url = oauth2_mixin._oauth_request_token_url(client_secret="test_client_secret")
        assert url == "https://example.com/token?client_secret=test_client_secret"

    def test_oauth_request_token_url_with_extra_params(self, oauth2_mixin):
        extra_params = {"scope": "email", "state": "xyz"}
        url = oauth2_mixin._oauth_request_token_url(extra_params=extra_params)
        assert url == "https://example.com/token?scope=email&state=xyz"

    def test_oauth_request_token_url_with_all_params(self, oauth2_mixin):
        url = oauth2_mixin._oauth_request_token_url(
            redirect_uri="https://example.com/redirect",
            client_id="test_client_id",
            client_secret="test_client_secret",
            code="test_code",
            extra_params={"scope": "email", "state": "xyz"}
        )
        expected_url = (
            "https://example.com/token?redirect_uri=https%3A%2F%2Fexample.com%2Fredirect"
            "&code=test_code&client_id=test_client_id&client_secret=test_client_secret"
            "&scope=email&state=xyz"
        )
        assert url == expected_url
