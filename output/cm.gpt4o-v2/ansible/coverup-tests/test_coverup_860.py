# file: lib/ansible/inventory/host.py:37-38
# asked: {"lines": [37, 38], "branches": []}
# gained: {"lines": [37, 38], "branches": []}

import pytest
from ansible.inventory.host import Host

def test_host_setstate():
    data = {
        'name': 'test_host',
        'vars': {'var1': 'value1'},
        'address': '192.168.1.1',
        'uuid': '1234-5678',
        'implicit': True,
        'groups': []
    }
    
    host = Host()
    host.__setstate__(data)
    
    assert host.name == 'test_host'
    assert host.vars == {'var1': 'value1'}
    assert host.address == '192.168.1.1'
    assert host._uuid == '1234-5678'
    assert host.implicit is True
    assert host.groups == []
