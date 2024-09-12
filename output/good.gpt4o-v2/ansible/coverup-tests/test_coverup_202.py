# file: lib/ansible/plugins/lookup/together.py:44-67
# asked: {"lines": [44, 45, 52, 53, 54, 55, 56, 57, 59, 61, 63, 64, 65, 67], "branches": [[54, 55], [54, 57], [64, 65], [64, 67]]}
# gained: {"lines": [44, 45, 52, 53, 54, 55, 56, 57, 59, 61, 63, 64, 65, 67], "branches": [[54, 55], [54, 57], [64, 65], [64, 67]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.together import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_lookup_variables(lookup_module, mocker):
    mocker.patch('ansible.plugins.lookup.together.listify_lookup_plugin_terms', side_effect=lambda x, templar, loader: x)
    terms = [['a', 'b'], ['c', 'd']]
    result = lookup_module._lookup_variables(terms)
    assert result == [['a', 'b'], ['c', 'd']]

def test_run_with_empty_list(lookup_module, mocker):
    mocker.patch.object(lookup_module, '_lookup_variables', return_value=[])
    with pytest.raises(AnsibleError, match="with_together requires at least one element in each list"):
        lookup_module.run([])

def test_run_with_non_empty_list(lookup_module, mocker):
    mocker.patch.object(lookup_module, '_lookup_variables', return_value=[['a', 'b'], ['c', 'd']])
    mocker.patch.object(lookup_module, '_flatten', side_effect=lambda x: x)
    result = lookup_module.run([['a', 'b'], ['c', 'd']])
    assert result == [('a', 'c'), ('b', 'd')]
