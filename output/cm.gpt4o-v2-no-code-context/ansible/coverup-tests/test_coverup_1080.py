# file: lib/ansible/inventory/host.py:34-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

import pytest
from ansible.inventory.host import Host

class MockHost(Host):
    def serialize(self):
        return {'mock': 'data'}

@pytest.fixture
def mock_host():
    return MockHost()

def test_host_getstate(monkeypatch, mock_host):
    def mock_serialize():
        return {'mock': 'data'}
    
    monkeypatch.setattr(mock_host, 'serialize', mock_serialize)
    state = mock_host.__getstate__()
    assert state == {'mock': 'data'}
