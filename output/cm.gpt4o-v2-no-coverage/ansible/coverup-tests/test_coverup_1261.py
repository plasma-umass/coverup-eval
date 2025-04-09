# file: lib/ansible/module_utils/common/parameters.py:188-242
# asked: {"lines": [222, 223, 227, 233, 239], "branches": [[220, 225], [221, 222], [222, 221], [222, 223], [225, 227], [232, 233], [238, 239]]}
# gained: {"lines": [222, 223, 227, 233, 239], "branches": [[220, 225], [221, 222], [222, 223], [225, 227], [232, 233], [238, 239]]}

import pytest
from ansible.module_utils.common.parameters import _handle_aliases
from ansible.module_utils.common.collections import is_iterable
from ansible.module_utils.six import binary_type, text_type

def test_handle_aliases_no_aliases():
    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'int'}
    }
    parameters = {'param1': 'value1', 'param2': 2}
    result = _handle_aliases(argument_spec, parameters)
    assert result == {}

def test_handle_aliases_with_aliases():
    argument_spec = {
        'param1': {'type': 'str', 'aliases': ['alias1']},
        'param2': {'type': 'int', 'aliases': ['alias2']}
    }
    parameters = {'alias1': 'value1', 'alias2': 2}
    result = _handle_aliases(argument_spec, parameters)
    assert result == {'alias1': 'param1', 'alias2': 'param2'}
    assert parameters['param1'] == 'value1'
    assert parameters['param2'] == 2

def test_handle_aliases_with_warnings():
    argument_spec = {
        'param1': {'type': 'str', 'aliases': ['alias1']},
        'param2': {'type': 'int', 'aliases': ['alias2']}
    }
    parameters = {'alias1': 'value1', 'param1': 'value1_override', 'alias2': 2}
    alias_warnings = []
    result = _handle_aliases(argument_spec, parameters, alias_warnings=alias_warnings)
    assert result == {'alias1': 'param1', 'alias2': 'param2'}
    assert ('param1', 'alias1') in alias_warnings

def test_handle_aliases_with_deprecations():
    argument_spec = {
        'param1': {'type': 'str', 'deprecated_aliases': [{'name': 'old_alias1', 'version': '2.0'}]},
        'param2': {'type': 'int', 'deprecated_aliases': [{'name': 'old_alias2', 'version': '2.0'}]}
    }
    parameters = {'old_alias1': 'value1', 'old_alias2': 2}
    alias_deprecations = []
    result = _handle_aliases(argument_spec, parameters, alias_deprecations=alias_deprecations)
    assert alias_deprecations == [{'name': 'old_alias1', 'version': '2.0'}, {'name': 'old_alias2', 'version': '2.0'}]

def test_handle_aliases_required_and_default():
    argument_spec = {
        'param1': {'type': 'str', 'required': True, 'default': 'default_value'}
    }
    parameters = {}
    with pytest.raises(ValueError, match="internal error: required and default are mutually exclusive for param1"):
        _handle_aliases(argument_spec, parameters)

def test_handle_aliases_invalid_aliases_type():
    argument_spec = {
        'param1': {'type': 'str', 'aliases': 'not_a_list'}
    }
    parameters = {}
    with pytest.raises(TypeError, match="internal error: aliases must be a list or tuple"):
        _handle_aliases(argument_spec, parameters)
