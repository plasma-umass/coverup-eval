# file: lib/ansible/module_utils/urls.py:493-495
# asked: {"lines": [493, 494, 495], "branches": []}
# gained: {"lines": [493, 494, 495], "branches": []}

import pytest
from ansible.module_utils.urls import SSLValidationError, ConnectionError

def test_ssl_validation_error_inheritance():
    error_instance = SSLValidationError("SSL validation failed")
    assert isinstance(error_instance, SSLValidationError)
    assert isinstance(error_instance, ConnectionError)
    assert str(error_instance) == "SSL validation failed"

def test_ssl_validation_error_message():
    error_message = "SSL validation failed due to expired certificate"
    error_instance = SSLValidationError(error_message)
    assert str(error_instance) == error_message
