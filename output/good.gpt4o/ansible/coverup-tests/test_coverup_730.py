# file lib/ansible/module_utils/urls.py:498-500
# lines [498, 499, 500]
# branches []

import pytest
from ansible.module_utils.urls import SSLValidationError

def test_NoSSLError():
    class NoSSLError(SSLValidationError):
        """Needed to connect to an HTTPS url but no ssl library available to verify the certificate"""
        pass

    # Create an instance of NoSSLError
    error_instance = NoSSLError("SSL library not available")

    # Assert that the instance is indeed an instance of NoSSLError and SSLValidationError
    assert isinstance(error_instance, NoSSLError)
    assert isinstance(error_instance, SSLValidationError)

    # Assert that the error message is correctly set
    assert str(error_instance) == "SSL library not available"
