# file tornado/httpclient.py:735-754
# lines [735, 736, 741, 744, 745, 747, 748, 749, 750, 751, 752, 754]
# branches ['749->750', '749->751', '751->752', '751->754']

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

def test_request_proxy(mocker):
    # Mock HTTPRequest
    mock_request = mocker.Mock(spec=HTTPRequest)
    mock_request.some_attr = None

    # Test with defaults
    defaults = {'some_attr': 'default_value'}
    proxy = _RequestProxy(mock_request, defaults)
    assert proxy.some_attr == 'default_value'

    # Test without defaults
    proxy = _RequestProxy(mock_request, None)
    assert proxy.some_attr is None

    # Test with request attribute
    mock_request.some_attr = 'request_value'
    proxy = _RequestProxy(mock_request, defaults)
    assert proxy.some_attr == 'request_value'
