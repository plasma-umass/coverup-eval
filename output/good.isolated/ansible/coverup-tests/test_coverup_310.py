# file lib/ansible/module_utils/urls.py:1018-1032
# lines [1018, 1022, 1023, 1024, 1025, 1027, 1028, 1031, 1032]
# branches ['1023->1024', '1023->1032', '1027->1028', '1027->1032', '1028->1027', '1028->1031']

import os
import pytest
from ansible.module_utils.urls import SSLValidationHandler
from unittest.mock import MagicMock

@pytest.fixture
def no_proxy_cleanup():
    # Store original NO_PROXY environment variable
    original_no_proxy = os.environ.get('no_proxy')
    yield
    # Restore original NO_PROXY environment variable
    if original_no_proxy is not None:
        os.environ['no_proxy'] = original_no_proxy
    else:
        os.environ.pop('no_proxy', None)

def test_detect_no_proxy_with_no_proxy_set(no_proxy_cleanup):
    test_url = "http://example.com"
    os.environ['no_proxy'] = "example.com"
    handler = SSLValidationHandler(MagicMock(), MagicMock())
    assert not handler.detect_no_proxy(test_url)

def test_detect_no_proxy_with_no_proxy_not_set(no_proxy_cleanup):
    test_url = "http://example.com"
    handler = SSLValidationHandler(MagicMock(), MagicMock())
    assert handler.detect_no_proxy(test_url)

def test_detect_no_proxy_with_no_proxy_set_different_domain(no_proxy_cleanup):
    test_url = "http://example.com"
    os.environ['no_proxy'] = "example.org"
    handler = SSLValidationHandler(MagicMock(), MagicMock())
    assert handler.detect_no_proxy(test_url)

def test_detect_no_proxy_with_no_proxy_set_subdomain(no_proxy_cleanup):
    test_url = "http://sub.example.com"
    os.environ['no_proxy'] = "example.com"
    handler = SSLValidationHandler(MagicMock(), MagicMock())
    assert not handler.detect_no_proxy(test_url)

def test_detect_no_proxy_with_no_proxy_set_port(no_proxy_cleanup):
    test_url = "http://example.com:8080"
    os.environ['no_proxy'] = "example.com"
    handler = SSLValidationHandler(MagicMock(), MagicMock())
    assert not handler.detect_no_proxy(test_url)

def test_detect_no_proxy_with_no_proxy_set_multiple(no_proxy_cleanup):
    test_url = "http://example.com"
    os.environ['no_proxy'] = "example.org,example.com"
    handler = SSLValidationHandler(MagicMock(), MagicMock())
    assert not handler.detect_no_proxy(test_url)

def test_detect_no_proxy_with_no_proxy_set_multiple_and_port(no_proxy_cleanup):
    test_url = "http://example.com:8080"
    os.environ['no_proxy'] = "example.org,example.com"
    handler = SSLValidationHandler(MagicMock(), MagicMock())
    assert not handler.detect_no_proxy(test_url)
