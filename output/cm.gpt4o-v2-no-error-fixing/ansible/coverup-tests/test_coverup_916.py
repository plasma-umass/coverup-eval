# file: lib/ansible/inventory/host.py:86-100
# asked: {"lines": [96], "branches": [[95, 96]]}
# gained: {"lines": [96], "branches": [[95, 96]]}

import pytest
from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host(name="localhost")

def test_host_initialization_with_port(host):
    host_with_port = Host(name="localhost", port=22)
    assert host_with_port.vars['ansible_port'] == 22

def test_host_initialization_without_port(host):
    assert 'ansible_port' not in host.vars

def test_host_set_variable(host):
    host.set_variable('ansible_port', 2222)
    assert host.vars['ansible_port'] == 2222
