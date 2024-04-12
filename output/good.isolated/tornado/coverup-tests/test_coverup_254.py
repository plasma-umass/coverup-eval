# file tornado/auth.py:148-200
# lines [154, 155, 156, 157, 158, 159, 160, 161, 162, 164, 165, 166, 167, 168, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 183, 184, 185, 186, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 200]
# branches ['164->165', '164->192', '173->174', '173->183', '188->189', '188->191', '192->193', '192->200']

import pytest
from unittest.mock import Mock
from tornado.web import RequestHandler
from tornado.auth import OpenIdMixin
from typing import Dict, Iterable, Optional

class TestOpenIdMixin:
    @pytest.fixture
    def mock_handler(self, mocker):
        request_mock = mocker.Mock()
        request_mock.full_url.return_value = 'http://example.com/auth/login'
        request_mock.host = 'example.com:80'
        handler_mock = mocker.Mock(spec=RequestHandler)
        handler_mock.request = request_mock
        return handler_mock

    def test_openid_args_with_ax_attrs_and_oauth_scope(self, mock_handler):
        mixin = OpenIdMixin()
        mixin.request = mock_handler.request
        callback_uri = '/auth/openid/callback'
        ax_attrs = ['email', 'language', 'username']
        oauth_scope = 'openid'

        args = mixin._openid_args(callback_uri, ax_attrs, oauth_scope)

        # Assertions to verify the openid arguments
        assert args['openid.return_to'] == 'http://example.com/auth/openid/callback'
        assert args['openid.realm'] == 'http://example.com/'
        assert args['openid.ns.ax'] == 'http://openid.net/srv/ax/1.0'
        assert args['openid.ax.mode'] == 'fetch_request'
        assert args['openid.ax.required'] == 'email,language,username'
        assert args['openid.ax.type.email'] == 'http://axschema.org/contact/email'
        assert args['openid.ax.type.language'] == 'http://axschema.org/pref/language'
        assert args['openid.ax.type.username'] == 'http://axschema.org/namePerson/friendly'
        assert args['openid.ns.oauth'] == 'http://specs.openid.net/extensions/oauth/1.0'
        assert args['openid.oauth.consumer'] == 'example.com'
        assert args['openid.oauth.scope'] == 'openid'

        # Clean up
        del mixin.request
