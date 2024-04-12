# file tornado/auth.py:553-586
# lines [553, 555, 556, 557, 558, 559, 560, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586]
# branches ['577->578', '577->579', '579->580', '579->581', '581->582', '581->583', '583->584', '583->585']

import pytest
from tornado.web import Application, RequestHandler
from tornado.auth import OAuth2Mixin
from unittest.mock import Mock, create_autospec
from tornado.httputil import HTTPServerRequest

class DummyOAuth2Mixin(OAuth2Mixin, RequestHandler):
    _OAUTH_AUTHORIZE_URL = "http://example.com/authorize"

@pytest.fixture
def mock_handler():
    application = Application()
    request = create_autospec(HTTPServerRequest, instance=True, method="GET", uri="/auth", connection=Mock())
    handler = DummyOAuth2Mixin(application, request)
    handler.redirect = Mock()
    return handler

def test_authorize_redirect_full_coverage(mock_handler):
    # Test with all parameters
    mock_handler.authorize_redirect(
        redirect_uri="http://example.com/redirect",
        client_id="client_id_example",
        client_secret="client_secret_example",
        extra_params={"extra_param": "extra_value"},
        scope=["read", "write"],
        response_type="token"
    )
    expected_url = (
        "http://example.com/authorize?"
        "response_type=token&"
        "redirect_uri=http%3A%2F%2Fexample.com%2Fredirect&"
        "client_id=client_id_example&"
        "extra_param=extra_value&"
        "scope=read+write"
    )
    mock_handler.redirect.assert_called_once_with(expected_url)

    # Test with only required parameters
    mock_handler.redirect.reset_mock()
    mock_handler.authorize_redirect()
    expected_url = "http://example.com/authorize?response_type=code"
    mock_handler.redirect.assert_called_once_with(expected_url)
