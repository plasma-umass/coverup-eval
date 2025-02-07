# file: lib/ansible/vars/hostvars.py:124-128
# asked: {"lines": [124, 128], "branches": []}
# gained: {"lines": [124, 128], "branches": []}

import pytest
import copy
from ansible.vars.hostvars import HostVars

class MockInventory:
    pass

class MockVariableManager:
    pass

class MockLoader:
    pass

@pytest.fixture
def hostvars():
    inventory = MockInventory()
    variable_manager = MockVariableManager()
    loader = MockLoader()
    return HostVars(inventory, variable_manager, loader)

def test_deepcopy_hostvars(hostvars):
    memo = {}
    copied_hostvars = copy.deepcopy(hostvars, memo)
    assert copied_hostvars is hostvars
