# file tornado/auth.py:148-200
# lines [154, 155, 156, 157, 158, 159, 160, 161, 162, 164, 165, 166, 167, 168, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 183, 184, 185, 186, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 200]
# branches ['164->165', '164->192', '173->174', '173->183', '188->189', '188->191', '192->193', '192->200']

import pytest
from unittest.mock import Mock, patch
from tornado.auth import OpenIdMixin
from tornado.web import RequestHandler
import urllib.parse

class TestOpenIdMixin:
    @patch('tornado.web.RequestHandler')
    def test_openid_args(self, mock_request_handler):
        # Mock the request handler and its request
        mock_request = Mock()
        mock_request.full_url.return_value = "http://example.com/callback"
        mock_request.host = "example.com"
        mock_request_handler.request = mock_request

        # Create an instance of OpenIdMixin
        class MockHandler(OpenIdMixin, RequestHandler):
            def __init__(self, request):
                self.request = request

        mixin = MockHandler(mock_request)

        # Test with ax_attrs and oauth_scope
        ax_attrs = ["name", "email", "language"]
        oauth_scope = "test_scope"
        result = mixin._openid_args("/callback", ax_attrs, oauth_scope)

        # Assertions to verify the result
        assert result["openid.ns"] == "http://specs.openid.net/auth/2.0"
        assert result["openid.claimed_id"] == "http://specs.openid.net/auth/2.0/identifier_select"
        assert result["openid.identity"] == "http://specs.openid.net/auth/2.0/identifier_select"
        assert result["openid.return_to"] == "http://example.com/callback"
        assert result["openid.realm"] == "http://example.com/"
        assert result["openid.mode"] == "checkid_setup"
        assert result["openid.ns.ax"] == "http://openid.net/srv/ax/1.0"
        assert result["openid.ax.mode"] == "fetch_request"
        assert result["openid.ax.type.firstname"] == "http://axschema.org/namePerson/first"
        assert result["openid.ax.type.fullname"] == "http://axschema.org/namePerson"
        assert result["openid.ax.type.lastname"] == "http://axschema.org/namePerson/last"
        assert result["openid.ax.type.email"] == "http://axschema.org/contact/email"
        assert result["openid.ax.type.language"] == "http://axschema.org/pref/language"
        assert result["openid.ax.required"] == "firstname,fullname,lastname,email,language"
        assert result["openid.ns.oauth"] == "http://specs.openid.net/extensions/oauth/1.0"
        assert result["openid.oauth.consumer"] == "example.com"
        assert result["openid.oauth.scope"] == "test_scope"

        # Test without ax_attrs and oauth_scope
        result = mixin._openid_args("/callback")

        # Assertions to verify the result
        assert result["openid.ns"] == "http://specs.openid.net/auth/2.0"
        assert result["openid.claimed_id"] == "http://specs.openid.net/auth/2.0/identifier_select"
        assert result["openid.identity"] == "http://specs.openid.net/auth/2.0/identifier_select"
        assert result["openid.return_to"] == "http://example.com/callback"
        assert result["openid.realm"] == "http://example.com/"
        assert result["openid.mode"] == "checkid_setup"
        assert "openid.ns.ax" not in result
        assert "openid.ax.mode" not in result
        assert "openid.ax.type.firstname" not in result
        assert "openid.ax.type.fullname" not in result
        assert "openid.ax.type.lastname" not in result
        assert "openid.ax.type.email" not in result
        assert "openid.ax.type.language" not in result
        assert "openid.ax.required" not in result
        assert "openid.ns.oauth" not in result
        assert "openid.oauth.consumer" not in result
        assert "openid.oauth.scope" not in result
