# file tornado/httpclient.py:314-336
# lines [336]
# branches []

import pytest
from tornado.httpclient import AsyncHTTPClient

@pytest.fixture
def reset_async_http_client():
    # Store the original configuration
    original_impl = AsyncHTTPClient._save_configuration()
    yield
    # Restore the original configuration after the test
    AsyncHTTPClient._restore_configuration(original_impl)

def test_configure_calls_super_configure(mocker, reset_async_http_client):
    mock_super_configure = mocker.patch('tornado.httpclient.Configurable.configure')
    AsyncHTTPClient.configure('tornado.simple_httpclient.SimpleAsyncHTTPClient', max_clients=10)
    mock_super_configure.assert_called_once_with('tornado.simple_httpclient.SimpleAsyncHTTPClient', max_clients=10)
