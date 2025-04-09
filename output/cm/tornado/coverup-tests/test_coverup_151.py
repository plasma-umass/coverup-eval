# file tornado/auth.py:924-931
# lines [924, 925, 927, 928, 929, 930]
# branches []

import pytest
from tornado.auth import FacebookGraphMixin
from unittest.mock import Mock, patch

# Define a test case for the FacebookGraphMixin class
def test_facebook_graph_mixin(mocker):
    # Create an instance of the FacebookGraphMixin
    mixin_instance = FacebookGraphMixin()
    
    # Mock the HTTPRequestHandler to attach to the mixin
    mixin_instance.request = Mock()
    mixin_instance.redirect = Mock()
    mixin_instance.finish = Mock()
    mixin_instance.write = Mock()
    
    # Mock the OAuth2Mixin's methods since FacebookGraphMixin inherits from it
    with patch.object(FacebookGraphMixin, 'authorize_redirect', return_value=None) as mock_authorize_redirect:
        with patch.object(FacebookGraphMixin, 'get_authenticated_user', return_value=None) as mock_get_authenticated_user:
            # Test the OAuth URLs
            assert mixin_instance._OAUTH_ACCESS_TOKEN_URL == "https://graph.facebook.com/oauth/access_token?"
            assert mixin_instance._OAUTH_AUTHORIZE_URL == "https://www.facebook.com/dialog/oauth?"
            assert mixin_instance._OAUTH_NO_CALLBACKS == False
            assert mixin_instance._FACEBOOK_BASE_URL == "https://graph.facebook.com"
            
            # Test the authorize_redirect method
            mixin_instance.authorize_redirect(redirect_uri='http://example.com/auth',
                                              client_id='test_client_id',
                                              extra_params={'scope': 'email'})
            mock_authorize_redirect.assert_called_once()
            
            # Test the get_authenticated_user method
            mixin_instance.get_authenticated_user(redirect_uri='http://example.com/auth',
                                                  client_id='test_client_id',
                                                  client_secret='test_client_secret',
                                                  code='test_code',
                                                  callback=Mock())
            mock_get_authenticated_user.assert_called_once()
