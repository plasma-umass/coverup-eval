# file: lib/ansible/inventory/host.py:37-38
# asked: {"lines": [38], "branches": []}
# gained: {"lines": [38], "branches": []}

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
        'groups': [{'name': 'group1'}, {'name': 'group2'}]
    }

def test_host_setstate(host_data, mocker):
    mocker.patch('ansible.inventory.group.Group.deserialize', return_value=None)
    
    host = Host()
    host.__setstate__(host_data)
    
    assert host.name == 'test_host'
    assert host.vars == {'var1': 'value1'}
    assert host.address == '192.168.1.1'
    assert host._uuid == '1234-5678'
    assert host.implicit is True
    assert len(host.groups) == 2
    assert isinstance(host.groups[0], Group)
    assert isinstance(host.groups[1], Group)
