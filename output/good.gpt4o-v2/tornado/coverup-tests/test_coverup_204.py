# file: tornado/simple_httpclient.py:165-190
# asked: {"lines": [168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 179, 180, 181, 182, 184, 185, 186, 187, 188, 189], "branches": [[173, 174], [173, 184], [179, 180], [179, 184], [186, 0], [186, 187]]}
# gained: {"lines": [168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 179, 180, 181, 182, 184, 185, 186, 187, 188, 189], "branches": [[173, 174], [179, 180], [179, 184], [186, 187]]}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.ioloop import IOLoop
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.log import gen_log

@pytest.fixture
def http_client():
    client = SimpleAsyncHTTPClient()
    yield client
    client.close()

def test_fetch_impl_max_clients_reached(http_client, mocker):
    request = HTTPRequest(url="http://example.com", connect_timeout=10, request_timeout=20)
    callback = mocker.Mock()
    
    # Mock the necessary attributes and methods
    http_client.queue = []
    http_client.active = [mocker.Mock()] * http_client.max_clients
    http_client.waiting = {}
    http_client.io_loop = IOLoop.current()
    mocker.patch.object(http_client.io_loop, 'add_timeout', return_value='timeout_handle')
    mocker.patch.object(http_client, '_process_queue')
    mocker.patch.object(gen_log, 'debug')

    http_client.fetch_impl(request, callback)

    assert len(http_client.queue) == 1
    assert len(http_client.waiting) == 1
    key = list(http_client.waiting.keys())[0]
    assert http_client.waiting[key][0] == request
    assert http_client.waiting[key][1] == callback
    assert http_client.waiting[key][2] == 'timeout_handle'
    http_client._process_queue.assert_called_once()
    gen_log.debug.assert_called_once_with(
        "max_clients limit reached, request queued. %d active, %d queued requests." % (len(http_client.active), len(http_client.queue))
    )

def test_fetch_impl_no_timeout(http_client, mocker):
    request = HTTPRequest(url="http://example.com", connect_timeout=0, request_timeout=0)
    callback = mocker.Mock()
    
    # Mock the necessary attributes and methods
    http_client.queue = []
    http_client.active = [mocker.Mock()] * http_client.max_clients
    http_client.waiting = {}
    http_client.io_loop = IOLoop.current()
    mocker.patch.object(http_client.io_loop, 'add_timeout')
    mocker.patch.object(http_client, '_process_queue')
    mocker.patch.object(gen_log, 'debug')

    http_client.fetch_impl(request, callback)

    assert len(http_client.queue) == 1
    assert len(http_client.waiting) == 1
    key = list(http_client.waiting.keys())[0]
    assert http_client.waiting[key][0] == request
    assert http_client.waiting[key][1] == callback
    assert http_client.waiting[key][2] is None
    http_client._process_queue.assert_called_once()
    gen_log.debug.assert_called_once_with(
        "max_clients limit reached, request queued. %d active, %d queued requests." % (len(http_client.active), len(http_client.queue))
    )
