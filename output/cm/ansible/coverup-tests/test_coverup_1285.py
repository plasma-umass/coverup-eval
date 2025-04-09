# file lib/ansible/vars/manager.py:684-695
# lines [689, 690, 692, 693, 694, 695]
# branches ['689->690', '689->692']

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.vars.manager import VariableManager
from collections.abc import Mapping

@pytest.fixture
def variable_manager():
    return VariableManager()

def test_set_nonpersistent_facts_with_non_mapping(variable_manager):
    with pytest.raises(AnsibleAssertionError):
        variable_manager.set_nonpersistent_facts('localhost', facts='not_a_mapping')

def test_set_nonpersistent_facts_with_mapping(variable_manager, mocker):
    mocker.patch.object(variable_manager, '_nonpersistent_fact_cache', {})
    facts = {'key': 'value'}
    variable_manager.set_nonpersistent_facts('localhost', facts)
    assert 'localhost' in variable_manager._nonpersistent_fact_cache
    assert variable_manager._nonpersistent_fact_cache['localhost'] == facts

def test_update_nonpersistent_facts_with_mapping(variable_manager, mocker):
    mocker.patch.object(variable_manager, '_nonpersistent_fact_cache', {'localhost': {'initial': 'fact'}})
    facts = {'key': 'value'}
    variable_manager.set_nonpersistent_facts('localhost', facts)
    assert 'localhost' in variable_manager._nonpersistent_fact_cache
    assert variable_manager._nonpersistent_fact_cache['localhost'] == {'initial': 'fact', 'key': 'value'}
