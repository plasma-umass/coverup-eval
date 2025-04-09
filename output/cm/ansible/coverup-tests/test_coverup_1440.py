# file lib/ansible/module_utils/common/parameters.py:150-154
# lines []
# branches ['151->154']

import pytest
from ansible.module_utils.common.parameters import _get_legal_inputs

# Assuming the existence of _handle_aliases function in the same module
# If not, a mock or a dummy function should be provided

def test_get_legal_inputs_with_aliases_provided():
    argument_spec = {'arg_key': 'arg_value'}
    parameters = {'param_key': 'param_value'}
    aliases = {'alias_key': 'alias_value'}
    
    # Call the function with aliases provided
    result = _get_legal_inputs(argument_spec, parameters, aliases=aliases)
    
    # Assert that the result includes keys from both the aliases and argument_spec
    assert 'alias_key' in result
    assert 'arg_key' in result
    assert len(result) == 2  # Ensure no other keys are included
