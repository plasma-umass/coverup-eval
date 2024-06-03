# file tornado/auth.py:588-608
# lines []
# branches ['598->600', '600->602', '602->604', '604->606', '606->608']

import pytest
from tornado.auth import OAuth2Mixin
from tornado.httputil import url_concat

class TestOAuth2Mixin(OAuth2Mixin):
    _OAUTH_ACCESS_TOKEN_URL = "https://example.com/oauth/access_token"

@pytest.fixture
def oauth2_mixin():
    return TestOAuth2Mixin()

def test_oauth_request_token_url_all_params(oauth2_mixin):
    redirect_uri = "https://example.com/redirect"
    client_id = "test_client_id"
    client_secret = "test_client_secret"
    code = "test_code"
    extra_params = {"scope": "email", "state": "xyz"}

    url = oauth2_mixin._oauth_request_token_url(
        redirect_uri=redirect_uri,
        client_id=client_id,
        client_secret=client_secret,
        code=code,
        extra_params=extra_params
    )

    expected_url = url_concat(
        oauth2_mixin._OAUTH_ACCESS_TOKEN_URL,
        {
            "redirect_uri": redirect_uri,
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "scope": "email",
            "state": "xyz"
        }
    )

    # Split the URLs into components and compare them as sets to avoid order issues
    url_components = set(url.split('&'))
    expected_url_components = set(expected_url.split('&'))

    assert url_components == expected_url_components

def test_oauth_request_token_url_no_params(oauth2_mixin):
    url = oauth2_mixin._oauth_request_token_url()

    expected_url = oauth2_mixin._OAUTH_ACCESS_TOKEN_URL

    assert url == expected_url

def test_oauth_request_token_url_some_params(oauth2_mixin):
    redirect_uri = "https://example.com/redirect"
    client_id = "test_client_id"

    url = oauth2_mixin._oauth_request_token_url(
        redirect_uri=redirect_uri,
        client_id=client_id
    )

    expected_url = url_concat(
        oauth2_mixin._OAUTH_ACCESS_TOKEN_URL,
        {
            "redirect_uri": redirect_uri,
            "client_id": client_id
        }
    )

    # Split the URLs into components and compare them as sets to avoid order issues
    url_components = set(url.split('&'))
    expected_url_components = set(expected_url.split('&'))

    assert url_components == expected_url_components
