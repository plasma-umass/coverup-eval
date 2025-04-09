# file: tornado/auth.py:553-586
# asked: {"lines": [553, 555, 556, 557, 558, 559, 560, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586], "branches": [[577, 578], [577, 579], [579, 580], [579, 581], [581, 582], [581, 583], [583, 584], [583, 585]]}
# gained: {"lines": [553, 555, 556, 557, 558, 559, 560, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586], "branches": [[577, 578], [577, 579], [579, 580], [579, 581], [581, 582], [581, 583], [583, 584], [583, 585]]}

import pytest
from unittest.mock import MagicMock, patch
from tornado.web import RequestHandler
from tornado.auth import OAuth2Mixin
from tornado.httputil import url_concat

class MockHandler(RequestHandler, OAuth2Mixin):
    _OAUTH_AUTHORIZE_URL = "http://example.com/authorize"

@pytest.fixture
def mock_handler():
    return MockHandler(MagicMock(), MagicMock())

def test_authorize_redirect_basic(mock_handler, mocker):
    mock_redirect = mocker.patch.object(mock_handler, 'redirect')
    mock_handler.authorize_redirect()
    mock_redirect.assert_called_once_with("http://example.com/authorize?response_type=code")

def test_authorize_redirect_with_redirect_uri(mock_handler, mocker):
    mock_redirect = mocker.patch.object(mock_handler, 'redirect')
    mock_handler.authorize_redirect(redirect_uri="http://example.com/callback")
    mock_redirect.assert_called_once_with("http://example.com/authorize?response_type=code&redirect_uri=http%3A%2F%2Fexample.com%2Fcallback")

def test_authorize_redirect_with_client_id(mock_handler, mocker):
    mock_redirect = mocker.patch.object(mock_handler, 'redirect')
    mock_handler.authorize_redirect(client_id="test_client_id")
    mock_redirect.assert_called_once_with("http://example.com/authorize?response_type=code&client_id=test_client_id")

def test_authorize_redirect_with_extra_params(mock_handler, mocker):
    mock_redirect = mocker.patch.object(mock_handler, 'redirect')
    extra_params = {"state": "xyz"}
    mock_handler.authorize_redirect(extra_params=extra_params)
    mock_redirect.assert_called_once_with("http://example.com/authorize?response_type=code&state=xyz")

def test_authorize_redirect_with_scope(mock_handler, mocker):
    mock_redirect = mocker.patch.object(mock_handler, 'redirect')
    scope = ["email", "profile"]
    mock_handler.authorize_redirect(scope=scope)
    mock_redirect.assert_called_once_with("http://example.com/authorize?response_type=code&scope=email+profile")

def test_authorize_redirect_with_all_params(mock_handler, mocker):
    mock_redirect = mocker.patch.object(mock_handler, 'redirect')
    mock_handler.authorize_redirect(
        redirect_uri="http://example.com/callback",
        client_id="test_client_id",
        client_secret="test_client_secret",
        extra_params={"state": "xyz"},
        scope=["email", "profile"],
        response_type="token"
    )
    expected_url = url_concat("http://example.com/authorize", {
        "response_type": "token",
        "redirect_uri": "http://example.com/callback",
        "client_id": "test_client_id",
        "state": "xyz",
        "scope": "email profile"
    })
    mock_redirect.assert_called_once_with(expected_url)
