# file: lib/ansible/inventory/host.py:86-100
# asked: {"lines": [96], "branches": [[95, 96]]}
# gained: {"lines": [96], "branches": [[95, 96]]}

import pytest
from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host(name="localhost")

def test_host_initialization_with_port(monkeypatch):
    def mock_set_variable(self, key, value):
        self.vars[key] = value

    monkeypatch.setattr(Host, "set_variable", mock_set_variable)
    
    host = Host(name="localhost", port=22)
    assert host.vars["ansible_port"] == 22

def test_host_initialization_without_port():
    host = Host(name="localhost")
    assert "ansible_port" not in host.vars
