# file tornado/netutil.py:389-401
# lines [389, 390, 395, 396, 398, 399, 401]
# branches []

import pytest
import socket
from tornado.ioloop import IOLoop
from tornado.netutil import Resolver
from unittest.mock import patch

# Assuming _resolve_addr is a function defined in the tornado.netutil module
# that we need to mock for our test.
# If it's not the case, please replace '_resolve_addr' with the correct function name.

class TestDefaultExecutorResolver:
    @pytest.mark.asyncio
    async def test_resolve(self, mocker):
        # Mock the _resolve_addr function to return a predefined result
        mock_resolve_addr = mocker.patch('tornado.netutil._resolve_addr')
        mock_resolve_addr.return_value = [(socket.AF_INET, ('127.0.0.1', 80))]

        # Create an instance of the DefaultExecutorResolver
        resolver = Resolver.DefaultExecutorResolver()

        # Call the resolve method with test parameters
        result = await resolver.resolve('localhost', 80)

        # Assert that the result matches the mocked _resolve_addr return value
        assert result == [(socket.AF_INET, ('127.0.0.1', 80))]

        # Assert that _resolve_addr was called with the correct arguments
        mock_resolve_addr.assert_called_once_with('localhost', 80, socket.AF_UNSPEC)

        # Clean up by stopping the IOLoop if it's running
        if IOLoop.current().running():
            IOLoop.current().stop()
