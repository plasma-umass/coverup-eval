# file: lib/ansible/inventory/host.py:54-55
# asked: {"lines": [54, 55], "branches": []}
# gained: {"lines": [54, 55], "branches": []}

import pytest
from ansible.inventory.host import Host

def test_host_repr():
    host_name = "test_host"
    host = Host(name=host_name)
    assert repr(host) == host_name
