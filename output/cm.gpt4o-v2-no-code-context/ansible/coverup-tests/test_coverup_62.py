# file: lib/ansible/plugins/lookup/nested.py:57-85
# asked: {"lines": [57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], "branches": [[61, 62], [61, 67], [76, 77], [76, 78], [79, 80], [79, 82], [83, 84], [83, 85]]}
# gained: {"lines": [57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], "branches": [[61, 62], [61, 67], [76, 77], [76, 78], [79, 80], [79, 82], [83, 84], [83, 85]]}

import pytest
from ansible.errors import AnsibleError, AnsibleUndefinedVariable
from ansible.plugins.lookup.nested import LookupModule
from ansible.utils.listify import listify_lookup_plugin_terms
from jinja2 import UndefinedError

class MockTemplar:
    pass

class MockLoader:
    pass

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_lookup_variables_success(lookup_module, monkeypatch):
    terms = ['term1', 'term2']
    variables = {}

    def mock_listify_lookup_plugin_terms(x, templar, loader, fail_on_undefined):
        return [x]

    monkeypatch.setattr('ansible.plugins.lookup.nested.listify_lookup_plugin_terms', mock_listify_lookup_plugin_terms)
    result = lookup_module._lookup_variables(terms, variables)
    assert result == [['term1'], ['term2']]

def test_lookup_variables_undefined_error(lookup_module, monkeypatch):
    terms = ['term1', 'term2']
    variables = {}

    def mock_listify_lookup_plugin_terms(x, templar, loader, fail_on_undefined):
        raise UndefinedError("undefined variable")

    monkeypatch.setattr('ansible.plugins.lookup.nested.listify_lookup_plugin_terms', mock_listify_lookup_plugin_terms)
    with pytest.raises(AnsibleUndefinedVariable, match="One of the nested variables was undefined. The error was: undefined variable"):
        lookup_module._lookup_variables(terms, variables)

def test_run_empty_terms(lookup_module, monkeypatch):
    terms = []
    variables = {}

    def mock_lookup_variables(terms, variables):
        return terms

    monkeypatch.setattr(lookup_module, '_lookup_variables', mock_lookup_variables)
    with pytest.raises(AnsibleError, match="with_nested requires at least one element in the nested list"):
        lookup_module.run(terms, variables)

def test_run_success(lookup_module, monkeypatch):
    terms = [['a', 'b'], ['c', 'd']]
    variables = {}

    def mock_lookup_variables(terms, variables):
        return terms

    def mock_combine(a, b):
        return [(x, y) for x in a for y in b]

    def mock_flatten(x):
        return x

    monkeypatch.setattr(lookup_module, '_lookup_variables', mock_lookup_variables)
    monkeypatch.setattr(lookup_module, '_combine', mock_combine)
    monkeypatch.setattr(lookup_module, '_flatten', mock_flatten)

    result = lookup_module.run(terms, variables)
    assert result == [('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd')]
