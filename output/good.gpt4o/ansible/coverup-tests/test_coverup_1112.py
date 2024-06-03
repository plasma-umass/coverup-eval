# file lib/ansible/module_utils/urls.py:1018-1032
# lines [1022, 1023, 1024, 1025, 1027, 1028, 1031, 1032]
# branches ['1023->1024', '1023->1032', '1027->1028', '1027->1032', '1028->1027', '1028->1031']

import os
import pytest
from unittest import mock
from urllib.parse import urlparse
from ansible.module_utils.urls import SSLValidationHandler

@pytest.fixture
def ssl_validation_handler(mocker):
    mocker.patch('ansible.module_utils.urls.SSLValidationHandler.__init__', return_value=None)
    return SSLValidationHandler()

def test_detect_no_proxy_with_no_proxy_set(ssl_validation_handler, mocker):
    url = 'http://example.com'
    mocker.patch.dict(os.environ, {'no_proxy': 'example.com,another.com'})
    
    result = ssl_validation_handler.detect_no_proxy(url)
    
    assert result is False

def test_detect_no_proxy_with_no_proxy_not_set(ssl_validation_handler, mocker):
    url = 'http://example.com'
    mocker.patch.dict(os.environ, {}, clear=True)
    
    result = ssl_validation_handler.detect_no_proxy(url)
    
    assert result is True

def test_detect_no_proxy_with_no_matching_proxy(ssl_validation_handler, mocker):
    url = 'http://example.com'
    mocker.patch.dict(os.environ, {'no_proxy': 'another.com'})
    
    result = ssl_validation_handler.detect_no_proxy(url)
    
    assert result is True
