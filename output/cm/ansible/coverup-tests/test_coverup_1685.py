# file lib/ansible/vars/hostvars.py:79-90
# lines [90]
# branches ['86->89', '89->90']

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

class MockVariableManager:
    def __init__(self):
        self._loader = None
        self._hostvars = None

@pytest.fixture
def hostvars_fixture():
    inventory = MagicMock()
    variable_manager = MockVariableManager()
    loader = MagicMock()
    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars._variable_manager = variable_manager
    return hostvars

def test_hostvars_setstate_loader_and_hostvars(hostvars_fixture):
    # Set _loader and _hostvars to None to trigger the conditional branches
    hostvars_fixture._variable_manager._loader = None
    hostvars_fixture._variable_manager._hostvars = None
    hostvars_fixture._loader = MagicMock()
    
    # Call __setstate__ to execute the conditional branches
    hostvars_fixture.__setstate__({'some_state': 'some_value'})
    
    # Assert that _loader and _hostvars are set correctly
    assert hostvars_fixture._variable_manager._loader == hostvars_fixture._loader
    assert hostvars_fixture._variable_manager._hostvars == hostvars_fixture
