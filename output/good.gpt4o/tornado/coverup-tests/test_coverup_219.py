# file tornado/simple_httpclient.py:165-190
# lines [174, 175, 176, 177, 179, 180, 181, 182, 187, 188, 189]
# branches ['173->174', '179->180', '179->184', '186->187']

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.ioloop import IOLoop
import functools
import logging

@pytest.fixture
def mock_ioloop(mocker):
    mock_loop = mocker.Mock(spec=IOLoop)
    mock_loop.time.return_value = 0  # Mock the time method to return a fixed value
    return mock_loop

@pytest.fixture
def client(mock_ioloop, mocker):
    # Mock the IOLoop.current() method to return the mock_ioloop
    mocker.patch('tornado.ioloop.IOLoop.current', return_value=mock_ioloop)
    return SimpleAsyncHTTPClient()

def test_fetch_impl_max_clients_reached(client, mocker):
    # Mock the request and callback
    request = mocker.Mock(spec=HTTPRequest)
    request.connect_timeout = 1
    request.request_timeout = 2
    callback = mocker.Mock()

    # Mock the internal state of the client
    client.max_clients = 1
    client.active = [object()]  # Simulate max clients reached
    client.queue = []
    client.waiting = {}

    # Mock the io_loop.add_timeout method
    add_timeout_mock = mocker.patch.object(client.io_loop, 'add_timeout')

    # Mock the logger
    gen_log_mock = mocker.patch('tornado.simple_httpclient.gen_log')

    # Call the method under test
    client.fetch_impl(request, callback)

    # Assertions to ensure the correct branches were executed
    assert len(client.queue) == 1
    assert client.queue[0][1] == request
    assert client.queue[0][2] == callback

    # Check if timeout was set correctly
    add_timeout_mock.assert_called_once()
    timeout_call_args = add_timeout_mock.call_args[0]
    assert timeout_call_args[1].func == client._on_timeout
    assert timeout_call_args[1].args[0] == client.queue[0][0]
    assert timeout_call_args[1].args[1] == "in request queue"

    # Check if the waiting dictionary was updated correctly
    assert client.waiting[client.queue[0][0]] == (request, callback, add_timeout_mock.return_value)

    # Check if the debug log was called
    gen_log_mock.debug.assert_called_once_with(
        "max_clients limit reached, request queued. %d active, %d queued requests." % (len(client.active), len(client.queue))
    )
