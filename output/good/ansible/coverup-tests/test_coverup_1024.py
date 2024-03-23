# file lib/ansible/vars/manager.py:655-659
# lines [655, 659]
# branches []

import pytest
from ansible.vars.manager import VariableManager

class MockVariableManager(VariableManager):
    def __init__(self):
        self._fact_cache = {}

@pytest.fixture
def variable_manager():
    return MockVariableManager()

def test_clear_facts(variable_manager):
    # Setup: Add a hostname and its facts to the fact cache
    hostname = 'test_host'
    variable_manager._fact_cache[hostname] = {'fact_key': 'fact_value'}

    # Precondition: Ensure the fact is in the cache
    assert hostname in variable_manager._fact_cache

    # Action: Clear the facts for the given hostname
    variable_manager.clear_facts(hostname)

    # Postcondition: Ensure the facts for the hostname are cleared from the cache
    assert hostname not in variable_manager._fact_cache

    # Cleanup is handled by the fixture's scope and garbage collection
