# file: lib/ansible/plugins/lookup/sequence.py:245-269
# asked: {"lines": [245, 246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 259, 260, 261, 262, 263, 264, 265, 266, 269], "branches": [[248, 249], [248, 269], [252, 253], [252, 259], [260, 248], [260, 261]]}
# gained: {"lines": [245, 246, 248, 249, 250, 251, 252, 253, 254, 255, 259, 260, 261, 262, 263, 269], "branches": [[248, 249], [248, 269], [252, 253], [252, 259], [260, 261]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    module = LookupModule()
    module.reset()
    return module

def test_run_with_valid_simple_args(mocker, lookup_module):
    mocker.patch.object(lookup_module, 'reset', wraps=lookup_module.reset)
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=True)
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence', return_value=iter(['1', '2', '3']))

    terms = ['1-3']
    variables = {}
    result = lookup_module.run(terms, variables)

    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('1-3')
    lookup_module.sanity_check.assert_called_once()
    lookup_module.generate_sequence.assert_called_once()
    assert result == ['1', '2', '3']

def test_run_with_invalid_simple_args(mocker, lookup_module):
    mocker.patch.object(lookup_module, 'reset', wraps=lookup_module.reset)
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=False)
    mocker.patch.object(lookup_module, 'parse_kv_args')
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence', return_value=iter(['1', '2', '3']))

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
    mocker.patch.object(lookup_module, 'reset', wraps=lookup_module.reset)
    mocker.patch.object(lookup_module, 'parse_simple_args', side_effect=AnsibleError('parse error'))
    mocker.patch.object(lookup_module, 'parse_kv_args')
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence')

    terms = ['invalid']
    variables = {}

    with pytest.raises(AnsibleError, match='parse error'):
        lookup_module.run(terms, variables)

    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('invalid')
    lookup_module.parse_kv_args.assert_not_called()
    lookup_module.sanity_check.assert_not_called()
    lookup_module.generate_sequence.assert_not_called()

def test_run_with_generation_error(mocker, lookup_module):
    mocker.patch.object(lookup_module, 'reset', wraps=lookup_module.reset)
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=True)
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence', side_effect=AnsibleError('generation error'))

    terms = ['1-3']
    variables = {}

    with pytest.raises(AnsibleError, match='generation error'):
        lookup_module.run(terms, variables)

    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('1-3')
    lookup_module.sanity_check.assert_called_once()
    lookup_module.generate_sequence.assert_called_once()
