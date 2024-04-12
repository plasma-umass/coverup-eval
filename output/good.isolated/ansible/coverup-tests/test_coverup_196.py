# file lib/ansible/module_utils/common/parameters.py:157-185
# lines [157, 173, 174, 176, 177, 178, 179, 180, 181, 183, 185]
# branches ['173->174', '173->176', '177->178', '177->185', '178->177', '178->179', '180->181', '180->183']

import pytest
from ansible.module_utils.common.parameters import _get_unsupported_parameters

def test_get_unsupported_parameters_with_options_context(mocker):
    argument_spec = {'name': {'type': 'str'}, 'state': {'type': 'str'}}
    parameters = {'name': 'test', 'state': 'present', 'invalid_param': 'value'}
    options_context = ['parent_key']

    # Mocking _get_legal_inputs to return only the keys from argument_spec
    mocker.patch(
        'ansible.module_utils.common.parameters._get_legal_inputs',
        return_value=set(argument_spec.keys())
    )

    unsupported_parameters = _get_unsupported_parameters(
        argument_spec, parameters, options_context=options_context
    )

    # Assert that the unsupported parameter is identified within the correct context
    assert unsupported_parameters == {('parent_key', 'invalid_param')}

    # Cleanup is not necessary as we are using mocker.patch which is automatically
    # undone at the end of the test
