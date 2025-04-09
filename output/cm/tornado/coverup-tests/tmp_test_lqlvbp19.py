import pytest
from tornado.web import RequestHandler
from tornado.auth import OAuth2Mixin
from unittest.mock import Mock

class DummyOAuth2Mixin(OAuth2Mixin, RequestHandler):
    _OAUTH_AUTHORIZE_URL = "http://example.com/authorize"

@pytest.fixture
def mock_handler(mocker):
    handler = DummyOAuth2Mixin()
    handler.redirect = Mock()
    return handler

def test_authorize_redirect_full_coverage(mock_handler):
    mock_handler.authorize_redirect(
        redirect_uri="http://example.com/redirect",
        client_id="client_id_example",
        client_secret="client_secret_example",
        extra_params={"extra_param1": "value1"},
        scope=["scope1", "scope2"],
        response_type="token"
    )
    
    expected_args = {
        "response_type": "token",
        "redirect_uri": "http://example.com/redirect",
        "client_id": "client_id_example",
        "scope": "scope1 scope2",
        "extra_param1": "value1"
    }
    expected_url = "http://example.com/authorize?" + "&".join(
        f"{key}={value}" for key, value in expected_args.items()
    )
    
    mock_handler.redirect.assert_called_once_with(expected_url)
