# file: tornado/httpclient.py:358-549
# asked: {"lines": [513, 514, 534], "branches": [[512, 513], [533, 534]]}
# gained: {"lines": [513, 514, 534], "branches": [[512, 513], [533, 534]]}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.httputil import HTTPHeaders
import datetime

def test_if_modified_since_header():
    headers = HTTPHeaders()
    if_modified_since = datetime.datetime(2023, 1, 1)
    request = HTTPRequest(url="http://example.com", headers=headers, if_modified_since=if_modified_since)
    assert "If-Modified-Since" in request.headers
    assert request.headers["If-Modified-Since"] == "Sun, 01 Jan 2023 00:00:00 GMT"

def test_decompress_response():
    request = HTTPRequest(url="http://example.com", decompress_response=True)
    assert request.decompress_response is True

    request = HTTPRequest(url="http://example.com", decompress_response=False)
    assert request.decompress_response is False

    request = HTTPRequest(url="http://example.com", use_gzip=True)
    assert request.decompress_response is True

    request = HTTPRequest(url="http://example.com", use_gzip=False)
    assert request.decompress_response is False
