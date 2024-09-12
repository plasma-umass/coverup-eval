# file: lib/ansible/module_utils/urls.py:904-907
# asked: {"lines": [904, 905, 906, 907], "branches": []}
# gained: {"lines": [904, 905, 906, 907], "branches": []}

import pytest
from unittest import mock
from ansible.module_utils.urls import SSLValidationHandler
import urllib.request as urllib_request

@pytest.fixture
def ssl_validation_handler():
    return SSLValidationHandler(hostname="example.com", port=443, ca_path="/path/to/ca")

def test_ssl_validation_handler_init(ssl_validation_handler):
    assert ssl_validation_handler.hostname == "example.com"
    assert ssl_validation_handler.port == 443
    assert ssl_validation_handler.ca_path == "/path/to/ca"

def test_ssl_validation_handler_no_ca_path():
    handler = SSLValidationHandler(hostname="example.com", port=443)
    assert handler.hostname == "example.com"
    assert handler.port == 443
    assert handler.ca_path is None
