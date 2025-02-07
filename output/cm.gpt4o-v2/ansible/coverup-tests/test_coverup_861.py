# file: lib/ansible/inventory/host.py:48-49
# asked: {"lines": [48, 49], "branches": []}
# gained: {"lines": [48, 49], "branches": []}

import pytest
from ansible.inventory.host import Host

def test_host_hash():
    host_name = "test_host"
    host = Host(name=host_name)
    assert hash(host) == hash(host_name)

