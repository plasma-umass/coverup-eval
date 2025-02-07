# file: lib/ansible/vars/hostvars.py:92-96
# asked: {"lines": [92, 93, 94, 95, 96], "branches": [[94, 95], [94, 96]]}
# gained: {"lines": [92, 93, 94, 95, 96], "branches": [[94, 95], [94, 96]]}

import pytest
from ansible.template import AnsibleUndefined
from ansible.vars.hostvars import HostVars, HostVarsVars

class MockLoader:
    pass

class MockVariableManager:
    def get_vars(self, host, include_hostvars):
        return {"var1": "value1"}

class MockInventory:
    def __init__(self):
        self.hosts = {}

class MockHost:
    pass

@pytest.fixture
def hostvars():
    inventory = MockInventory()
    variable_manager = MockVariableManager()
    loader = MockLoader()
    hv = HostVars(inventory, variable_manager, loader)
    hv._find_host = lambda x: MockHost() if x == "existing_host" else None
    return hv

def test_getitem_with_existing_host(hostvars):
    result = hostvars["existing_host"]
    assert isinstance(result, HostVarsVars)
    assert result._vars == {"var1": "value1"}
    assert result._loader == hostvars._loader

def test_getitem_with_non_existing_host(hostvars):
    result = hostvars["non_existing_host"]
    assert isinstance(result, AnsibleUndefined)
    assert repr(result) == "AnsibleUndefined"
