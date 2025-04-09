# file: lib/ansible/inventory/host.py:71-84
# asked: {"lines": [72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84], "branches": [[81, 0], [81, 82]]}
# gained: {"lines": [72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84], "branches": [[81, 0], [81, 82]]}

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
            {'name': 'group1', 'vars': {'gvar1': 'gvalue1'}},
            {'name': 'group2', 'vars': {'gvar2': 'gvalue2'}}
        ]
    }

def test_host_deserialize(host_data, monkeypatch):
    def mock_get_unique_id():
        return 'mock-uuid'
    
    monkeypatch.setattr('ansible.inventory.host.get_unique_id', mock_get_unique_id)
    
    host = Host()
    host.deserialize(host_data)
    
    assert host.name == 'test_host'
    assert host.vars == {'var1': 'value1'}
    assert host.address == '192.168.1.1'
    assert host._uuid == '1234-5678'
    assert host.implicit is True
    assert len(host.groups) == 2
    assert host.groups[0].name == 'group1'
    assert host.groups[0].vars == {'gvar1': 'gvalue1'}
    assert host.groups[1].name == 'group2'
    assert host.groups[1].vars == {'gvar2': 'gvalue2'}
