# file tornado/auth.py:553-586
# lines [575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586]
# branches ['577->578', '577->579', '579->580', '579->581', '581->582', '581->583', '583->584', '583->585']

import pytest
from unittest.mock import MagicMock, patch
from tornado.web import RequestHandler
from tornado.auth import OAuth2Mixin
from tornado.httputil import url_concat

class TestOAuth2Mixin(OAuth2Mixin):
    _OAUTH_AUTHORIZE_URL = "http://example.com/authorize"

@pytest.fixture
def mock_handler():
    handler = MagicMock(spec=RequestHandler)
    handler.request = MagicMock()
    return handler

def test_authorize_redirect(mock_handler):
    mixin = TestOAuth2Mixin()
    mixin.__dict__.update(mock_handler.__dict__)
    mixin.redirect = mock_handler.redirect

    redirect_uri = "http://example.com/redirect"
    client_id = "test_client_id"
    client_secret = "test_client_secret"
    extra_params = {"state": "xyz"}
    scope = ["email", "profile"]
    response_type = "code"

    with patch.object(mixin, 'redirect') as mock_redirect:
        mixin.authorize_redirect(
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
        expected_url = url_concat(mixin._OAUTH_AUTHORIZE_URL, expected_args)
        mock_redirect.assert_called_once_with(expected_url)
