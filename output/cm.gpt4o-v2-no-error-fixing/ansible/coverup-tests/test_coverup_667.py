# file: lib/ansible/vars/manager.py:655-659
# asked: {"lines": [655, 659], "branches": []}
# gained: {"lines": [655, 659], "branches": []}

import pytest
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    return VariableManager()

def test_clear_facts(variable_manager, mocker):
    # Setup: Add a fact to the _fact_cache
    hostname = 'test_host'
    variable_manager._fact_cache[hostname] = {'some': 'fact'}
    
    # Ensure the fact is in the cache before clearing
    assert hostname in variable_manager._fact_cache
    
    # Act: Clear the facts for the host
    variable_manager.clear_facts(hostname)
    
    # Assert: The fact should be removed from the cache
    assert hostname not in variable_manager._fact_cache
