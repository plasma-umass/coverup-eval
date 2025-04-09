# file: lib/ansible/inventory/host.py:57-69
# asked: {"lines": [57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68], "branches": [[59, 60], [59, 62]]}
# gained: {"lines": [57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68], "branches": [[59, 60], [59, 62]]}

import pytest
from unittest.mock import Mock, patch
from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host(name="localhost", port=None, gen_uuid=False)

def test_serialize_empty_groups(host):
    serialized = host.serialize()
    assert serialized["name"] == "localhost"
    assert serialized["vars"] == {}
    assert serialized["address"] == "localhost"
    assert serialized["uuid"] is None
    assert serialized["groups"] == []
    assert serialized["implicit"] is False

def test_serialize_with_groups(host):
    mock_group = Mock()
    mock_group.serialize.return_value = {"name": "group1"}
    host.groups.append(mock_group)
    
    serialized = host.serialize()
    assert serialized["groups"] == [{"name": "group1"}]

def test_serialize_with_vars(host):
    host.vars = {"var1": "value1"}
    
    serialized = host.serialize()
    assert serialized["vars"] == {"var1": "value1"}

def test_serialize_with_uuid(monkeypatch):
    mock_uuid = "1234-5678"
    monkeypatch.setattr("ansible.inventory.host.get_unique_id", lambda: mock_uuid)
    host = Host(name="localhost", port=22, gen_uuid=True)
    
    serialized = host.serialize()
    assert serialized["uuid"] == mock_uuid
