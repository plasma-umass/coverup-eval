# file lib/ansible/module_utils/common/parameters.py:188-242
# lines [221, 222, 223, 227, 232, 233, 235, 236, 237, 238, 239, 240]
# branches ['220->221', '221->222', '221->225', '222->221', '222->223', '225->227', '229->232', '232->233', '232->235', '235->215', '235->236', '237->235', '237->238', '238->239', '238->240']

import pytest
from ansible.module_utils.common.parameters import _handle_aliases

def test_handle_aliases_deprecated_aliases():
    argument_spec = {
        'param1': {
            'type': 'str',
            'deprecated_aliases': [{'name': 'old_param1', 'version': '2.0'}]
        }
    }
    parameters = {'old_param1': 'value1'}
    alias_deprecations = []

    _handle_aliases(argument_spec, parameters, alias_deprecations=alias_deprecations)

    assert alias_deprecations == [{'name': 'old_param1', 'version': '2.0'}]

def test_handle_aliases_required_and_default():
    argument_spec = {
        'param1': {
            'type': 'str',
            'default': 'default_value',
            'required': True
        }
    }
    parameters = {}

    with pytest.raises(ValueError, match="internal error: required and default are mutually exclusive for param1"):
        _handle_aliases(argument_spec, parameters)

def test_handle_aliases_invalid_aliases_type():
    argument_spec = {
        'param1': {
            'type': 'str',
            'aliases': 'not_a_list_or_tuple'
        }
    }
    parameters = {}

    with pytest.raises(TypeError, match="internal error: aliases must be a list or tuple"):
        _handle_aliases(argument_spec, parameters)

def test_handle_aliases_alias_warnings():
    argument_spec = {
        'param1': {
            'type': 'str',
            'aliases': ['alias1']
        }
    }
    parameters = {'param1': 'value1', 'alias1': 'value2'}
    alias_warnings = []

    _handle_aliases(argument_spec, parameters, alias_warnings=alias_warnings)

    assert alias_warnings == [('param1', 'alias1')]
    assert parameters['param1'] == 'value2'
