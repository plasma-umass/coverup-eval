# file: tornado/httpclient.py:223-247
# asked: {"lines": [223, 236, 237, 238, 239, 240, 246, 247], "branches": [[236, 237], [236, 238], [239, 0], [239, 240], [246, 0], [246, 247]]}
# gained: {"lines": [223, 236, 237, 238, 239, 240, 246, 247], "branches": [[236, 237], [236, 238], [239, 0], [239, 240], [246, 0], [246, 247]]}

import pytest
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient

@pytest.fixture
def http_client():
    client = AsyncHTTPClient(force_instance=True)
    yield client
    client.close()

def test_close_not_closed(http_client):
    http_client._closed = False
    http_client._instance_cache = {http_client.io_loop: http_client}
    http_client.close()
    assert http_client._closed

def test_close_already_closed(http_client):
    http_client._closed = True
    http_client.close()
    assert http_client._closed

def test_close_inconsistent_cache(http_client):
    http_client._closed = False
    http_client._instance_cache = {http_client.io_loop: "not_http_client"}
    with pytest.raises(RuntimeError, match="inconsistent AsyncHTTPClient cache"):
        http_client.close()

def test_close_none_cache(http_client):
    http_client._closed = False
    http_client._instance_cache = None
    http_client.close()
    assert http_client._closed
