# file: lib/ansible/module_utils/common/parameters.py:150-154
# asked: {"lines": [150, 151, 152, 154], "branches": [[151, 152], [151, 154]]}
# gained: {"lines": [150, 151, 152, 154], "branches": [[151, 152], [151, 154]]}

import pytest
from ansible.module_utils.common.parameters import _get_legal_inputs
from ansible.module_utils.common.parameters import _handle_aliases

def test_get_legal_inputs_with_aliases():
    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'int'}
    }
    parameters = {
        'param1': 'value1',
        'param2': 2
    }
    aliases = {
        'alias1': 'param1',
        'alias2': 'param2'
    }
    
    result = _get_legal_inputs(argument_spec, parameters, aliases)
    assert result == ['alias1', 'alias2', 'param1', 'param2']

def test_get_legal_inputs_without_aliases(monkeypatch):
    argument_spec = {
        'param1': {'type': 'str', 'aliases': ['alias1']},
        'param2': {'type': 'int', 'aliases': ['alias2']}
    }
    parameters = {
        'param1': 'value1',
        'param2': 2
    }
    
    def mock_handle_aliases(argument_spec, parameters):
        return {
            'alias1': 'param1',
            'alias2': 'param2'
        }
    
    monkeypatch.setattr('ansible.module_utils.common.parameters._handle_aliases', mock_handle_aliases)
    
    result = _get_legal_inputs(argument_spec, parameters)
    assert result == ['alias1', 'alias2', 'param1', 'param2']
