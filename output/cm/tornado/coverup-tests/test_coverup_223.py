# file tornado/auth.py:202-262
# lines [205, 206, 207, 210, 211, 212, 213, 214, 216, 217, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262]
# branches ['206->207', '206->210', '211->212', '211->219', '212->211', '212->216', '220->221', '220->222', '224->225', '224->229', '225->224', '225->226', '229->230', '229->231', '241->242', '241->244', '244->245', '244->247', '247->248', '247->249', '249->250', '249->251', '251->252', '251->253', '253->254', '253->255', '255->256', '255->257', '257->258', '257->259', '260->261', '260->262']

import pytest
from tornado import httpclient
from tornado.web import RequestHandler, Application
from unittest.mock import Mock, create_autospec
from tornado.auth import OpenIdMixin, AuthError
from tornado.httputil import HTTPServerRequest

class DummyHandler(RequestHandler, OpenIdMixin):
    def initialize(self):
        self.request = create_autospec(HTTPServerRequest, instance=True)
        self.request.arguments = {}

    def get_argument(self, name, default=None):
        return self.request.arguments.get(name, [default])[0]

@pytest.fixture
def mock_handler():
    application = Application()
    request = HTTPServerRequest(method='GET', uri='/auth/login', connection=Mock())
    handler = DummyHandler(application, request)
    handler._transforms = []  # This can be an empty list for testing purposes
    return handler

def test_on_authentication_verified(mock_handler):
    # Mock the HTTPResponse to simulate a valid OpenID response
    response = Mock(spec=httpclient.HTTPResponse)
    response.body = b"is_valid:true"

    # Set up the arguments to simulate attribute exchange
    ax_ns = "http://openid.net/srv/ax/1.0"
    mock_handler.request.arguments = {
        "openid.ns.ax": [ax_ns],
        "openid.ax.type.email": ["http://axschema.org/contact/email"],
        "openid.ax.value.email": ["test@example.com"],
        "openid.ax.type.first": ["http://axschema.org/namePerson/first"],
        "openid.ax.value.first": ["Test"],
        "openid.ax.type.last": ["http://axschema.org/namePerson/last"],
        "openid.ax.value.last": ["User"],
        "openid.ax.type.username": ["http://axschema.org/namePerson/friendly"],
        "openid.ax.value.username": ["testuser"],
        "openid.ax.type.locale": ["http://axschema.org/pref/language"],
        "openid.ax.value.locale": ["en-US"],
        "openid.claimed_id": ["http://example.com/testuser"]
    }

    # Call the method under test
    user_info = mock_handler._on_authentication_verified(response)

    # Assertions to verify postconditions
    assert user_info["email"] == "test@example.com"
    assert user_info["first_name"] == "Test"
    assert user_info["last_name"] == "User"
    assert user_info["username"] == "testuser"
    assert user_info["locale"] == "en-us"  # Note: the method under test calls .lower()
    assert user_info["claimed_id"] == "http://example.com/testuser"
    assert user_info["name"] == "Test User"

def test_on_authentication_verified_invalid_response(mock_handler):
    # Mock the HTTPResponse to simulate an invalid OpenID response
    response = Mock(spec=httpclient.HTTPResponse)
    response.body = b"is_valid:false"

    # Expect an AuthError to be raised due to invalid response
    with pytest.raises(AuthError):
        mock_handler._on_authentication_verified(response)
