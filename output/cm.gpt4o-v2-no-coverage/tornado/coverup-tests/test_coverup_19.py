# file: tornado/httpclient.py:358-549
# asked: {"lines": [358, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 391, 392, 393, 394, 511, 512, 513, 514, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549], "branches": [[512, 513], [512, 516], [533, 534], [533, 536]]}
# gained: {"lines": [358, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 391, 392, 393, 394, 511, 512, 513, 514, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549], "branches": [[512, 513], [533, 534]]}

import pytest
import ssl
from tornado.httpclient import HTTPRequest
from tornado.httputil import HTTPHeaders
import datetime

def test_http_request_initialization():
    url = "http://example.com"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    body = '{"key": "value"}'
    auth_username = "user"
    auth_password = "pass"
    auth_mode = "basic"
    connect_timeout = 10.0
    request_timeout = 30.0
    if_modified_since = datetime.datetime(2020, 1, 1)
    follow_redirects = False
    max_redirects = 3
    user_agent = "TestAgent"
    use_gzip = True
    network_interface = "eth0"
    streaming_callback = lambda x: x
    header_callback = lambda x: x
    prepare_curl_callback = lambda x: x
    proxy_host = "proxy.example.com"
    proxy_port = 8080
    proxy_username = "proxyuser"
    proxy_password = "proxypass"
    proxy_auth_mode = "digest"
    allow_nonstandard_methods = True
    validate_cert = False
    ca_certs = "/path/to/ca_certs"
    allow_ipv6 = False
    client_key = "/path/to/client_key"
    client_cert = "/path/to/client_cert"
    body_producer = lambda write: None
    expect_100_continue = True
    decompress_response = False
    ssl_options = {"cert_reqs": ssl.CERT_NONE}

    request = HTTPRequest(
        url=url,
        method=method,
        headers=headers,
        body=body,
        auth_username=auth_username,
        auth_password=auth_password,
        auth_mode=auth_mode,
        connect_timeout=connect_timeout,
        request_timeout=request_timeout,
        if_modified_since=if_modified_since,
        follow_redirects=follow_redirects,
        max_redirects=max_redirects,
        user_agent=user_agent,
        use_gzip=use_gzip,
        network_interface=network_interface,
        streaming_callback=streaming_callback,
        header_callback=header_callback,
        prepare_curl_callback=prepare_curl_callback,
        proxy_host=proxy_host,
        proxy_port=proxy_port,
        proxy_username=proxy_username,
        proxy_password=proxy_password,
        proxy_auth_mode=proxy_auth_mode,
        allow_nonstandard_methods=allow_nonstandard_methods,
        validate_cert=validate_cert,
        ca_certs=ca_certs,
        allow_ipv6=allow_ipv6,
        client_key=client_key,
        client_cert=client_cert,
        body_producer=body_producer,
        expect_100_continue=expect_100_continue,
        decompress_response=decompress_response,
        ssl_options=ssl_options,
    )

    assert request.url == url
    assert request.method == method
    assert request.headers["Content-Type"] == "application/json"
    assert request.body == body.encode("utf-8")
    assert request.auth_username == auth_username
    assert request.auth_password == auth_password
    assert request.auth_mode == auth_mode
    assert request.connect_timeout == connect_timeout
    assert request.request_timeout == request_timeout
    assert request.headers["If-Modified-Since"] == "Wed, 01 Jan 2020 00:00:00 GMT"
    assert request.follow_redirects == follow_redirects
    assert request.max_redirects == max_redirects
    assert request.user_agent == user_agent
    assert request.decompress_response == decompress_response
    assert request.network_interface == network_interface
    assert request.streaming_callback == streaming_callback
    assert request.header_callback == header_callback
    assert request.prepare_curl_callback == prepare_curl_callback
    assert request.proxy_host == proxy_host
    assert request.proxy_port == proxy_port
    assert request.proxy_username == proxy_username
    assert request.proxy_password == proxy_password
    assert request.proxy_auth_mode == proxy_auth_mode
    assert request.allow_nonstandard_methods == allow_nonstandard_methods
    assert request.validate_cert == validate_cert
    assert request.ca_certs == ca_certs
    assert request.allow_ipv6 == allow_ipv6
    assert request.client_key == client_key
    assert request.client_cert == client_cert
    assert request.body_producer == body_producer
    assert request.expect_100_continue == expect_100_continue
    assert request.ssl_options == ssl_options
    assert isinstance(request.start_time, float)
