# file: lib/ansible/module_utils/urls.py:748-764
# asked: {"lines": [756, 764], "branches": [[755, 756], [761, 764]]}
# gained: {"lines": [756, 764], "branches": [[755, 756], [761, 764]]}

import pytest
import ansible.module_utils.six.moves.urllib.request as urllib_request
from ansible.module_utils.urls import RequestWithMethod

def test_request_with_method_init_no_headers():
    url = 'http://example.com'
    method = 'GET'
    data = None
    headers = None
    origin_req_host = None
    unverifiable = True

    request = RequestWithMethod(url, method, data, headers, origin_req_host, unverifiable)
    
    assert request.get_method() == 'GET'
    assert request.header_items() == []

def test_request_with_method_get_method_custom():
    url = 'http://example.com'
    method = 'DELETE'
    data = None
    headers = {}
    origin_req_host = None
    unverifiable = True

    request = RequestWithMethod(url, method, data, headers, origin_req_host, unverifiable)
    
    assert request.get_method() == 'DELETE'

def test_request_with_method_get_method_default(monkeypatch):
    url = 'http://example.com'
    method = 'GET'
    data = None
    headers = {}
    origin_req_host = None
    unverifiable = True

    class MockRequest(urllib_request.Request):
        def get_method(self):
            return 'DEFAULT_METHOD'

    monkeypatch.setattr(urllib_request.Request, 'get_method', MockRequest.get_method)
    
    request = RequestWithMethod(url, method, data, headers, origin_req_host, unverifiable)
    request._method = None  # Simulate the condition where _method is None
    
    assert request.get_method() == 'DEFAULT_METHOD'
