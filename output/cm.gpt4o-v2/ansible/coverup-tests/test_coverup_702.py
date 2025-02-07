# file: lib/ansible/module_utils/urls.py:904-907
# asked: {"lines": [904, 905, 906, 907], "branches": []}
# gained: {"lines": [904, 905, 906, 907], "branches": []}

import pytest
from ansible.module_utils.urls import SSLValidationHandler

def test_ssl_validation_handler_init():
    hostname = "example.com"
    port = 443
    ca_path = "/path/to/ca"

    handler = SSLValidationHandler(hostname, port, ca_path)

    assert handler.hostname == hostname
    assert handler.port == port
    assert handler.ca_path == ca_path

def test_ssl_validation_handler_init_no_ca_path():
    hostname = "example.com"
    port = 443

    handler = SSLValidationHandler(hostname, port)

    assert handler.hostname == hostname
    assert handler.port == port
    assert handler.ca_path is None
