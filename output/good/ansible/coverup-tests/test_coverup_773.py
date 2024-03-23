# file lib/ansible/module_utils/urls.py:488-490
# lines [488, 489, 490]
# branches []

import pytest
from ansible.module_utils.urls import ProxyError

def test_proxy_error():
    with pytest.raises(ProxyError) as exc_info:
        raise ProxyError("Proxy connection failed")

    assert str(exc_info.value) == "Proxy connection failed", "ProxyError did not contain the correct message"
