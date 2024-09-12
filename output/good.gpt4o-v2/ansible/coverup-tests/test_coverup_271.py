# file: lib/ansible/inventory/host.py:71-84
# asked: {"lines": [71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84], "branches": [[81, 0], [81, 82]]}
# gained: {"lines": [71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84], "branches": [[81, 0], [81, 82]]}

import pytest
from ansible.inventory.host import Host
from ansible.inventory.group import Group

@pytest.fixture
def host_data():
    return {
        'name': 'test_host',
        'vars': {'var1': 'value1'},
        'address': '192.168.1.1',
        'uuid': '1234-5678',
        'implicit': True,
        'groups': [
            {
                'name': 'group1',
                'vars': {'gvar1': 'gvalue1'},
                'depth': 1,
                'hosts': ['host1'],
                'parent_groups': []
            }
        ]
    }

def test_deserialize_host(monkeypatch, host_data):
    def mock_init(self, name=None, port=None, gen_uuid=True):
        self.vars = {}
        self.groups = []
        self._uuid = None
        self.name = name
        self.address = name
        self.implicit = False

    monkeypatch.setattr(Host, '__init__', mock_init)
    host = Host()
    host.deserialize(host_data)

    assert host.name == 'test_host'
    assert host.vars == {'var1': 'value1'}
    assert host.address == '192.168.1.1'
    assert host._uuid == '1234-5678'
    assert host.implicit is True
    assert len(host.groups) == 1
    assert isinstance(host.groups[0], Group)
    assert host.groups[0].name == 'group1'
    assert host.groups[0].vars == {'gvar1': 'gvalue1'}
    assert host.groups[0].depth == 1
    assert host.groups[0].hosts == ['host1']
