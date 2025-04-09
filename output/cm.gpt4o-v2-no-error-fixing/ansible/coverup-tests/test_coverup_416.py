# file: lib/ansible/module_utils/common/parameters.py:150-154
# asked: {"lines": [150, 151, 152, 154], "branches": [[151, 152], [151, 154]]}
# gained: {"lines": [150, 151, 152, 154], "branches": [[151, 152], [151, 154]]}

import pytest
from ansible.module_utils.common.parameters import _get_legal_inputs

def test_get_legal_inputs_with_aliases(mocker):
    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'int', 'aliases': ['alias2']}
    }
    parameters = {'alias2': 42}
    aliases = {'alias2': 'param2'}

    mock_handle_aliases = mocker.patch('ansible.module_utils.common.parameters._handle_aliases', return_value=aliases)

    result = _get_legal_inputs(argument_spec, parameters, aliases)
    assert result == ['alias2', 'param1', 'param2']
    mock_handle_aliases.assert_not_called()

def test_get_legal_inputs_without_aliases(mocker):
    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'int', 'aliases': ['alias2']}
    }
    parameters = {'alias2': 42}

    mock_handle_aliases = mocker.patch('ansible.module_utils.common.parameters._handle_aliases', return_value={'alias2': 'param2'})

    result = _get_legal_inputs(argument_spec, parameters)
    assert result == ['alias2', 'param1', 'param2']
    mock_handle_aliases.assert_called_once_with(argument_spec, parameters)
