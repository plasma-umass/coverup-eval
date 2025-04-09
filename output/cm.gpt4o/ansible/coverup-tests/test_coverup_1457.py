# file lib/ansible/inventory/host.py:86-100
# lines [96]
# branches ['95->96']

import pytest
from ansible.inventory.host import Host

def test_host_with_port():
    host = Host(name="localhost", port=22)
    assert host.vars['ansible_port'] == 22
    assert host.name == "localhost"
    assert host.address == "localhost"
    assert host._uuid is not None
    assert host.implicit is False

def test_host_without_port():
    host = Host(name="localhost")
    assert 'ansible_port' not in host.vars
    assert host.name == "localhost"
    assert host.address == "localhost"
    assert host._uuid is not None
    assert host.implicit is False
