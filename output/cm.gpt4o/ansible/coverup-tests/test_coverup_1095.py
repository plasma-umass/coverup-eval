# file lib/ansible/plugins/lookup/together.py:44-67
# lines [44, 45, 52, 53, 54, 55, 56, 57, 59, 61, 63, 64, 65, 67]
# branches ['54->55', '54->57', '64->65', '64->67']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.together import LookupModule
from unittest.mock import patch

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_lookup_variables(lookup_module):
    terms = [['a', 'b'], ['c', 'd']]
    expected = [['a', 'b'], ['c', 'd']]
    with patch('ansible.plugins.lookup.together.listify_lookup_plugin_terms', side_effect=lambda x, templar, loader: x):
        result = lookup_module._lookup_variables(terms)
    assert result == expected

def test_run_empty_list(lookup_module):
    with pytest.raises(AnsibleError, match="with_together requires at least one element in each list"):
        lookup_module.run([])

def test_run_transpose(lookup_module):
    terms = [['a', 'b'], ['c', 'd']]
    expected = [['a', 'c'], ['b', 'd']]
    with patch('ansible.plugins.lookup.together.listify_lookup_plugin_terms', side_effect=lambda x, templar, loader: x):
        result = lookup_module.run(terms)
    assert result == expected

def test_run_fill_none(lookup_module):
    terms = [['a', 'b'], ['c']]
    expected = [['a', 'c'], ['b', None]]
    with patch('ansible.plugins.lookup.together.listify_lookup_plugin_terms', side_effect=lambda x, templar, loader: x):
        result = lookup_module.run(terms)
    assert result == expected
