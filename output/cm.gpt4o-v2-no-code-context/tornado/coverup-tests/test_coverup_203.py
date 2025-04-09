# file: tornado/auth.py:148-200
# asked: {"lines": [154, 155, 156, 157, 158, 159, 160, 161, 162, 164, 165, 166, 167, 168, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 183, 184, 185, 186, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 200], "branches": [[164, 165], [164, 192], [173, 174], [173, 183], [188, 189], [188, 191], [192, 193], [192, 200]]}
# gained: {"lines": [154, 155, 156, 157, 158, 159, 160, 161, 162, 164, 165, 166, 167, 168, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 183, 184, 185, 186, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 200], "branches": [[164, 165], [164, 192], [173, 174], [188, 189], [188, 191], [192, 193], [192, 200]]}

import pytest
from unittest.mock import Mock, patch
from tornado.auth import OpenIdMixin
from tornado.web import RequestHandler
import urllib.parse

class TestOpenIdMixin:
    @pytest.fixture
    def handler(self):
        handler = Mock(spec=RequestHandler)
        handler.request = Mock()
        handler.request.full_url.return_value = "http://example.com/callback"
        handler.request.host = "example.com"
        return handler

    @pytest.fixture
    def openid_mixin(self, handler):
        class TestHandler(OpenIdMixin, RequestHandler):
            def __init__(self, handler):
                self.request = handler.request
        return TestHandler(handler)

    def test_openid_args_no_ax_attrs_no_oauth_scope(self, openid_mixin, handler):
        callback_uri = "/callback"
        result = openid_mixin._openid_args(callback_uri)
        assert result["openid.ns"] == "http://specs.openid.net/auth/2.0"
        assert result["openid.claimed_id"] == "http://specs.openid.net/auth/2.0/identifier_select"
        assert result["openid.identity"] == "http://specs.openid.net/auth/2.0/identifier_select"
        assert result["openid.return_to"] == "http://example.com/callback"
        assert result["openid.realm"] == "http://example.com/"
        assert result["openid.mode"] == "checkid_setup"

    def test_openid_args_with_ax_attrs(self, openid_mixin, handler):
        callback_uri = "/callback"
        ax_attrs = ["name", "email"]
        result = openid_mixin._openid_args(callback_uri, ax_attrs)
        assert result["openid.ns.ax"] == "http://openid.net/srv/ax/1.0"
        assert result["openid.ax.mode"] == "fetch_request"
        assert result["openid.ax.type.firstname"] == "http://axschema.org/namePerson/first"
        assert result["openid.ax.type.fullname"] == "http://axschema.org/namePerson"
        assert result["openid.ax.type.lastname"] == "http://axschema.org/namePerson/last"
        assert result["openid.ax.type.email"] == "http://axschema.org/contact/email"
        assert result["openid.ax.required"] == "firstname,fullname,lastname,email"

    def test_openid_args_with_oauth_scope(self, openid_mixin, handler):
        callback_uri = "/callback"
        oauth_scope = "test_scope"
        result = openid_mixin._openid_args(callback_uri, oauth_scope=oauth_scope)
        assert result["openid.ns.oauth"] == "http://specs.openid.net/extensions/oauth/1.0"
        assert result["openid.oauth.consumer"] == "example.com"
        assert result["openid.oauth.scope"] == oauth_scope

    def test_openid_args_with_ax_attrs_and_oauth_scope(self, openid_mixin, handler):
        callback_uri = "/callback"
        ax_attrs = ["name", "email"]
        oauth_scope = "test_scope"
        result = openid_mixin._openid_args(callback_uri, ax_attrs, oauth_scope)
        assert result["openid.ns.ax"] == "http://openid.net/srv/ax/1.0"
        assert result["openid.ax.mode"] == "fetch_request"
        assert result["openid.ax.type.firstname"] == "http://axschema.org/namePerson/first"
        assert result["openid.ax.type.fullname"] == "http://axschema.org/namePerson"
        assert result["openid.ax.type.lastname"] == "http://axschema.org/namePerson/last"
        assert result["openid.ax.type.email"] == "http://axschema.org/contact/email"
        assert result["openid.ax.required"] == "firstname,fullname,lastname,email"
        assert result["openid.ns.oauth"] == "http://specs.openid.net/extensions/oauth/1.0"
        assert result["openid.oauth.consumer"] == "example.com"
        assert result["openid.oauth.scope"] == oauth_scope
