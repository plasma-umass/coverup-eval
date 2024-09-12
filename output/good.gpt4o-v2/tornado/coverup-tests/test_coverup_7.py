# file: tornado/httpclient.py:249-307
# asked: {"lines": [249, 252, 283, 284, 285, 286, 288, 289, 290, 295, 296, 297, 299, 300, 301, 302, 303, 304, 306, 307], "branches": [[283, 284], [283, 285], [285, 286], [285, 288], [288, 289], [288, 295], [300, 301], [300, 304], [301, 302], [301, 304]]}
# gained: {"lines": [249, 252], "branches": []}

import pytest
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPResponse, HTTPError
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
from unittest.mock import Mock, patch

@pytest.mark.gen_test
async def test_fetch_with_string_url():
    client = AsyncHTTPClient(force_instance=True)
    url = "http://example.com"
    
    with patch.object(client, 'fetch_impl') as mock_fetch_impl:
        future = client.fetch(url)
        assert isinstance(future, Future)
        assert not future.done()
        
        response = HTTPResponse(HTTPRequest(url), 200)
        mock_fetch_impl.call_args[0][1](response)
        
        result = await future
        assert result == response

@pytest.mark.gen_test
async def test_fetch_with_http_request():
    client = AsyncHTTPClient(force_instance=True)
    request = HTTPRequest("http://example.com")
    
    with patch.object(client, 'fetch_impl') as mock_fetch_impl:
        future = client.fetch(request)
        assert isinstance(future, Future)
        assert not future.done()
        
        response = HTTPResponse(request, 200)
        mock_fetch_impl.call_args[0][1](response)
        
        result = await future
        assert result == response

@pytest.mark.gen_test
async def test_fetch_with_error():
    client = AsyncHTTPClient(force_instance=True)
    url = "http://example.com"
    
    with patch.object(client, 'fetch_impl') as mock_fetch_impl:
        future = client.fetch(url)
        assert isinstance(future, Future)
        assert not future.done()
        
        error = HTTPError(500, "Internal Server Error")
        response = HTTPResponse(HTTPRequest(url), 500, error=error)
        mock_fetch_impl.call_args[0][1](response)
        
        with pytest.raises(HTTPError):
            await future

@pytest.mark.gen_test
async def test_fetch_with_error_no_raise():
    client = AsyncHTTPClient(force_instance=True)
    url = "http://example.com"
    
    with patch.object(client, 'fetch_impl') as mock_fetch_impl:
        future = client.fetch(url, raise_error=False)
        assert isinstance(future, Future)
        assert not future.done()
        
        error = HTTPError(500, "Internal Server Error")
        response = HTTPResponse(HTTPRequest(url), 500, error=error)
        mock_fetch_impl.call_args[0][1](response)
        
        result = await future
        assert result == response
        assert result.error == error

@pytest.mark.gen_test
async def test_fetch_on_closed_client():
    client = AsyncHTTPClient(force_instance=True)
    client.close()
    
    with pytest.raises(RuntimeError):
        client.fetch("http://example.com")

@pytest.mark.gen_test
async def test_fetch_with_kwargs_on_http_request():
    client = AsyncHTTPClient(force_instance=True)
    request = HTTPRequest("http://example.com")
    
    with pytest.raises(ValueError):
        client.fetch(request, some_kwarg="value")
