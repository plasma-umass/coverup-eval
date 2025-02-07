# file: lib/ansible/module_utils/urls.py:488-490
# asked: {"lines": [488, 489, 490], "branches": []}
# gained: {"lines": [488, 489, 490], "branches": []}

import pytest
from ansible.module_utils.urls import ProxyError

def test_proxy_error_inheritance():
    with pytest.raises(ProxyError):
        raise ProxyError("Proxy connection failed")

def test_proxy_error_message():
    try:
        raise ProxyError("Proxy connection failed")
    except ProxyError as e:
        assert str(e) == "Proxy connection failed"
