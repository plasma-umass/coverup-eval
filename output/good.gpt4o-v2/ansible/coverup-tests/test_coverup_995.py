# file: lib/ansible/vars/hostvars.py:107-109
# asked: {"lines": [107, 109], "branches": []}
# gained: {"lines": [107, 109], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def hostvars():
    inventory_mock = MagicMock()
    variable_manager_mock = MagicMock()
    loader_mock = MagicMock()
    return HostVars(inventory=inventory_mock, variable_manager=variable_manager_mock, loader=loader_mock)

def test_contains_host_found(hostvars):
    host_name = "existing_host"
    hostvars._inventory.get_host.return_value = True

    assert host_name in hostvars

def test_contains_host_not_found(hostvars):
    host_name = "non_existing_host"
    hostvars._inventory.get_host.return_value = None

    assert host_name not in hostvars
