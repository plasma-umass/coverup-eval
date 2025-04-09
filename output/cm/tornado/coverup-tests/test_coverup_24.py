# file tornado/auth.py:588-608
# lines [588, 590, 591, 592, 593, 594, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608]
# branches ['598->599', '598->600', '600->601', '600->602', '602->603', '602->604', '604->605', '604->606', '606->607', '606->608']

import pytest
from tornado.auth import OAuth2Mixin
from tornado.httputil import url_concat

class DummyOAuth2Mixin(OAuth2Mixin):
    _OAUTH_ACCESS_TOKEN_URL = "http://example.com/oauth/access_token"

@pytest.fixture
def oauth_mixin():
    return DummyOAuth2Mixin()

def test_oauth_request_token_url(oauth_mixin):
    redirect_uri = "http://example.com/redirect"
    client_id = "dummy_client_id"
    client_secret = "dummy_client_secret"
    code = "dummy_code"
    extra_params = {"extra_param1": "value1", "extra_param2": "value2"}

    # Test with all parameters
    expected_url = (
        "http://example.com/oauth/access_token?"
        "redirect_uri=http%3A%2F%2Fexample.com%2Fredirect&"
        "code=dummy_code&"
        "client_id=dummy_client_id&"
        "client_secret=dummy_client_secret&"
        "extra_param1=value1&"
        "extra_param2=value2"
    )
    assert oauth_mixin._oauth_request_token_url(
        redirect_uri=redirect_uri,
        client_id=client_id,
        client_secret=client_secret,
        code=code,
        extra_params=extra_params
    ) == expected_url

    # Test with only mandatory parameters
    expected_url = "http://example.com/oauth/access_token"
    assert oauth_mixin._oauth_request_token_url() == expected_url

    # Test with some parameters
    expected_url = (
        "http://example.com/oauth/access_token?"
        "redirect_uri=http%3A%2F%2Fexample.com%2Fredirect&"
        "client_id=dummy_client_id"
    )
    assert oauth_mixin._oauth_request_token_url(
        redirect_uri=redirect_uri,
        client_id=client_id
    ) == expected_url
