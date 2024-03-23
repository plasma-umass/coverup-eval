# file tornado/httpclient.py:198-214
# lines [198, 199, 200, 201, 203, 204, 205, 206, 211, 212, 213, 214]
# branches ['200->201', '200->203', '204->205', '204->206', '212->213', '212->214']

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

class TestAsyncHTTPClient:

    @pytest.fixture
    def mock_ioloop(self, mocker):
        mock = mocker.patch('tornado.ioloop.IOLoop.current')
        mock.return_value = 'mocked_ioloop'
        return mock

    @pytest.fixture
    def mock_instance_cache(self, mocker):
        mock = mocker.patch('tornado.httpclient.AsyncHTTPClient._async_clients')
        mock.return_value = {}
        return mock

    def test_async_http_client_new_instance(self, mock_ioloop, mock_instance_cache):
        # Test creating a new instance with force_instance=False
        client = AsyncHTTPClient()
        assert isinstance(client, AsyncHTTPClient)
        assert client._instance_cache is not None
        assert client._instance_cache['mocked_ioloop'] == client

    def test_async_http_client_force_new_instance(self, mock_ioloop, mock_instance_cache):
        # Test creating a new instance with force_instance=True
        client = AsyncHTTPClient(force_instance=True)
        assert isinstance(client, AsyncHTTPClient)
        assert client._instance_cache is None

    def test_async_http_client_reuse_instance(self, mock_ioloop, mock_instance_cache):
        # Test reusing an existing instance
        existing_client = AsyncHTTPClient()
        mock_instance_cache.return_value['mocked_ioloop'] = existing_client
        client = AsyncHTTPClient()
        assert client is existing_client

    def test_async_http_client_cleanup(self, mock_ioloop, mock_instance_cache):
        # Test cleanup after test
        client = AsyncHTTPClient()
        del client._instance_cache['mocked_ioloop']
        assert 'mocked_ioloop' not in client._instance_cache

# The following line is for local testing purposes only and should not be included in the response
# pytest.main([__file__])
