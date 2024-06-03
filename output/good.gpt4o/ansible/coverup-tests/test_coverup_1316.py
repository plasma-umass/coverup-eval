# file lib/ansible/plugins/lookup/sequence.py:245-269
# lines [255]
# branches []

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_run_with_ansible_error(lookup_module, mocker):
    mocker.patch.object(lookup_module, 'reset')
    mocker.patch.object(lookup_module, 'parse_simple_args', side_effect=AnsibleError)
    mocker.patch.object(lookup_module, 'parse_kv_args')
    mocker.patch.object(lookup_module, 'sanity_check')
    mocker.patch.object(lookup_module, 'generate_sequence')

    terms = ['invalid_term']
    with pytest.raises(AnsibleError):
        lookup_module.run(terms, {})

    lookup_module.reset.assert_called_once()
    lookup_module.parse_simple_args.assert_called_once_with('invalid_term')
    lookup_module.parse_kv_args.assert_not_called()
    lookup_module.sanity_check.assert_not_called()
    lookup_module.generate_sequence.assert_not_called()
