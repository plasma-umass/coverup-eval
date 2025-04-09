# file lib/ansible/vars/hostvars.py:79-90
# lines [80, 86, 87, 89, 90]
# branches ['86->87', '86->89', '89->exit', '89->90']

import pytest
from unittest.mock import Mock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_variable_manager():
    return Mock()

@pytest.fixture
def hostvars_instance(mock_variable_manager):
    inventory = Mock()
    inventory.hosts = []  # Mock the hosts attribute to avoid iteration issues
    loader = Mock()
    hv = HostVars(inventory, mock_variable_manager, loader)
    return hv

def test_hostvars_setstate(mock_variable_manager, hostvars_instance):
    state = {'_variable_manager': mock_variable_manager, '_loader': Mock()}
    hostvars_instance.__setstate__(state)

    assert hostvars_instance._variable_manager == mock_variable_manager
    assert hostvars_instance._loader == state['_loader']

    # Ensure the lines 86-90 are executed
    mock_variable_manager._loader = None
    mock_variable_manager._hostvars = None

    hostvars_instance.__setstate__(state)

    assert mock_variable_manager._loader == hostvars_instance._loader
    assert mock_variable_manager._hostvars == hostvars_instance
