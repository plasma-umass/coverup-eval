# file: lib/ansible/module_utils/urls.py:488-490
# asked: {"lines": [488, 489, 490], "branches": []}
# gained: {"lines": [488, 489, 490], "branches": []}

import pytest
from ansible.module_utils.urls import ConnectionError

def test_proxy_error_inheritance():
    class ProxyError(ConnectionError):
        """Failure to connect because of a proxy"""
        pass

    with pytest.raises(ProxyError):
        raise ProxyError("Proxy connection failed")

    assert issubclass(ProxyError, ConnectionError)
