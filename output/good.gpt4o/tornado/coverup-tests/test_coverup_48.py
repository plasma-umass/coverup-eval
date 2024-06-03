# file tornado/httpclient.py:223-247
# lines [223, 236, 237, 238, 239, 240, 246, 247]
# branches ['236->237', '236->238', '239->exit', '239->240', '246->exit', '246->247']

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

@pytest.fixture
def mock_ioloop(mocker):
    return mocker.Mock(spec=IOLoop)

@pytest.fixture
def async_http_client(mocker, mock_ioloop):
    # Mock the configured_class method to avoid creating a real HTTP client
    mocker.patch('tornado.httpclient.AsyncHTTPClient.configured_class', return_value=AsyncHTTPClient)
    client = AsyncHTTPClient(force_instance=True)
    client.io_loop = mock_ioloop
    yield client
    client.close()

def test_async_http_client_close(mocker, async_http_client, mock_ioloop):
    # Mock the _instance_cache to simulate the conditions
    async_http_client._instance_cache = {mock_ioloop: async_http_client}
    async_http_client._closed = False

    # Call the close method and assert the expected behavior
    async_http_client.close()
    assert async_http_client._closed
    assert mock_ioloop not in async_http_client._instance_cache

    # Test the branch where cached_val is not None and not self
    async_http_client._closed = False
    async_http_client._instance_cache = {mock_ioloop: "other_client"}
    with pytest.raises(RuntimeError, match="inconsistent AsyncHTTPClient cache"):
        async_http_client.close()

    # Test the branch where cached_val is None
    async_http_client._closed = False
    async_http_client._instance_cache = {mock_ioloop: None}
    async_http_client.close()
    assert async_http_client._closed
    assert mock_ioloop not in async_http_client._instance_cache
