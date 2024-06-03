# file lib/ansible/plugins/lookup/sequence.py:245-269
# lines [245, 246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 259, 260, 261, 262, 263, 264, 265, 266, 269]
# branches ['248->249', '248->269', '252->253', '252->259', '260->248', '260->261']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_run_with_invalid_term(lookup_module, mocker):
    terms = ["invalid_term"]
    variables = {}

    mocker.patch.object(lookup_module, 'reset')
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=False)
    mocker.patch.object(lookup_module, 'parse_kv_args', side_effect=Exception("parse_kv_args error"))
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence')

    with pytest.raises(AnsibleError, match="unknown error parsing with_sequence arguments: 'invalid_term'. Error was: parse_kv_args error"):
        lookup_module.run(terms, variables)

def test_run_with_stride_zero(lookup_module, mocker):
    terms = ["valid_term"]
    variables = {}

    mocker.patch.object(lookup_module, 'reset')
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=True)
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence')
    
    # Mocking the stride attribute directly on the instance
    lookup_module.stride = 0

    result = lookup_module.run(terms, variables)
    assert result == []

def test_run_with_generate_sequence_error(lookup_module, mocker):
    terms = ["valid_term"]
    variables = {}

    mocker.patch.object(lookup_module, 'reset')
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=True)
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence', side_effect=Exception("generate_sequence error"))
    
    # Mocking the stride attribute directly on the instance
    lookup_module.stride = 1

    with pytest.raises(AnsibleError, match="unknown error generating sequence: generate_sequence error"):
        lookup_module.run(terms, variables)
