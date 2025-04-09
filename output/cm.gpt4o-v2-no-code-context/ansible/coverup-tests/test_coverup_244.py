# file: lib/ansible/module_utils/urls.py:1018-1032
# asked: {"lines": [1018, 1022, 1023, 1024, 1025, 1027, 1028, 1031, 1032], "branches": [[1023, 1024], [1023, 1032], [1027, 1028], [1027, 1032], [1028, 1027], [1028, 1031]]}
# gained: {"lines": [1018, 1022, 1023, 1024, 1025, 1027, 1028, 1031, 1032], "branches": [[1023, 1024], [1023, 1032], [1027, 1028], [1027, 1032], [1028, 1027], [1028, 1031]]}

import os
import pytest
from urllib.parse import urlparse
from unittest import mock
from ansible.module_utils.urls import SSLValidationHandler

@pytest.fixture
def ssl_validation_handler():
    class MockSSLValidationHandler(SSLValidationHandler):
        def __init__(self):
            pass
    return MockSSLValidationHandler()

def test_detect_no_proxy_with_no_proxy_set(ssl_validation_handler, monkeypatch):
    url = 'http://example.com'
    monkeypatch.setenv('no_proxy', 'example.com')
    
    result = ssl_validation_handler.detect_no_proxy(url)
    
    assert result is False

def test_detect_no_proxy_with_no_proxy_not_set(ssl_validation_handler, monkeypatch):
    url = 'http://example.com'
    monkeypatch.delenv('no_proxy', raising=False)
    
    result = ssl_validation_handler.detect_no_proxy(url)
    
    assert result is True

def test_detect_no_proxy_with_no_matching_no_proxy(ssl_validation_handler, monkeypatch):
    url = 'http://example.com'
    monkeypatch.setenv('no_proxy', 'anotherdomain.com')
    
    result = ssl_validation_handler.detect_no_proxy(url)
    
    assert result is True

def test_detect_no_proxy_with_partial_matching_no_proxy(ssl_validation_handler, monkeypatch):
    url = 'http://sub.example.com'
    monkeypatch.setenv('no_proxy', 'example.com')
    
    result = ssl_validation_handler.detect_no_proxy(url)
    
    assert result is False

def test_detect_no_proxy_with_port_in_url(ssl_validation_handler, monkeypatch):
    url = 'http://example.com:8080'
    monkeypatch.setenv('no_proxy', 'example.com')
    
    result = ssl_validation_handler.detect_no_proxy(url)
    
    assert result is False
