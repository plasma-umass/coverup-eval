# file: lib/ansible/inventory/host.py:102-103
# asked: {"lines": [102, 103], "branches": []}
# gained: {"lines": [102, 103], "branches": []}

import pytest
from ansible.inventory.host import Host

def test_get_name():
    host = Host(name="test_host")
    assert host.get_name() == "test_host"
