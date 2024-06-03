# file lib/ansible/module_utils/urls.py:493-495
# lines [493, 494, 495]
# branches []

import pytest
from ansible.module_utils.urls import SSLValidationError

def test_ssl_validation_error():
    with pytest.raises(SSLValidationError):
        raise SSLValidationError("SSL validation failed")

    # Ensure the exception message is correct
    try:
        raise SSLValidationError("SSL validation failed")
    except SSLValidationError as e:
        assert str(e) == "SSL validation failed"
