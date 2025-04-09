# file: lib/ansible/module_utils/urls.py:1018-1032
# asked: {"lines": [1022, 1023, 1024, 1025, 1027, 1028, 1031, 1032], "branches": [[1023, 1024], [1023, 1032], [1027, 1028], [1027, 1032], [1028, 1027], [1028, 1031]]}
# gained: {"lines": [1022, 1023, 1024, 1025, 1027, 1028, 1031, 1032], "branches": [[1023, 1024], [1023, 1032], [1027, 1028], [1027, 1032], [1028, 1027], [1028, 1031]]}

import os
import pytest
from ansible.module_utils.urls import SSLValidationHandler

@pytest.fixture
def ssl_validation_handler():
    return SSLValidationHandler('hostname', 443)

def test_detect_no_proxy_with_no_proxy_set(ssl_validation_handler, monkeypatch):
    monkeypatch.setenv('no_proxy', 'example.com,localhost')
    assert not ssl_validation_handler.detect_no_proxy('http://example.com')
    assert not ssl_validation_handler.detect_no_proxy('http://localhost:8080')
    assert ssl_validation_handler.detect_no_proxy('http://otherdomain.com')

def test_detect_no_proxy_with_no_proxy_not_set(ssl_validation_handler, monkeypatch):
    monkeypatch.delenv('no_proxy', raising=False)
    assert ssl_validation_handler.detect_no_proxy('http://example.com')
    assert ssl_validation_handler.detect_no_proxy('http://localhost:8080')
    assert ssl_validation_handler.detect_no_proxy('http://otherdomain.com')
