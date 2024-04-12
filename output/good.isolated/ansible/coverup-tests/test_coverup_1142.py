# file lib/ansible/module_utils/common/parameters.py:188-242
# lines [213, 215, 216, 217, 218, 220, 221, 222, 223, 225, 227, 229, 230, 232, 233, 235, 236, 237, 238, 239, 240, 242]
# branches ['215->216', '215->242', '220->221', '220->225', '221->222', '221->225', '222->221', '222->223', '225->227', '225->229', '229->230', '229->232', '232->233', '232->235', '235->215', '235->236', '237->235', '237->238', '238->239', '238->240']

import pytest

from ansible.module_utils.common.parameters import _handle_aliases

def test_handle_aliases_with_deprecations_and_warnings():
    argument_spec = {
        'size': {
            'type': 'int',
            'aliases': ['length', 'quantity'],
            'deprecated_aliases': [{'name': 'amt', 'version': '2.10', 'date': '2020-04-01'}]
        }
    }
    parameters = {
        'length': 10,
        'amt': 5,
        'size': 10  # Adding 'size' to trigger the warning for having both an option and its alias
    }
    alias_warnings = []
    alias_deprecations = []

    expected_aliases_results = {'length': 'size', 'quantity': 'size'}
    expected_parameters = {'size': 10, 'length': 10, 'amt': 5}
    expected_alias_warnings = [('size', 'length')]
    expected_alias_deprecations = [{'name': 'amt', 'version': '2.10', 'date': '2020-04-01'}]

    aliases_results = _handle_aliases(argument_spec, parameters, alias_warnings, alias_deprecations)

    assert aliases_results == expected_aliases_results
    assert parameters == expected_parameters
    assert alias_warnings == expected_alias_warnings
    assert alias_deprecations == expected_alias_deprecations
