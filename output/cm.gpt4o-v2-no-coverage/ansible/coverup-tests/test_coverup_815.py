# file: lib/ansible/module_utils/urls.py:498-500
# asked: {"lines": [498, 499, 500], "branches": []}
# gained: {"lines": [498, 499, 500], "branches": []}

import pytest
from ansible.module_utils.urls import NoSSLError, SSLValidationError

def test_nosslerror_inheritance():
    # Verify that NoSSLError is a subclass of SSLValidationError
    assert issubclass(NoSSLError, SSLValidationError)

def test_nosslerror_instance():
    # Verify that an instance of NoSSLError can be created and is an instance of both NoSSLError and SSLValidationError
    error_instance = NoSSLError("No SSL library available")
    assert isinstance(error_instance, NoSSLError)
    assert isinstance(error_instance, SSLValidationError)
    assert str(error_instance) == "No SSL library available"
