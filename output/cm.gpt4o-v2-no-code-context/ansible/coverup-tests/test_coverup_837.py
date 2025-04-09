# file: lib/ansible/vars/hostvars.py:107-109
# asked: {"lines": [107, 109], "branches": []}
# gained: {"lines": [107, 109], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def hostvars():
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    hv = HostVars(inventory, variable_manager, loader)
    hv._find_host = MagicMock()
    return hv

def test_hostvars_contains_true(hostvars):
    hostvars._find_host.return_value = 'some_host'
    assert 'some_host' in hostvars
    hostvars._find_host.assert_called_once_with('some_host')

def test_hostvars_contains_false(hostvars):
    hostvars._find_host.return_value = None
    assert 'non_existent_host' not in hostvars
    hostvars._find_host.assert_called_once_with('non_existent_host')
