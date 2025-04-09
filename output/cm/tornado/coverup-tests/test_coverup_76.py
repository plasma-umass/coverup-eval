# file tornado/simple_httpclient.py:192-200
# lines [192, 193, 194, 195, 196, 197, 198, 199, 200]
# branches ['193->exit', '193->194', '195->196', '195->197']

import functools
from collections import deque
from unittest.mock import Mock, patch
import pytest

from tornado.simple_httpclient import SimpleAsyncHTTPClient

@pytest.fixture
def simple_async_http_client():
    client = SimpleAsyncHTTPClient(max_clients=1)
    client.queue = deque()
    client.active = {}
    client.waiting = {}
    client._remove_timeout = Mock()
    client._handle_request = Mock()
    return client

def test_process_queue_skips_non_waiting_requests(simple_async_http_client):
    key = 'non_waiting_key'
    request = Mock()
    callback = Mock()
    simple_async_http_client.queue.append((key, request, callback))
    
    simple_async_http_client._process_queue()
    
    simple_async_http_client._remove_timeout.assert_not_called()
    simple_async_http_client._handle_request.assert_not_called()
    assert key not in simple_async_http_client.active

def test_process_queue_processes_waiting_requests(simple_async_http_client):
    key = 'waiting_key'
    request = Mock()
    callback = Mock()
    simple_async_http_client.queue.append((key, request, callback))
    simple_async_http_client.waiting[key] = True
    
    release_callback = functools.partial(simple_async_http_client._release_fetch, key)
    simple_async_http_client._handle_request.return_value = None
    
    simple_async_http_client._process_queue()
    
    simple_async_http_client._remove_timeout.assert_called_once_with(key)
    # Using assert_called_once_with can cause issues with comparing partial functions.
    # Instead, we can check the call arguments directly.
    simple_async_http_client._handle_request.assert_called()
    args, _ = simple_async_http_client._handle_request.call_args
    assert args[0] == request
    assert isinstance(args[1], functools.partial)
    assert args[1].func == simple_async_http_client._release_fetch
    assert args[1].args == (key,)
    assert args[2] == callback
    assert simple_async_http_client.active[key] == (request, callback)
