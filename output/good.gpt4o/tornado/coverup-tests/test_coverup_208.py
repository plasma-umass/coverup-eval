# file tornado/simple_httpclient.py:202-203
# lines [202, 203]
# branches []

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import AsyncHTTPClient
from tornado.testing import AsyncTestCase, gen_test

class TestSimpleAsyncHTTPClient(AsyncTestCase):
    @gen_test
    async def test_connection_class(self):
        client = SimpleAsyncHTTPClient()
        connection_class = client._connection_class()
        assert connection_class.__name__ == "_HTTPConnection"
        assert issubclass(connection_class, object)  # Assuming _HTTPConnection is a subclass of object

    def tearDown(self):
        AsyncHTTPClient.configure(None)  # Reset the AsyncHTTPClient configuration
        super().tearDown()
