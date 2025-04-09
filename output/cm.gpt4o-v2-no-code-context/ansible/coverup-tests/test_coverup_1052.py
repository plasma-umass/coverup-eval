# file: lib/ansible/inventory/host.py:86-100
# asked: {"lines": [96], "branches": [[95, 96]]}
# gained: {"lines": [96], "branches": [[95, 96]]}

import pytest
from ansible.inventory.host import Host

def test_host_with_port():
    host = Host(name="localhost", port=22)
    assert host.vars['ansible_port'] == 22

def test_host_without_port():
    host = Host(name="localhost")
    assert 'ansible_port' not in host.vars

def test_host_with_gen_uuid(monkeypatch):
    def mock_get_unique_id():
        return "mocked-uuid"
    
    monkeypatch.setattr('ansible.inventory.host.get_unique_id', mock_get_unique_id)
    host = Host(name="localhost", gen_uuid=True)
    assert host._uuid == "mocked-uuid"

def test_host_without_gen_uuid():
    host = Host(name="localhost", gen_uuid=False)
    assert host._uuid is None
