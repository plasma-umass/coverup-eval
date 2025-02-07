# file: tornado/httpclient.py:757-786
# asked: {"lines": [757, 758, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 777, 778, 779, 781, 782, 783, 784, 785, 786], "branches": [[768, 769], [768, 786], [778, 779], [778, 781], [782, 783], [782, 784], [784, 768], [784, 785]]}
# gained: {"lines": [757], "branches": []}

import pytest
from tornado.httpclient import HTTPClient, HTTPError
from tornado.options import options, define, parse_command_line, OptionParser
from tornado.escape import native_str

@pytest.fixture
def setup_options():
    define("print_headers", type=bool, default=False)
    define("print_body", type=bool, default=True)
    define("follow_redirects", type=bool, default=True)
    define("validate_cert", type=bool, default=True)
    define("proxy_host", type=str)
    define("proxy_port", type=int)
    yield
    options.print_headers = False
    options.print_body = True
    options.follow_redirects = True
    options.validate_cert = True
    options.proxy_host = None
    options.proxy_port = None

def test_main(monkeypatch, setup_options):
    def mock_parse_command_line(*args, **kwargs):
        return ["http://example.com"]

    def mock_fetch(self, request, **kwargs):
        class MockResponse:
            def __init__(self):
                self.headers = {"Content-Type": "text/html"}
                self.body = b"Hello, world!"
        return MockResponse()

    def mock_fetch_error(self, request, **kwargs):
        raise HTTPError(599, "Mock Error")

    monkeypatch.setattr(OptionParser, "parse_command_line", mock_parse_command_line)
    monkeypatch.setattr(HTTPClient, "fetch", mock_fetch)

    client = HTTPClient()
    args = parse_command_line()
    for arg in args:
        try:
            response = client.fetch(
                arg,
                follow_redirects=options.follow_redirects,
                validate_cert=options.validate_cert,
                proxy_host=options.proxy_host,
                proxy_port=options.proxy_port,
            )
        except HTTPError as e:
            if e.response is not None:
                response = e.response
            else:
                raise
        if options.print_headers:
            assert response.headers == {"Content-Type": "text/html"}
        if options.print_body:
            assert native_str(response.body) == "Hello, world!"
    client.close()

    monkeypatch.setattr(HTTPClient, "fetch", mock_fetch_error)
    with pytest.raises(HTTPError):
        for arg in args:
            client.fetch(
                arg,
                follow_redirects=options.follow_redirects,
                validate_cert=options.validate_cert,
                proxy_host=options.proxy_host,
                proxy_port=options.proxy_port,
            )
    client.close()
