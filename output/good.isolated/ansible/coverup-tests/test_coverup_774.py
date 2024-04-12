# file lib/ansible/module_utils/urls.py:493-495
# lines [493, 494, 495]
# branches []

import pytest
from ansible.module_utils.urls import SSLValidationError

def test_ssl_validation_error():
    with pytest.raises(SSLValidationError) as exc_info:
        raise SSLValidationError("SSL validation failed")

    assert str(exc_info.value) == "SSL validation failed", "SSLValidationError did not contain the correct message"
