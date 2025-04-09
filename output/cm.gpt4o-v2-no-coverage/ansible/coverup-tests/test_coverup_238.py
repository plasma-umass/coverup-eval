# file: lib/ansible/inventory/data.py:80-102
# asked: {"lines": [80, 82, 83, 85, 87, 88, 91, 92, 94, 95, 97, 98, 100, 102], "branches": [[82, 83], [82, 85], [92, 94], [92, 97]]}
# gained: {"lines": [80, 82, 83, 85, 87, 88, 91, 92, 94, 95, 97, 98, 100, 102], "branches": [[82, 83], [82, 85], [92, 94], [92, 97]]}

import pytest
import sys
from ansible.inventory.data import InventoryData
from ansible.inventory.host import Host

class MockDisplay:
    def warning(self, msg):
        pass

@pytest.fixture
def inventory_data(monkeypatch):
    inventory = InventoryData()
    inventory.localhost = None
    monkeypatch.setattr('ansible.inventory.data.display', MockDisplay())
    return inventory

def test_create_implicit_localhost_with_existing_localhost(inventory_data):
    existing_host = Host('localhost')
    inventory_data.localhost = existing_host

    result = inventory_data._create_implicit_localhost('localhost')

    assert result == existing_host
    assert result.address == 'localhost'
    assert not result.implicit

def test_create_implicit_localhost_without_existing_localhost(monkeypatch, inventory_data):
    monkeypatch.setattr(sys, 'executable', '/usr/bin/python3')

    result = inventory_data._create_implicit_localhost('localhost')

    assert result.address == '127.0.0.1'
    assert result.implicit
    assert result.vars['ansible_python_interpreter'] == '/usr/bin/python3'
    assert result.vars['ansible_connection'] == 'local'
    assert inventory_data.localhost == result

def test_create_implicit_localhost_without_sys_executable(monkeypatch, inventory_data):
    monkeypatch.setattr(sys, 'executable', None)

    result = inventory_data._create_implicit_localhost('localhost')

    assert result.address == '127.0.0.1'
    assert result.implicit
    assert result.vars['ansible_python_interpreter'] == '/usr/bin/python'
    assert result.vars['ansible_connection'] == 'local'
    assert inventory_data.localhost == result
