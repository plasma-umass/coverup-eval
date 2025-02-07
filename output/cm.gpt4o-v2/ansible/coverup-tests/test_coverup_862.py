# file: lib/ansible/inventory/host.py:51-52
# asked: {"lines": [51, 52], "branches": []}
# gained: {"lines": [51, 52], "branches": []}

import pytest
from ansible.inventory.host import Host

def test_host_str_method():
    host_name = "test_host"
    host = Host(name=host_name)
    
    assert str(host) == host_name

