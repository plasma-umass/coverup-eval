# file: lib/ansible/inventory/host.py:161-162
# asked: {"lines": [161, 162], "branches": []}
# gained: {"lines": [161, 162], "branches": []}

import pytest
from ansible.utils.vars import combine_vars
from ansible.inventory.host import Host

class MockHost(Host):
    def __init__(self, vars, magic_vars):
        self.vars = vars
        self._magic_vars = magic_vars

    def get_magic_vars(self):
        return self._magic_vars

@pytest.fixture
def host():
    return MockHost(vars={'var1': 'value1'}, magic_vars={'magic_var1': 'magic_value1'})

def test_get_vars(host):
    expected_vars = combine_vars(host.vars, host.get_magic_vars())
    assert host.get_vars() == expected_vars
