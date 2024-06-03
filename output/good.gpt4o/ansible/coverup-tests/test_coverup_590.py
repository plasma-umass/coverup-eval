# file lib/ansible/module_utils/common/parameters.py:150-154
# lines [150, 151, 152, 154]
# branches ['151->152', '151->154']

import pytest
from unittest import mock
from ansible.module_utils.common.parameters import _get_legal_inputs

def test_get_legal_inputs_with_aliases(mocker):
    argument_spec = {'arg1': {}, 'arg2': {}}
    parameters = {'param1': 'value1'}
    aliases = {'alias1': 'arg1', 'alias2': 'arg2'}

    mock_handle_aliases = mocker.patch('ansible.module_utils.common.parameters._handle_aliases', return_value=aliases)

    result = _get_legal_inputs(argument_spec, parameters)
    
    mock_handle_aliases.assert_called_once_with(argument_spec, parameters)
    assert set(result) == set(['alias1', 'alias2', 'arg1', 'arg2'])

def test_get_legal_inputs_without_aliases(mocker):
    argument_spec = {'arg1': {}, 'arg2': {}}
    parameters = {'param1': 'value1'}

    mock_handle_aliases = mocker.patch('ansible.module_utils.common.parameters._handle_aliases', return_value={})

    result = _get_legal_inputs(argument_spec, parameters)
    
    mock_handle_aliases.assert_called_once_with(argument_spec, parameters)
    assert set(result) == set(['arg1', 'arg2'])
