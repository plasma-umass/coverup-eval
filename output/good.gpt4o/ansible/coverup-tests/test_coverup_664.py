# file lib/ansible/module_utils/urls.py:904-907
# lines [904, 905, 906, 907]
# branches []

import pytest
from unittest import mock
from ansible.module_utils.urls import SSLValidationHandler

def test_ssl_validation_handler_initialization():
    hostname = 'example.com'
    port = 443
    ca_path = '/path/to/ca'

    handler = SSLValidationHandler(hostname, port, ca_path)

    assert handler.hostname == hostname
    assert handler.port == port
    assert handler.ca_path == ca_path

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Mock any global state or cleanup necessary
    yield
    # Perform cleanup actions if necessary
