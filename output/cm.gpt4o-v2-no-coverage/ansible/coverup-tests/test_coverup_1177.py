# file: lib/ansible/plugins/lookup/sequence.py:245-269
# asked: {"lines": [256, 257, 264, 265, 266], "branches": [[260, 248]]}
# gained: {"lines": [256, 257, 264, 265, 266], "branches": []}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    module = LookupModule()
    module.reset()
    return module

def test_run_with_valid_simple_args(mocker, lookup_module):
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=True)
    mocker.patch.object(lookup_module, 'generate_sequence', return_value=['1', '2', '3'])
    mocker.patch.object(lookup_module, 'reset')
    mocker.patch.object(lookup_module, 'sanity_check')

    terms = ['1-3']
    variables = {}
    result = lookup_module.run(terms, variables)
    
    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('1-3')
    lookup_module.sanity_check.assert_called_once()
    lookup_module.generate_sequence.assert_called_once()
    assert result == ['1', '2', '3']

def test_run_with_invalid_simple_args(mocker, lookup_module):
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=False)
    mocker.patch.object(lookup_module, 'parse_kv_args')
    mocker.patch.object(lookup_module, 'generate_sequence', return_value=['1', '2', '3'])
    mocker.patch.object(lookup_module, 'reset')
    mocker.patch.object(lookup_module, 'sanity_check')

    terms = ['start=1 end=3']
    variables = {}
    result = lookup_module.run(terms, variables)
    
    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('start=1 end=3')
    lookup_module.parse_kv_args.assert_called_once()
    lookup_module.sanity_check.assert_called_once()
    lookup_module.generate_sequence.assert_called_once()
    assert result == ['1', '2', '3']

def test_run_with_parse_error(mocker, lookup_module):
    mocker.patch.object(lookup_module, 'parse_simple_args', side_effect=AnsibleError)
    mocker.patch.object(lookup_module, 'reset')

    terms = ['invalid']
    variables = {}
    with pytest.raises(AnsibleError):
        lookup_module.run(terms, variables)
    
    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('invalid')

def test_run_with_unknown_parse_error(mocker, lookup_module):
    mocker.patch.object(lookup_module, 'parse_simple_args', side_effect=Exception('unknown error'))
    mocker.patch.object(lookup_module, 'reset')

    terms = ['invalid']
    variables = {}
    with pytest.raises(AnsibleError, match="unknown error parsing with_sequence arguments: 'invalid'. Error was: unknown error"):
        lookup_module.run(terms, variables)
    
    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('invalid')

def test_run_with_sanity_check_error(mocker, lookup_module):
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=True)
    mocker.patch.object(lookup_module, 'sanity_check', side_effect=AnsibleError)
    mocker.patch.object(lookup_module, 'reset')

    terms = ['1-3']
    variables = {}
    with pytest.raises(AnsibleError):
        lookup_module.run(terms, variables)
    
    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('1-3')
    lookup_module.sanity_check.assert_called_once()

def test_run_with_generate_sequence_error(mocker, lookup_module):
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=True)
    mocker.patch.object(lookup_module, 'generate_sequence', side_effect=Exception('generate error'))
    mocker.patch.object(lookup_module, 'reset')
    mocker.patch.object(lookup_module, 'sanity_check')

    terms = ['1-3']
    variables = {}
    with pytest.raises(AnsibleError, match="unknown error generating sequence: generate error"):
        lookup_module.run(terms, variables)
    
    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('1-3')
    lookup_module.sanity_check.assert_called_once()
    lookup_module.generate_sequence.assert_called_once()
