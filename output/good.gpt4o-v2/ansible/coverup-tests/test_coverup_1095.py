# file: lib/ansible/plugins/lookup/vars.py:75-106
# asked: {"lines": [75, 77, 78, 79, 80, 82, 83, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 99, 100, 101, 102, 104, 106], "branches": [[78, 79], [78, 80], [86, 87], [86, 106], [87, 88], [87, 90], [101, 102], [101, 104]]}
# gained: {"lines": [75, 77, 78, 79, 80, 82, 83, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 99, 100, 101, 102, 104, 106], "branches": [[78, 79], [78, 80], [86, 87], [86, 106], [87, 88], [87, 90], [101, 102], [101, 104]]}

import pytest
from ansible.errors import AnsibleError, AnsibleUndefinedVariable
from ansible.module_utils.six import string_types
from ansible.plugins.lookup.vars import LookupModule
from ansible.template import Templar
from unittest.mock import MagicMock

@pytest.fixture
def templar():
    return MagicMock(spec=Templar)

@pytest.fixture
def lookup_module(templar):
    lm = LookupModule(loader=None, templar=templar)
    lm._load_name = 'vars'
    lm.set_options = MagicMock()
    lm.get_option = MagicMock(side_effect=lambda option: 'default_value' if option == 'default' else None)
    return lm

def test_run_with_valid_string_term(lookup_module, templar):
    terms = ['valid_term']
    variables = {'valid_term': 'value'}
    templar._available_variables = variables
    templar.template.return_value = 'templated_value'

    result = lookup_module.run(terms, variables)

    assert result == ['templated_value']
    templar.template.assert_called_once_with('value', fail_on_undefined=True)

def test_run_with_invalid_non_string_term(lookup_module):
    terms = [123]  # Non-string term

    with pytest.raises(AnsibleError, match='Invalid setting identifier'):
        lookup_module.run(terms)

def test_run_with_missing_variable_and_default(lookup_module, templar):
    terms = ['missing_term']
    variables = {}
    templar._available_variables = variables

    result = lookup_module.run(terms, variables)

    assert result == ['default_value']

def test_run_with_missing_variable_and_no_default(lookup_module, templar):
    terms = ['missing_term']
    variables = {}
    templar._available_variables = variables
    lookup_module.get_option = MagicMock(return_value=None)

    with pytest.raises(AnsibleUndefinedVariable, match='No variable found with this name'):
        lookup_module.run(terms, variables)

def test_run_with_hostvars(lookup_module, templar):
    terms = ['hostvar_term']
    variables = {
        'hostvars': {
            'inventory_hostname': {
                'hostvar_term': 'hostvar_value'
            }
        },
        'inventory_hostname': 'inventory_hostname'
    }
    templar._available_variables = variables
    templar.template.return_value = 'templated_hostvar_value'

    result = lookup_module.run(terms, variables)

    assert result == ['templated_hostvar_value']
    templar.template.assert_called_once_with('hostvar_value', fail_on_undefined=True)
