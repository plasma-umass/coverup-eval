# file: tornado/auth.py:553-586
# asked: {"lines": [575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586], "branches": [[577, 578], [577, 579], [579, 580], [579, 581], [581, 582], [581, 583], [583, 584], [583, 585]]}
# gained: {"lines": [575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586], "branches": [[577, 578], [577, 579], [579, 580], [579, 581], [581, 582], [581, 583], [583, 584], [583, 585]]}

import pytest
from unittest.mock import MagicMock, patch
from tornado.web import RequestHandler
from tornado.auth import OAuth2Mixin
from tornado.httputil import url_concat

class TestOAuth2Mixin(OAuth2Mixin):
    _OAUTH_AUTHORIZE_URL = "http://example.com/authorize"

@pytest.fixture
def handler():
    return MagicMock(spec=RequestHandler)

@pytest.fixture
def oauth2_mixin(handler):
    mixin = TestOAuth2Mixin()
    mixin.redirect = handler.redirect
    return mixin

def test_authorize_redirect_with_all_params(oauth2_mixin, handler):
    redirect_uri = "http://example.com/redirect"
    client_id = "test_client_id"
    client_secret = "test_client_secret"
    extra_params = {"state": "xyz"}
    scope = ["email", "profile"]
    response_type = "code"

    with patch.object(oauth2_mixin, '_OAUTH_AUTHORIZE_URL', "http://example.com/authorize"):
        oauth2_mixin.authorize_redirect(
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret,
            extra_params=extra_params,
            scope=scope,
            response_type=response_type
        )

    expected_args = {
        "response_type": response_type,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "state": "xyz",
        "scope": "email profile"
    }
    expected_url = url_concat("http://example.com/authorize", expected_args)
    handler.redirect.assert_called_once_with(expected_url)

def test_authorize_redirect_with_minimal_params(oauth2_mixin, handler):
    response_type = "code"

    with patch.object(oauth2_mixin, '_OAUTH_AUTHORIZE_URL', "http://example.com/authorize"):
        oauth2_mixin.authorize_redirect(response_type=response_type)

    expected_args = {"response_type": response_type}
    expected_url = url_concat("http://example.com/authorize", expected_args)
    handler.redirect.assert_called_once_with(expected_url)

def test_authorize_redirect_with_some_params(oauth2_mixin, handler):
    redirect_uri = "http://example.com/redirect"
    client_id = "test_client_id"
    response_type = "code"

    with patch.object(oauth2_mixin, '_OAUTH_AUTHORIZE_URL', "http://example.com/authorize"):
        oauth2_mixin.authorize_redirect(
            redirect_uri=redirect_uri,
            client_id=client_id,
            response_type=response_type
        )

    expected_args = {
        "response_type": response_type,
        "redirect_uri": redirect_uri,
        "client_id": client_id
    }
    expected_url = url_concat("http://example.com/authorize", expected_args)
    handler.redirect.assert_called_once_with(expected_url)
