# file lib/ansible/module_utils/common/parameters.py:150-154
# lines [150, 151, 152, 154]
# branches ['151->152', '151->154']

import pytest
from ansible.module_utils.common.parameters import _get_legal_inputs

# Assuming the existence of `_handle_aliases` function as it is not provided in the snippet.
# If `_handle_aliases` is not defined, you would need to mock it or define a stub for testing purposes.

def test_get_legal_inputs_with_aliases(mocker):
    # Mock the _handle_aliases function to return a specific alias dict
    mock_handle_aliases = mocker.patch(
        'ansible.module_utils.common.parameters._handle_aliases',
        return_value={'alias_name': 'original_name'}
    )
    
    argument_spec = {'param1': {}, 'param2': {}}
    parameters = {'param1': 'value1', 'alias_name': 'value2'}
    aliases = None  # This will cause the _handle_aliases to be called

    # Call the function under test
    legal_inputs = _get_legal_inputs(argument_spec, parameters, aliases)

    # Assertions to check if the returned list contains keys from both argument_spec and aliases
    assert 'param1' in legal_inputs
    assert 'param2' in legal_inputs
    assert 'alias_name' in legal_inputs
    assert len(legal_inputs) == 3  # Ensure no extra keys are present

    # Verify that _handle_aliases was called with the correct arguments
    mock_handle_aliases.assert_called_once_with(argument_spec, parameters)
