# file: lib/ansible/plugins/lookup/sequence.py:245-269
# asked: {"lines": [256, 257], "branches": [[260, 248]]}
# gained: {"lines": [256, 257], "branches": [[260, 248]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_run_with_exception_handling(lookup_module, mocker):
    mocker.patch.object(lookup_module, 'reset')
    mocker.patch.object(lookup_module, 'parse_simple_args', side_effect=Exception("test exception"))
    mocker.patch.object(lookup_module, 'parse_kv_args')
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence')

    with pytest.raises(AnsibleError, match="unknown error parsing with_sequence arguments: 'term1'. Error was: test exception"):
        lookup_module.run(['term1'], {})

def test_run_with_stride_zero(lookup_module, mocker):
    mocker.patch.object(lookup_module, 'reset')
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=True)
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence')
    
    lookup_module.stride = 0
    result = lookup_module.run(['term1'], {})
    
    assert result == []
