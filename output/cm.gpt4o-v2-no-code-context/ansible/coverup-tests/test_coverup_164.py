# file: lib/ansible/plugins/lookup/together.py:44-67
# asked: {"lines": [44, 45, 52, 53, 54, 55, 56, 57, 59, 61, 63, 64, 65, 67], "branches": [[54, 55], [54, 57], [64, 65], [64, 67]]}
# gained: {"lines": [44, 45, 52, 53, 54, 55, 56, 57, 59, 61, 63, 64, 65, 67], "branches": [[54, 55], [54, 57], [64, 65], [64, 67]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.together import LookupModule
from ansible.plugins.lookup import LookupBase
from ansible.utils.listify import listify_lookup_plugin_terms
from unittest.mock import patch

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_lookup_variables(lookup_module):
    terms = [['a', 'b'], ['c', 'd']]
    with patch('ansible.plugins.lookup.together.listify_lookup_plugin_terms', side_effect=lambda x, **kwargs: x):
        result = lookup_module._lookup_variables(terms)
    assert result == terms

def test_run_empty_terms(lookup_module):
    terms = []
    with pytest.raises(AnsibleError, match="with_together requires at least one element in each list"):
        lookup_module.run(terms)

def test_run_non_empty_terms(lookup_module):
    terms = [['a', 'b'], ['c', 'd']]
    with patch('ansible.plugins.lookup.together.listify_lookup_plugin_terms', side_effect=lambda x, **kwargs: x):
        result = lookup_module.run(terms)
    assert result == [['a', 'c'], ['b', 'd']]

def test_run_with_none_fill(lookup_module):
    terms = [['a', 'b'], ['c']]
    with patch('ansible.plugins.lookup.together.listify_lookup_plugin_terms', side_effect=lambda x, **kwargs: x):
        result = lookup_module.run(terms)
    assert result == [['a', 'c'], ['b', None]]
