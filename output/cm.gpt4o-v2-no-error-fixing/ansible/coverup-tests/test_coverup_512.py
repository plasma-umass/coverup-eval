# file: lib/ansible/module_utils/urls.py:488-490
# asked: {"lines": [488, 489, 490], "branches": []}
# gained: {"lines": [488, 489, 490], "branches": []}

import pytest
from ansible.module_utils.urls import ProxyError, ConnectionError

def test_proxy_error_inheritance():
    with pytest.raises(ProxyError) as excinfo:
        raise ProxyError("Proxy connection failed")
    assert isinstance(excinfo.value, ProxyError)
    assert isinstance(excinfo.value, ConnectionError)
    assert str(excinfo.value) == "Proxy connection failed"
