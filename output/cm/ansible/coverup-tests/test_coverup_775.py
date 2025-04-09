# file lib/ansible/module_utils/urls.py:498-500
# lines [498, 499, 500]
# branches []

import pytest
from ansible.module_utils.urls import NoSSLError

def test_no_ssl_error():
    with pytest.raises(NoSSLError) as exc_info:
        raise NoSSLError("SSL library is not available")

    assert str(exc_info.value) == "SSL library is not available", "NoSSLError message should match the expected message"
