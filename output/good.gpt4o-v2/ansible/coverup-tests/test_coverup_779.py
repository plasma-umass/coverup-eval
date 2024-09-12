# file: lib/ansible/vars/hostvars.py:57-59
# asked: {"lines": [57, 58, 59], "branches": []}
# gained: {"lines": [57, 58, 59], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def hostvars_instance(mock_variable_manager):
    inventory = MagicMock()
    loader = MagicMock()
    return HostVars(inventory, mock_variable_manager, loader)

def test_set_variable_manager(hostvars_instance, mock_variable_manager):
    new_variable_manager = MagicMock()
    hostvars_instance.set_variable_manager(new_variable_manager)
    
    assert hostvars_instance._variable_manager == new_variable_manager
    assert new_variable_manager._hostvars == hostvars_instance
