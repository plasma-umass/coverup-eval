# file: lib/ansible/module_utils/urls.py:493-495
# asked: {"lines": [493, 494, 495], "branches": []}
# gained: {"lines": [493, 494, 495], "branches": []}

import pytest
from ansible.module_utils.urls import SSLValidationError, ConnectionError

def test_ssl_validation_error_inheritance():
    with pytest.raises(SSLValidationError):
        raise SSLValidationError("SSL validation failed")

    assert issubclass(SSLValidationError, ConnectionError)
