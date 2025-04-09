# file lib/ansible/module_utils/urls.py:488-490
# lines [488, 489, 490]
# branches []

import pytest
from ansible.module_utils.urls import ConnectionError

def test_proxy_error():
    class ProxyError(ConnectionError):
        """Failure to connect because of a proxy"""
        pass

    with pytest.raises(ProxyError):
        raise ProxyError("Proxy connection failed")

    proxy_error_instance = ProxyError("Proxy connection failed")
    assert isinstance(proxy_error_instance, ConnectionError)
    assert str(proxy_error_instance) == "Proxy connection failed"
