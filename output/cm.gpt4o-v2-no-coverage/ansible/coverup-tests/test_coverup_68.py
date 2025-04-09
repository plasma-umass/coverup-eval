# file: lib/ansible/plugins/lookup/nested.py:57-85
# asked: {"lines": [57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], "branches": [[61, 62], [61, 67], [76, 77], [76, 78], [79, 80], [79, 82], [83, 84], [83, 85]]}
# gained: {"lines": [57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], "branches": [[61, 62], [61, 67], [76, 77], [76, 78], [79, 80], [79, 82], [83, 84], [83, 85]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError, AnsibleUndefinedVariable
from ansible.plugins.lookup import LookupBase
from ansible.plugins.lookup.nested import LookupModule
from jinja2.exceptions import UndefinedError

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_lookup_variables_success(lookup_module):
    terms = ['term1', 'term2']
    variables = {'var1': 'value1'}
    
    with patch('ansible.plugins.lookup.nested.listify_lookup_plugin_terms', side_effect=lambda x, **kwargs: [x]):
        result = lookup_module._lookup_variables(terms, variables)
    
    assert result == [['term1'], ['term2']]

def test_lookup_variables_undefined_error(lookup_module):
    terms = ['term1', 'term2']
    variables = {'var1': 'value1'}
    
    with patch('ansible.plugins.lookup.nested.listify_lookup_plugin_terms', side_effect=UndefinedError):
        with pytest.raises(AnsibleUndefinedVariable, match="One of the nested variables was undefined. The error was: "):
            lookup_module._lookup_variables(terms, variables)

def test_run_success(lookup_module):
    terms = [['a', 'b'], ['c', 'd']]
    variables = {'var1': 'value1'}
    
    with patch.object(LookupModule, '_lookup_variables', return_value=terms), \
         patch.object(LookupModule, '_combine', side_effect=lambda x, y: [(i, j) for i in x for j in y]), \
         patch.object(LookupModule, '_flatten', side_effect=lambda x: x):
        
        result = lookup_module.run(terms, variables)
    
    assert result == [('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd')]

def test_run_empty_terms(lookup_module):
    terms = []
    variables = {'var1': 'value1'}
    
    with patch.object(LookupModule, '_lookup_variables', return_value=terms):
        with pytest.raises(AnsibleError, match="with_nested requires at least one element in the nested list"):
            lookup_module.run(terms, variables)
