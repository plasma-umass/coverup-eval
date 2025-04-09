# file: tornado/auth.py:588-608
# asked: {"lines": [588, 590, 591, 592, 593, 594, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608], "branches": [[598, 599], [598, 600], [600, 601], [600, 602], [602, 603], [602, 604], [604, 605], [604, 606], [606, 607], [606, 608]]}
# gained: {"lines": [588, 590, 591, 592, 593, 594, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608], "branches": [[598, 599], [598, 600], [600, 601], [600, 602], [602, 603], [602, 604], [604, 605], [604, 606], [606, 607], [606, 608]]}

import pytest
from tornado.auth import OAuth2Mixin
from tornado.httputil import url_concat

class TestOAuth2Mixin:
    @pytest.fixture
    def oauth_mixin(self):
        class TestOAuth2(OAuth2Mixin):
            _OAUTH_ACCESS_TOKEN_URL = "http://example.com/token"
        return TestOAuth2()

    def test_oauth_request_token_url_no_params(self, oauth_mixin):
        result = oauth_mixin._oauth_request_token_url()
        assert result == "http://example.com/token"

    def test_oauth_request_token_url_with_redirect_uri(self, oauth_mixin):
        result = oauth_mixin._oauth_request_token_url(redirect_uri="http://example.com/redirect")
        assert result == "http://example.com/token?redirect_uri=http%3A%2F%2Fexample.com%2Fredirect"

    def test_oauth_request_token_url_with_code(self, oauth_mixin):
        result = oauth_mixin._oauth_request_token_url(code="authcode")
        assert result == "http://example.com/token?code=authcode"

    def test_oauth_request_token_url_with_client_id(self, oauth_mixin):
        result = oauth_mixin._oauth_request_token_url(client_id="clientid")
        assert result == "http://example.com/token?client_id=clientid"

    def test_oauth_request_token_url_with_client_secret(self, oauth_mixin):
        result = oauth_mixin._oauth_request_token_url(client_secret="clientsecret")
        assert result == "http://example.com/token?client_secret=clientsecret"

    def test_oauth_request_token_url_with_extra_params(self, oauth_mixin):
        extra_params = {"scope": "email", "state": "xyz"}
        result = oauth_mixin._oauth_request_token_url(extra_params=extra_params)
        assert result == "http://example.com/token?scope=email&state=xyz"

    def test_oauth_request_token_url_with_all_params(self, oauth_mixin):
        extra_params = {"scope": "email", "state": "xyz"}
        result = oauth_mixin._oauth_request_token_url(
            redirect_uri="http://example.com/redirect",
            client_id="clientid",
            client_secret="clientsecret",
            code="authcode",
            extra_params=extra_params
        )
        assert result == ("http://example.com/token?redirect_uri=http%3A%2F%2Fexample.com%2Fredirect"
                          "&code=authcode&client_id=clientid&client_secret=clientsecret"
                          "&scope=email&state=xyz")
