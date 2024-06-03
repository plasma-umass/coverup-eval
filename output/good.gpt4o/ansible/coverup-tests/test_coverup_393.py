# file lib/ansible/plugins/lookup/random_choice.py:42-53
# lines [42, 44, 46, 47, 48, 49, 50, 51, 53]
# branches ['47->48', '47->53']

import pytest
from ansible.plugins.lookup.random_choice import LookupModule
from ansible.errors import AnsibleError

def test_lookup_module_run(mocker):
    lookup = LookupModule()

    # Test with empty terms
    terms = []
    result = lookup.run(terms)
    assert result == terms

    # Test with non-empty terms
    terms = ['a', 'b', 'c']
    result = lookup.run(terms)
    assert result[0] in terms

    # Test exception handling
    mocker.patch('random.choice', side_effect=Exception('Test exception'))
    with pytest.raises(AnsibleError, match="Unable to choose random term: Test exception"):
        lookup.run(terms)
