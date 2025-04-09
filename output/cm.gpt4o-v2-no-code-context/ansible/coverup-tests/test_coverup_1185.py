# file: lib/ansible/module_utils/urls.py:748-764
# asked: {"lines": [756, 764], "branches": [[755, 756], [761, 764]]}
# gained: {"lines": [756, 764], "branches": [[755, 756], [761, 764]]}

import pytest
from unittest import mock
from ansible.module_utils.urls import RequestWithMethod
import urllib.request as urllib_request

def test_request_with_method_no_headers():
    url = 'http://example.com'
    method = 'POST'
    data = b'some data'
    
    request = RequestWithMethod(url, method, data)
    
    assert request.get_method() == 'POST'
    assert request.data == data
    assert request.headers == {}

def test_request_with_method_custom_headers():
    url = 'http://example.com'
    method = 'GET'
    data = b'some data'
    headers = {'User-Agent': 'custom-agent'}
    
    request = RequestWithMethod(url, method, data, headers)
    
    assert request.get_method() == 'GET'
    assert request.data == data
    assert request.headers['User-agent'] == headers['User-Agent']

def test_request_with_method_fallback_get_method(monkeypatch):
    url = 'http://example.com'
    method = 'GET'
    data = b'some data'
    
    class MockRequest(urllib_request.Request):
        def get_method(self):
            return 'DEFAULT'
    
    monkeypatch.setattr(urllib_request, 'Request', MockRequest)
    
    request = RequestWithMethod(url, method, data)
    request._method = None  # Simulate the condition where _method is None
    
    assert request.get_method() == 'DEFAULT'
    assert request.data == data
