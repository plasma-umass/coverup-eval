# file: lib/ansible/vars/manager.py:655-659
# asked: {"lines": [655, 659], "branches": []}
# gained: {"lines": [655, 659], "branches": []}

import pytest
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    vm = VariableManager()
    vm._fact_cache = {'test_host': 'some_fact'}
    return vm

def test_clear_facts(variable_manager):
    hostname = 'test_host'
    variable_manager.clear_facts(hostname)
    assert hostname not in variable_manager._fact_cache
