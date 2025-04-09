# file: lib/ansible/inventory/host.py:71-84
# asked: {"lines": [71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84], "branches": [[81, 0], [81, 82]]}
# gained: {"lines": [71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84], "branches": [[81, 0], [81, 82]]}

import pytest
from ansible.inventory.host import Host, Group

@pytest.fixture
def host():
    return Host()

def test_deserialize_with_all_fields(monkeypatch, host):
    data = {
        'name': 'test_host',
        'vars': {'var1': 'value1'},
        'address': '192.168.1.1',
        'uuid': '1234-5678',
        'implicit': True,
        'groups': [{'name': 'group1'}, {'name': 'group2'}]
    }

    # Mock the Group class to avoid side effects
    class MockGroup:
        def __init__(self):
            self.name = None

        def deserialize(self, data):
            self.name = data.get('name')

    monkeypatch.setattr('ansible.inventory.host.Group', MockGroup)

    host.deserialize(data)

    assert host.name == 'test_host'
    assert host.vars == {'var1': 'value1'}
    assert host.address == '192.168.1.1'
    assert host._uuid == '1234-5678'
    assert host.implicit is True
    assert len(host.groups) == 2
    assert host.groups[0].name == 'group1'
    assert host.groups[1].name == 'group2'

def test_deserialize_with_minimal_fields(monkeypatch, host):
    data = {
        'name': 'test_host_minimal'
    }

    # Mock the Group class to avoid side effects
    class MockGroup:
        def __init__(self):
            self.name = None

        def deserialize(self, data):
            self.name = data.get('name')

    monkeypatch.setattr('ansible.inventory.host.Group', MockGroup)

    host.deserialize(data)

    assert host.name == 'test_host_minimal'
    assert host.vars == {}
    assert host.address == ''
    assert host._uuid is None
    assert host.implicit is False
    assert len(host.groups) == 0
