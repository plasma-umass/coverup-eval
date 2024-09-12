# file: lib/ansible/plugins/lookup/sequence.py:245-269
# asked: {"lines": [256, 257, 264, 265, 266], "branches": [[260, 248]]}
# gained: {"lines": [256, 257, 264, 265, 266], "branches": []}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_run_with_exception_during_parsing(lookup_module, mocker):
    mocker.patch.object(lookup_module, 'parse_simple_args', side_effect=Exception('parsing error'))
    with pytest.raises(AnsibleError, match="unknown error parsing with_sequence arguments: 'invalid_term'. Error was: parsing error"):
        lookup_module.run(['invalid_term'], {})

def test_run_with_exception_during_generation(lookup_module, mocker):
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=True)
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence', side_effect=Exception('generation error'))
    with pytest.raises(AnsibleError, match="unknown error generating sequence: generation error"):
        lookup_module.run(['valid_term'], {})

def test_run_with_stride_zero(lookup_module, mocker):
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=True)
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence', return_value=[])
    lookup_module.stride = 0
    result = lookup_module.run(['valid_term'], {})
    assert result == []

def test_run_with_valid_term(lookup_module, mocker):
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=True)
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence', return_value=['1', '2', '3'])
    result = lookup_module.run(['valid_term'], {})
    assert result == ['1', '2', '3']
