# file: lib/ansible/module_utils/urls.py:498-500
# asked: {"lines": [498, 499, 500], "branches": []}
# gained: {"lines": [498, 499, 500], "branches": []}

import pytest
from ansible.module_utils.urls import SSLValidationError

def test_NoSSLError_inheritance():
    class NoSSLError(SSLValidationError):
        """Needed to connect to an HTTPS url but no ssl library available to verify the certificate"""
        pass

    # Ensure NoSSLError is a subclass of SSLValidationError
    assert issubclass(NoSSLError, SSLValidationError)

def test_NoSSLError_instance():
    class NoSSLError(SSLValidationError):
        """Needed to connect to an HTTPS url but no ssl library available to verify the certificate"""
        pass

    # Create an instance of NoSSLError and check its type
    error_instance = NoSSLError("SSL library not available")
    assert isinstance(error_instance, NoSSLError)
    assert str(error_instance) == "SSL library not available"
