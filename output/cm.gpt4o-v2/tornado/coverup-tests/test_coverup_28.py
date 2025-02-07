# file: tornado/httpclient.py:358-549
# asked: {"lines": [358, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 391, 392, 393, 394, 511, 512, 513, 514, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549], "branches": [[512, 513], [512, 516], [533, 534], [533, 536]]}
# gained: {"lines": [358, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 391, 392, 393, 394, 511, 512, 513, 514, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549], "branches": [[512, 513], [533, 534]]}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.httputil import HTTPHeaders
import datetime
import ssl
import time

@pytest.fixture
def mock_time(monkeypatch):
    class MockTime:
        def time(self):
            return 1234567890.0

    mock_time = MockTime()
    monkeypatch.setattr(time, 'time', mock_time.time)
    return mock_time

def test_http_request_full_coverage(mock_time):
    headers = HTTPHeaders({"Content-Type": "application/json"})
    if_modified_since = datetime.datetime(2020, 1, 1)
    ssl_context = ssl.create_default_context()

    request = HTTPRequest(
        url="http://example.com",
        method="POST",
        headers=headers,
        body=b"{}",  # body should be bytes
        auth_username="user",
        auth_password="pass",
        auth_mode="basic",
        connect_timeout=10.0,
        request_timeout=20.0,
        if_modified_since=if_modified_since,
        follow_redirects=True,
        max_redirects=5,
        user_agent="TestAgent",
        use_gzip=True,
        network_interface="eth0",
        streaming_callback=lambda x: x,
        header_callback=lambda x: x,
        prepare_curl_callback=lambda x: x,
        proxy_host="proxy.example.com",
        proxy_port=8080,
        proxy_username="proxyuser",
        proxy_password="proxypass",
        proxy_auth_mode="digest",
        allow_nonstandard_methods=True,
        validate_cert=True,
        ca_certs="/path/to/ca_certs",
        allow_ipv6=True,
        client_key="/path/to/client_key",
        client_cert="/path/to/client_cert",
        body_producer=None,
        expect_100_continue=True,
        decompress_response=True,
        ssl_options=ssl_context
    )

    assert request.url == "http://example.com"
    assert request.method == "POST"
    assert request.headers["Content-Type"] == "application/json"
    assert request.headers["If-Modified-Since"] == "Wed, 01 Jan 2020 00:00:00 GMT"
    assert request.body == b"{}"  # body should be bytes
    assert request.auth_username == "user"
    assert request.auth_password == "pass"
    assert request.auth_mode == "basic"
    assert request.connect_timeout == 10.0
    assert request.request_timeout == 20.0
    assert request.follow_redirects is True
    assert request.max_redirects == 5
    assert request.user_agent == "TestAgent"
    assert request.decompress_response is True
    assert request.network_interface == "eth0"
    assert request.streaming_callback is not None
    assert request.header_callback is not None
    assert request.prepare_curl_callback is not None
    assert request.proxy_host == "proxy.example.com"
    assert request.proxy_port == 8080
    assert request.proxy_username == "proxyuser"
    assert request.proxy_password == "proxypass"
    assert request.proxy_auth_mode == "digest"
    assert request.allow_nonstandard_methods is True
    assert request.validate_cert is True
    assert request.ca_certs == "/path/to/ca_certs"
    assert request.allow_ipv6 is True
    assert request.client_key == "/path/to/client_key"
    assert request.client_cert == "/path/to/client_cert"
    assert request.ssl_options == ssl_context
    assert request.expect_100_continue is True
    assert request.start_time == 1234567890.0
