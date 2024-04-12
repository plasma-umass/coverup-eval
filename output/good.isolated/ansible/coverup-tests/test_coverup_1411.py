# file lib/ansible/module_utils/common/parameters.py:157-185
# lines []
# branches ['173->176', '180->183']

import pytest
from ansible.module_utils.common.parameters import _get_unsupported_parameters

def test_get_unsupported_parameters_with_and_without_options_context():
    argument_spec = {'name': {'type': 'str'}, 'state': {'type': 'str'}}
    parameters_with_unsupported = {'name': 'test', 'invalid_param': 'value'}
    parameters_without_unsupported = {'name': 'test', 'state': 'present'}
    options_context = ['parent']

    # Test with options_context and unsupported parameter
    unsupported_parameters_with_context = _get_unsupported_parameters(
        argument_spec, parameters_with_unsupported, options_context=options_context
    )

    # Test without options_context and with unsupported parameter
    unsupported_parameters_without_context = _get_unsupported_parameters(
        argument_spec, parameters_with_unsupported, options_context=None
    )

    # Test without options_context and without unsupported parameter
    unsupported_parameters_no_unsupported = _get_unsupported_parameters(
        argument_spec, parameters_without_unsupported, options_context=None
    )

    # Assertions to check if the unsupported parameter is detected within the context
    assert unsupported_parameters_with_context == {('parent', 'invalid_param')}

    # Assertions to check if the unsupported parameter is detected without context
    assert unsupported_parameters_without_context == {'invalid_param'}

    # Assertions to check if no unsupported parameters are found when there are none
    assert not unsupported_parameters_no_unsupported
