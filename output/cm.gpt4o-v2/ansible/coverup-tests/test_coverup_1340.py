# file: lib/ansible/plugins/lookup/nested.py:57-85
# asked: {"lines": [57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], "branches": [[61, 62], [61, 67], [76, 77], [76, 78], [79, 80], [79, 82], [83, 84], [83, 85]]}
# gained: {"lines": [57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], "branches": [[61, 62], [61, 67], [76, 77], [76, 78], [79, 80], [79, 82], [83, 84], [83, 85]]}

import pytest
from unittest.mock import MagicMock, patch
from jinja2.exceptions import UndefinedError
from ansible.errors import AnsibleError, AnsibleUndefinedVariable
from ansible.plugins.lookup.nested import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_lookup_variables_success(lookup_module):
    terms = ['var1', 'var2']
    variables = {'var1': 'value1', 'var2': 'value2'}
    lookup_module._templar = MagicMock()
    lookup_module._loader = MagicMock()

    with patch('ansible.plugins.lookup.nested.listify_lookup_plugin_terms', side_effect=lambda x, templar, loader, fail_on_undefined: [variables[x]]):
        result = lookup_module._lookup_variables(terms, variables)
        assert result == [['value1'], ['value2']]

def test_lookup_variables_undefined_error(lookup_module):
    terms = ['var1', 'var2']
    variables = {'var1': 'value1'}
    lookup_module._templar = MagicMock()
    lookup_module._loader = MagicMock()

    with patch('ansible.plugins.lookup.nested.listify_lookup_plugin_terms', side_effect=UndefinedError):
        with pytest.raises(AnsibleUndefinedVariable, match="One of the nested variables was undefined. The error was: "):
            lookup_module._lookup_variables(terms, variables)

def test_run_empty_terms(lookup_module):
    terms = []
    variables = {}
    lookup_module._templar = MagicMock()
    lookup_module._loader = MagicMock()

    with patch.object(lookup_module, '_lookup_variables', return_value=terms):
        with pytest.raises(AnsibleError, match="with_nested requires at least one element in the nested list"):
            lookup_module.run(terms, variables)

def test_run_success(lookup_module):
    terms = [['a'], ['b']]
    variables = {}
    lookup_module._templar = MagicMock()
    lookup_module._loader = MagicMock()

    with patch.object(lookup_module, '_lookup_variables', return_value=terms):
        with patch.object(lookup_module, '_combine', side_effect=lambda x, y: x + y):
            with patch.object(lookup_module, '_flatten', side_effect=lambda x: x):
                result = lookup_module.run(terms, variables)
                assert result == ['a', 'b']
