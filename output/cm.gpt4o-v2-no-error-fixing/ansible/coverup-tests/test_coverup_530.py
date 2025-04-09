# file: lib/ansible/module_utils/urls.py:498-500
# asked: {"lines": [498, 499, 500], "branches": []}
# gained: {"lines": [498, 499, 500], "branches": []}

import pytest
from ansible.module_utils.urls import NoSSLError, SSLValidationError

def test_nosslerror_inheritance():
    # Verify that NoSSLError is a subclass of SSLValidationError
    assert issubclass(NoSSLError, SSLValidationError)

def test_nosslerror_instantiation():
    # Verify that NoSSLError can be instantiated
    error_instance = NoSSLError("SSL library not available")
    assert isinstance(error_instance, NoSSLError)
    assert str(error_instance) == "SSL library not available"
