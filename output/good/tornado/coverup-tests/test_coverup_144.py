# file tornado/auth.py:264-270
# lines [264, 270]
# branches []

import pytest
from tornado import httpclient
from tornado.auth import OpenIdMixin

@pytest.fixture
def mock_http_client(mocker):
    client = mocker.Mock(spec=httpclient.AsyncHTTPClient)
    mocker.patch.object(httpclient, 'AsyncHTTPClient', return_value=client)
    return client

def test_get_auth_http_client(mock_http_client):
    mixin = OpenIdMixin()
    client = mixin.get_auth_http_client()
    assert client is mock_http_client
