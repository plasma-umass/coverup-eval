# file: lib/ansible/module_utils/urls.py:493-495
# asked: {"lines": [493, 494, 495], "branches": []}
# gained: {"lines": [493, 494, 495], "branches": []}

import pytest
from ansible.module_utils.urls import SSLValidationError, ConnectionError

def test_ssl_validation_error_inheritance():
    # Verify that SSLValidationError is a subclass of ConnectionError
    assert issubclass(SSLValidationError, ConnectionError)

def test_ssl_validation_error_instance():
    # Verify that an instance of SSLValidationError can be created
    error_instance = SSLValidationError("SSL validation failed")
    assert isinstance(error_instance, SSLValidationError)
    assert isinstance(error_instance, ConnectionError)
    assert str(error_instance) == "SSL validation failed"
