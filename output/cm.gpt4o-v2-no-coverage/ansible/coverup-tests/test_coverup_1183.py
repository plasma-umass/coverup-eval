# file: lib/ansible/module_utils/urls.py:748-764
# asked: {"lines": [761, 762, 764], "branches": [[755, 757], [761, 762], [761, 764]]}
# gained: {"lines": [761, 762, 764], "branches": [[755, 757], [761, 762], [761, 764]]}

import pytest
import ansible.module_utils.six.moves.urllib.request as urllib_request
from ansible.module_utils.urls import RequestWithMethod

def test_request_with_method_init(monkeypatch):
    url = 'http://example.com'
    method = 'POST'
    data = b'some data'
    headers = {'Content-Type': 'application/json'}
    origin_req_host = 'localhost'
    unverifiable = False

    request = RequestWithMethod(url, method, data, headers, origin_req_host, unverifiable)

    assert request.get_method() == 'POST'
    assert request.data == data
    assert dict(request.header_items()) == {'Content-type': 'application/json'}
    assert request.origin_req_host == origin_req_host
    assert request.unverifiable == unverifiable

def test_request_with_method_default_headers(monkeypatch):
    url = 'http://example.com'
    method = 'DELETE'

    request = RequestWithMethod(url, method)

    assert request.get_method() == 'DELETE'
    assert dict(request.header_items()) == {}

def test_request_with_method_get_method(monkeypatch):
    url = 'http://example.com'
    method = 'PUT'

    request = RequestWithMethod(url, method)

    assert request.get_method() == 'PUT'

    # Test the fallback to the parent class's get_method
    request._method = None
    assert request.get_method() == urllib_request.Request.get_method(request)
