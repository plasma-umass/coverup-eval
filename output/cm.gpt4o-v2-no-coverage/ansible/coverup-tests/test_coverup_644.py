# file: lib/ansible/vars/hostvars.py:68-77
# asked: {"lines": [68, 73, 74, 75, 77], "branches": [[74, 75], [74, 77]]}
# gained: {"lines": [68, 73, 74, 75, 77], "branches": [[74, 75], [74, 77]]}

import pytest
from unittest.mock import MagicMock
from ansible.template import AnsibleUndefined
from ansible.vars.hostvars import HostVars

@pytest.fixture
def hostvars():
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    return HostVars(inventory, variable_manager, loader)

def test_raw_get_host_not_found(hostvars):
    hostvars._inventory.get_host.return_value = None
    result = hostvars.raw_get('nonexistent_host')
    assert isinstance(result, AnsibleUndefined)
    assert result._undefined_name == "hostvars['nonexistent_host']"

def test_raw_get_host_found(hostvars):
    mock_host = MagicMock()
    hostvars._inventory.get_host.return_value = mock_host
    expected_vars = {'var1': 'value1'}
    hostvars._variable_manager.get_vars.return_value = expected_vars

    result = hostvars.raw_get('existent_host')
    assert result == expected_vars
    hostvars._variable_manager.get_vars.assert_called_once_with(host=mock_host, include_hostvars=False)
