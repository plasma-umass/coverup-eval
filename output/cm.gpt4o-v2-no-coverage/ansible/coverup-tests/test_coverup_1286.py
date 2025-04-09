# file: lib/ansible/module_utils/common/parameters.py:157-185
# asked: {"lines": [174, 181], "branches": [[173, 174], [180, 181]]}
# gained: {"lines": [174, 181], "branches": [[173, 174], [180, 181]]}

import pytest
from ansible.module_utils.common.parameters import _get_unsupported_parameters

def test_get_unsupported_parameters_no_legal_inputs():
    argument_spec = {'param1': {'type': 'str'}, 'param2': {'type': 'int'}}
    parameters = {'param1': 'value1', 'param3': 'value3'}
    expected_unsupported = {'param3'}
    
    result = _get_unsupported_parameters(argument_spec, parameters)
    
    assert result == expected_unsupported

def test_get_unsupported_parameters_with_legal_inputs():
    argument_spec = {'param1': {'type': 'str'}, 'param2': {'type': 'int'}}
    parameters = {'param1': 'value1', 'param3': 'value3'}
    legal_inputs = ['param1', 'param2']
    expected_unsupported = {'param3'}
    
    result = _get_unsupported_parameters(argument_spec, parameters, legal_inputs)
    
    assert result == expected_unsupported

def test_get_unsupported_parameters_with_options_context():
    argument_spec = {'param1': {'type': 'str'}, 'param2': {'type': 'int'}}
    parameters = {'param1': 'value1', 'param3': 'value3'}
    options_context = ['parent']
    expected_unsupported = {('parent', 'param3')}
    
    result = _get_unsupported_parameters(argument_spec, parameters, options_context=options_context)
    
    assert result == expected_unsupported

def test_get_unsupported_parameters_all_supported():
    argument_spec = {'param1': {'type': 'str'}, 'param2': {'type': 'int'}}
    parameters = {'param1': 'value1', 'param2': 'value2'}
    expected_unsupported = set()
    
    result = _get_unsupported_parameters(argument_spec, parameters)
    
    assert result == expected_unsupported
