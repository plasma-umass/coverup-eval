# file lib/ansible/playbook/play_context.py:321-337
# lines []
# branches ['334->333']

import pytest
from ansible.playbook.play_context import PlayContext
from ansible import constants as C

# Mocking the MAGIC_VARIABLE_MAPPING to control the test scenario
C.MAGIC_VARIABLE_MAPPING = {
    'test_prop': ['test_var']
}

@pytest.fixture
def play_context():
    pc = PlayContext()
    pc.test_prop = 'test_value'
    return pc

def test_update_vars_with_missing_branch(play_context):
    variables = {}
    play_context.update_vars(variables)
    assert 'test_var' in variables
    assert variables['test_var'] == 'test_value'

    # Now test the branch where 'test_var' is already in variables
    variables = {'test_var': 'existing_value'}
    play_context.update_vars(variables)
    # The value should not be updated because it already exists
    assert variables['test_var'] == 'existing_value'
