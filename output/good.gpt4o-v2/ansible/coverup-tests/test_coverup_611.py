# file: lib/ansible/module_utils/common/parameters.py:150-154
# asked: {"lines": [150, 151, 152, 154], "branches": [[151, 152], [151, 154]]}
# gained: {"lines": [150, 151, 152, 154], "branches": [[151, 152], [151, 154]]}

import pytest
from ansible.module_utils.common.parameters import _get_legal_inputs

def test_get_legal_inputs_with_aliases(monkeypatch):
    argument_spec = {'arg1': 'value1', 'arg2': 'value2'}
    parameters = {'param1': 'value1'}
    aliases = {'alias1': 'arg1', 'alias2': 'arg2'}

    result = _get_legal_inputs(argument_spec, parameters, aliases)
    assert result == ['alias1', 'alias2', 'arg1', 'arg2']

def test_get_legal_inputs_without_aliases(monkeypatch):
    argument_spec = {'arg1': 'value1', 'arg2': 'value2'}
    parameters = {'param1': 'value1'}

    def mock_handle_aliases(arg_spec, params):
        return {'alias1': 'arg1', 'alias2': 'arg2'}

    monkeypatch.setattr('ansible.module_utils.common.parameters._handle_aliases', mock_handle_aliases)

    result = _get_legal_inputs(argument_spec, parameters)
    assert result == ['alias1', 'alias2', 'arg1', 'arg2']
