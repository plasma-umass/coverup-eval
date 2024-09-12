# file: lib/ansible/module_utils/common/parameters.py:188-242
# asked: {"lines": [221, 222, 223, 227, 232, 233, 235, 236, 237, 238, 239, 240], "branches": [[220, 221], [221, 222], [221, 225], [222, 221], [222, 223], [225, 227], [229, 232], [232, 233], [232, 235], [235, 215], [235, 236], [237, 235], [237, 238], [238, 239], [238, 240]]}
# gained: {"lines": [221, 222, 223, 227, 232, 233, 235, 236, 237, 238, 239, 240], "branches": [[220, 221], [221, 222], [221, 225], [222, 223], [225, 227], [229, 232], [232, 233], [232, 235], [235, 215], [235, 236], [237, 235], [237, 238], [238, 239]]}

import pytest
from ansible.module_utils.common.parameters import _handle_aliases
from ansible.module_utils.common.collections import is_iterable
from ansible.module_utils.six import binary_type, text_type

def test_handle_aliases_with_deprecated_aliases():
    argument_spec = {
        'param1': {
            'deprecated_aliases': [{'name': 'old_param1'}],
            'aliases': ['alias1'],
        }
    }
    parameters = {'old_param1': 'value1'}
    alias_deprecations = []

    _handle_aliases(argument_spec, parameters, alias_deprecations=alias_deprecations)

    assert alias_deprecations == [{'name': 'old_param1'}]

def test_handle_aliases_required_and_default():
    argument_spec = {
        'param1': {
            'default': 'default_value',
            'required': True,
        }
    }
    parameters = {}

    with pytest.raises(ValueError, match="internal error: required and default are mutually exclusive for param1"):
        _handle_aliases(argument_spec, parameters)

def test_handle_aliases_non_iterable_aliases():
    argument_spec = {
        'param1': {
            'aliases': 'not_a_list_or_tuple',
        }
    }
    parameters = {}

    with pytest.raises(TypeError, match="internal error: aliases must be a list or tuple"):
        _handle_aliases(argument_spec, parameters)

def test_handle_aliases_with_alias_warnings():
    argument_spec = {
        'param1': {
            'aliases': ['alias1'],
        }
    }
    parameters = {'alias1': 'value1', 'param1': 'value2'}
    alias_warnings = []

    _handle_aliases(argument_spec, parameters, alias_warnings=alias_warnings)

    assert alias_warnings == [('param1', 'alias1')]
    assert parameters['param1'] == 'value1'
