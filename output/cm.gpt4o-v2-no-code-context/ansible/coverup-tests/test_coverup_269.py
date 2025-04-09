# file: lib/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [86, 87, 88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [86, 87, 88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest
from unittest.mock import MagicMock

# Mocking the necessary imports
class AnsibleUnsafe:
    pass

class AnsibleUnsafeText(str):
    pass

def to_text(obj, errors='strict'):
    return str(obj)

class MockDisplay:
    def deprecated(self, msg, version, collection_name):
        pass

@pytest.fixture
def mock_display(monkeypatch):
    monkeypatch.setattr('ansible.utils.display.Display', MockDisplay)
    monkeypatch.setattr('ansible.utils.unsafe_proxy.AnsibleUnsafe', AnsibleUnsafe)
    monkeypatch.setattr('ansible.utils.unsafe_proxy.AnsibleUnsafeText', AnsibleUnsafeText)
    monkeypatch.setattr('ansible.utils.unsafe_proxy.to_text', to_text)

def test_unsafe_proxy_with_ansible_unsafe(mock_display):
    from ansible.utils.unsafe_proxy import UnsafeProxy
    obj = AnsibleUnsafe()
    proxy = UnsafeProxy(obj)
    assert proxy is obj

def test_unsafe_proxy_with_string(mock_display):
    from ansible.utils.unsafe_proxy import UnsafeProxy
    obj = "test string"
    proxy = UnsafeProxy(obj)
    assert isinstance(proxy, AnsibleUnsafeText)
    assert proxy == to_text(obj, errors='surrogate_or_strict')

def test_unsafe_proxy_with_other_type(mock_display):
    from ansible.utils.unsafe_proxy import UnsafeProxy
    obj = 12345
    proxy = UnsafeProxy(obj)
    assert proxy is obj
