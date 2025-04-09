# file: lib/ansible/plugins/lookup/sequence.py:245-269
# asked: {"lines": [255], "branches": [[252, 259]]}
# gained: {"lines": [255], "branches": [[252, 259]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    module = LookupModule()
    module.stride = 1  # Set default value for stride to avoid AttributeError
    return module

def test_parse_simple_args_false(mocker, lookup_module):
    mocker.patch.object(lookup_module, 'reset')
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=False)
    mocker.patch.object(lookup_module, 'parse_kv_args')
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence', return_value=[1, 2, 3])
    
    terms = ['a=1 b=2 c=3']
    result = lookup_module.run(terms, {})
    
    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('a=1 b=2 c=3')
    lookup_module.parse_kv_args.assert_called_once()
    lookup_module.sanity_check.assert_called_once()
    assert result == [1, 2, 3]

def test_ansible_error_in_parse_kv_args(mocker, lookup_module):
    mocker.patch.object(lookup_module, 'reset')
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=False)
    mocker.patch.object(lookup_module, 'parse_kv_args', side_effect=AnsibleError)
    
    terms = ['a=1 b=2 c=3']
    
    with pytest.raises(AnsibleError):
        lookup_module.run(terms, {})
    
    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('a=1 b=2 c=3')
    lookup_module.parse_kv_args.assert_called_once()

def test_sanity_check_called(mocker, lookup_module):
    mocker.patch.object(lookup_module, 'reset')
    mocker.patch.object(lookup_module, 'parse_simple_args', return_value=True)
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence', return_value=[1, 2, 3])
    
    terms = ['a=1 b=2 c=3']
    result = lookup_module.run(terms, {})
    
    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('a=1 b=2 c=3')
    lookup_module.sanity_check.assert_called_once()
    assert result == [1, 2, 3]
