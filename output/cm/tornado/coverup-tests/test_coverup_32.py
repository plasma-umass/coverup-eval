# file tornado/httpclient.py:735-754
# lines [735, 736, 741, 744, 745, 747, 748, 749, 750, 751, 752, 754]
# branches ['749->750', '749->751', '751->752', '751->754']

import pytest
from tornado.httpclient import HTTPRequest, _RequestProxy

@pytest.fixture
def request_proxy():
    request = HTTPRequest(url='http://example.com')
    defaults = {'method': 'GET', 'body': None}
    return _RequestProxy(request, defaults)

def test_request_proxy_getattr_with_request_attribute(request_proxy):
    assert request_proxy.url == 'http://example.com'

def test_request_proxy_getattr_with_default_attribute(request_proxy):
    assert request_proxy.method == 'GET'

def test_request_proxy_getattr_with_nonexistent_attribute(request_proxy):
    with pytest.raises(AttributeError):
        _ = request_proxy.nonexistent_attribute

def test_request_proxy_getattr_with_none_defaults():
    request = HTTPRequest(url='http://example.com', method='POST')
    proxy = _RequestProxy(request, None)
    assert proxy.url == 'http://example.com'
    assert proxy.method == 'POST'
