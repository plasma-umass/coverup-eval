# file: lib/ansible/vars/hostvars.py:92-96
# asked: {"lines": [93, 94, 95, 96], "branches": [[94, 95], [94, 96]]}
# gained: {"lines": [93, 94, 95, 96], "branches": [[94, 95], [94, 96]]}

import pytest
from ansible.template import AnsibleUndefined
from ansible.vars.hostvars import HostVars, HostVarsVars

class MockLoader:
    pass

class MockHostVars(HostVars):
    def __init__(self):
        self._loader = MockLoader()
    
    def raw_get(self, host_name):
        if host_name == "undefined_host":
            return AnsibleUndefined()
        elif host_name == "defined_host":
            return {"var1": "value1"}
        return None

@pytest.fixture
def hostvars():
    return MockHostVars()

def test_getitem_with_undefined_host(hostvars):
    result = hostvars["undefined_host"]
    assert isinstance(result, AnsibleUndefined)

def test_getitem_with_defined_host(hostvars):
    result = hostvars["defined_host"]
    assert isinstance(result, HostVarsVars)
    assert result._vars == {"var1": "value1"}
    assert isinstance(result._loader, MockLoader)
