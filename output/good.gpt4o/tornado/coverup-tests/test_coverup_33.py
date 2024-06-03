# file tornado/auth.py:202-262
# lines [202, 205, 206, 207, 210, 211, 212, 213, 214, 216, 217, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262]
# branches ['206->207', '206->210', '211->212', '211->219', '212->211', '212->216', '220->221', '220->222', '224->225', '224->229', '225->224', '225->226', '229->230', '229->231', '241->242', '241->244', '244->245', '244->247', '247->248', '247->249', '249->250', '249->251', '251->252', '251->253', '253->254', '253->255', '255->256', '255->257', '257->258', '257->259', '260->261', '260->262']

import pytest
from unittest.mock import MagicMock
from tornado.web import RequestHandler, Application
from tornado.httpclient import HTTPResponse, HTTPRequest
from tornado.auth import OpenIdMixin, AuthError

class MockRequestHandler(RequestHandler, OpenIdMixin):
    def __init__(self, application, request, **kwargs):
        super().__init__(application=application, request=request, **kwargs)
        self.request = request

    def get_argument(self, name, default=None):
        return self.request.arguments.get(name, [default])[0]

@pytest.fixture
def mock_request_handler(mocker):
    application = Application()
    request = MagicMock()
    request.arguments = {
        "openid.ns.ax": ["http://openid.net/srv/ax/1.0"],
        "openid.ax.type.email": ["http://axschema.org/contact/email"],
        "openid.ax.value.email": ["test@example.com"],
        "openid.ax.type.name": ["http://axschema.org/namePerson"],
        "openid.ax.value.name": ["Test User"],
        "openid.ax.type.first": ["http://axschema.org/namePerson/first"],
        "openid.ax.value.first": ["Test"],
        "openid.ax.type.last": ["http://axschema.org/namePerson/last"],
        "openid.ax.value.last": ["User"],
        "openid.ax.type.friendly": ["http://axschema.org/namePerson/friendly"],
        "openid.ax.value.friendly": ["testuser"],
        "openid.ax.type.language": ["http://axschema.org/pref/language"],
        "openid.ax.value.language": ["en"],
        "openid.claimed_id": ["http://example.com/claimed_id"]
    }
    handler = MockRequestHandler(application, request)
    return handler

def test_on_authentication_verified_valid_response(mock_request_handler):
    response = MagicMock(spec=HTTPResponse)
    response.body = b"is_valid:true"
    user = mock_request_handler._on_authentication_verified(response)
    
    assert user["email"] == "test@example.com"
    assert user["name"] == "Test User"
    assert user["first_name"] == "Test"
    assert user["last_name"] == "User"
    assert user["username"] == "testuser"
    assert user["locale"] == "en"
    assert user["claimed_id"] == "http://example.com/claimed_id"

def test_on_authentication_verified_invalid_response(mock_request_handler):
    response = MagicMock(spec=HTTPResponse)
    response.body = b"is_valid:false"
    
    with pytest.raises(AuthError):
        mock_request_handler._on_authentication_verified(response)
