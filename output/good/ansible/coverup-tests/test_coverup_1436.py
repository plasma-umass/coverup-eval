# file lib/ansible/plugins/lookup/random_choice.py:42-53
# lines [53]
# branches ['47->53']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup import random_choice

# Test function to cover line 53 when terms is not empty
def test_random_choice_with_terms():
    lookup = random_choice.LookupModule()
    terms = ['apple', 'banana', 'cherry']
    result = lookup.run(terms)
    assert len(result) == 1
    assert result[0] in terms

# Test function to cover line 53 when terms is empty
def test_random_choice_with_empty_terms():
    lookup = random_choice.LookupModule()
    terms = []
    result = lookup.run(terms)
    assert result == terms
