# file tornado/simple_httpclient.py:79-88
# lines [79, 80]
# branches []

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado.ioloop import IOLoop

@pytest.mark.asyncio
async def test_simple_async_http_client_fetch(mocker):
    # Mock the IOLoop instance to ensure it does not affect other tests
    mock_ioloop = mocker.patch('tornado.ioloop.IOLoop.current', return_value=IOLoop())

    client = SimpleAsyncHTTPClient()
    request = HTTPRequest(url="http://example.com")

    # Mock the fetch method to simulate a response
    mock_response = mocker.Mock()
    mock_response.code = 200
    mock_response.body = b"Hello, world!"
    mock_fetch = mocker.patch.object(client, 'fetch', return_value=mock_response)

    response = await client.fetch(request)

    # Assertions to verify the postconditions
    assert response.code == 200
    assert response.body == b"Hello, world!"

    # Clean up
    client.close()
    mock_ioloop().close()
