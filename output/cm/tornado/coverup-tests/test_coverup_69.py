# file tornado/httpclient.py:191-196
# lines [191, 192, 193, 194, 195, 196]
# branches ['194->195', '194->196']

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
import weakref

class TestAsyncHTTPClient:
    @pytest.fixture
    def mock_ioloop(self, mocker):
        return mocker.Mock(spec=IOLoop)

    def test_async_clients_creates_dict(self, mock_ioloop):
        # Ensure the attribute does not exist before the test
        attr_name = "_async_client_dict_" + AsyncHTTPClient.__name__
        if hasattr(AsyncHTTPClient, attr_name):
            delattr(AsyncHTTPClient, attr_name)

        # Call the method to test if it creates the dictionary
        client_dict = AsyncHTTPClient._async_clients()
        assert isinstance(client_dict, weakref.WeakKeyDictionary)
        assert getattr(AsyncHTTPClient, attr_name) is client_dict

        # Clean up by deleting the attribute
        delattr(AsyncHTTPClient, attr_name)

    def test_async_clients_reuses_dict(self, mock_ioloop):
        # Create the attribute before the test
        attr_name = "_async_client_dict_" + AsyncHTTPClient.__name__
        existing_dict = weakref.WeakKeyDictionary()
        setattr(AsyncHTTPClient, attr_name, existing_dict)

        # Call the method to test if it reuses the existing dictionary
        client_dict = AsyncHTTPClient._async_clients()
        assert client_dict is existing_dict

        # Clean up by deleting the attribute
        delattr(AsyncHTTPClient, attr_name)
