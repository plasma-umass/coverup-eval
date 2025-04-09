# file: tornado/simple_httpclient.py:165-190
# asked: {"lines": [168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 179, 180, 181, 182, 184, 185, 186, 187, 188, 189], "branches": [[173, 174], [173, 184], [179, 180], [179, 184], [186, 0], [186, 187]]}
# gained: {"lines": [168, 169, 170, 171, 172, 173, 184, 185, 186, 187, 188, 189], "branches": [[173, 184], [186, 187]]}

import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse, AsyncHTTPClient
from tornado.ioloop import IOLoop
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.log import gen_log
from unittest.mock import Mock, patch
import functools

@pytest.fixture
def http_client():
    client = SimpleAsyncHTTPClient()
    client.initialize(max_clients=2)
    return client

def test_fetch_impl(http_client, monkeypatch):
    request = HTTPRequest(url="http://example.com", connect_timeout=10, request_timeout=20)
    callback = Mock()

    mock_add_timeout = Mock()
    monkeypatch.setattr(http_client.io_loop, 'add_timeout', mock_add_timeout)
    mock_process_queue = Mock()
    monkeypatch.setattr(http_client, '_process_queue', mock_process_queue)
    mock_gen_log_debug = Mock()
    monkeypatch.setattr(gen_log, 'debug', mock_gen_log_debug)

    http_client.fetch_impl(request, callback)

    assert len(http_client.queue) == 1
    assert len(http_client.waiting) == 1
    assert mock_process_queue.called

    key, req, cb = http_client.queue[0]
    assert req == request
    assert cb == callback

    if len(http_client.active) >= http_client.max_clients:
        assert mock_add_timeout.called
    else:
        assert not mock_add_timeout.called

    if http_client.queue:
        assert mock_gen_log_debug.called

def test_on_timeout(http_client, monkeypatch):
    request = HTTPRequest(url="http://example.com", connect_timeout=10, request_timeout=20)
    callback = Mock()
    key = object()
    http_client.waiting[key] = (request, callback, None)
    http_client.queue.append((key, request, callback))

    mock_add_callback = Mock()
    monkeypatch.setattr(http_client.io_loop, 'add_callback', mock_add_callback)

    http_client._on_timeout(key, "in request queue")

    assert key not in http_client.waiting
    assert (key, request, callback) not in http_client.queue
    assert mock_add_callback.called

def test_process_queue(http_client, monkeypatch):
    request = HTTPRequest(url="http://example.com", connect_timeout=10, request_timeout=20)
    callback = Mock()
    key = object()
    http_client.queue.append((key, request, callback))
    http_client.waiting[key] = (request, callback, None)

    mock_handle_request = Mock()
    monkeypatch.setattr(http_client, '_handle_request', mock_handle_request)
    mock_remove_timeout = Mock()
    monkeypatch.setattr(http_client, '_remove_timeout', mock_remove_timeout)

    http_client._process_queue()

    assert len(http_client.queue) == 0 or len(http_client.active) < http_client.max_clients
    assert mock_handle_request.called
    assert mock_remove_timeout.called
