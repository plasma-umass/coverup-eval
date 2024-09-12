# file: tornado/httpclient.py:735-754
# asked: {"lines": [735, 736, 741, 744, 745, 747, 748, 749, 750, 751, 752, 754], "branches": [[749, 750], [749, 751], [751, 752], [751, 754]]}
# gained: {"lines": [735, 736, 741, 747], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest
from typing import Optional, Dict, Any

class _RequestProxy:
    """Combines an object with a dictionary of defaults.

    Used internally by AsyncHTTPClient implementations.
    """

    def __init__(
        self, request: HTTPRequest, defaults: Optional[Dict[str, Any]]
    ) -> None:
        self.request = request
        self.defaults = defaults

    def __getattr__(self, name: str) -> Any:
        request_attr = getattr(self.request, name)
        if request_attr is not None:
            return request_attr
        elif self.defaults is not None:
            return self.defaults.get(name, None)
        else:
            return None

@pytest.fixture
def mock_http_request(mocker):
    return mocker.Mock(spec=HTTPRequest)

def test_request_proxy_with_request_attribute(mock_http_request):
    mock_http_request.some_attr = 'value'
    proxy = _RequestProxy(mock_http_request, None)
    assert proxy.some_attr == 'value'

def test_request_proxy_with_defaults(mock_http_request):
    mock_http_request.some_attr = None
    defaults = {'some_attr': 'default_value'}
    proxy = _RequestProxy(mock_http_request, defaults)
    assert proxy.some_attr == 'default_value'

def test_request_proxy_with_no_defaults(mock_http_request):
    mock_http_request.some_attr = None
    proxy = _RequestProxy(mock_http_request, None)
    assert proxy.some_attr is None

def test_request_proxy_with_missing_attribute(mock_http_request):
    proxy = _RequestProxy(mock_http_request, None)
    with pytest.raises(AttributeError):
        _ = proxy.missing_attr
