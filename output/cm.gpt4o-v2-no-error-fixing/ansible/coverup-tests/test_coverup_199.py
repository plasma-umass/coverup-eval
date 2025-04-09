# file: lib/ansible/inventory/host.py:57-69
# asked: {"lines": [57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68], "branches": [[59, 60], [59, 62]]}
# gained: {"lines": [57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68], "branches": [[59, 60], [59, 62]]}

import pytest
from ansible.inventory.host import Host

class MockGroup:
    def serialize(self):
        return {"mock": "group"}

@pytest.fixture
def host():
    return Host(name="test_host")

def test_serialize_no_groups(host):
    expected = {
        "name": "test_host",
        "vars": {},
        "address": "test_host",
        "uuid": host._uuid,
        "groups": [],
        "implicit": False,
    }
    assert host.serialize() == expected

def test_serialize_with_groups(host, monkeypatch):
    mock_group = MockGroup()
    monkeypatch.setattr(host, 'groups', [mock_group])
    
    expected = {
        "name": "test_host",
        "vars": {},
        "address": "test_host",
        "uuid": host._uuid,
        "groups": [{"mock": "group"}],
        "implicit": False,
    }
    assert host.serialize() == expected
