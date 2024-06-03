# file lib/ansible/plugins/lookup/vars.py:75-106
# lines [75, 77, 78, 79, 80, 82, 83, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 99, 100, 101, 102, 104, 106]
# branches ['78->79', '78->80', '86->87', '86->106', '87->88', '87->90', '101->102', '101->104']

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError, AnsibleUndefinedVariable
from ansible.plugins.lookup.vars import LookupModule
from ansible.template import Templar

@pytest.fixture
def templar_mock():
    return MagicMock(spec=Templar)

@pytest.fixture
def lookup_module(templar_mock):
    module = LookupModule()
    module._templar = templar_mock
    module._load_name = 'vars'  # Mock the _load_name attribute
    module.set_options = MagicMock()  # Mock set_options to avoid configuration issues
    module.get_option = MagicMock(return_value=None)  # Mock get_option to avoid configuration issues
    return module

def test_run_with_variables(lookup_module, templar_mock):
    terms = ['var1', 'var2']
    variables = {'var1': 'value1', 'var2': 'value2'}
    templar_mock._available_variables = variables
    templar_mock.template.side_effect = lambda x, fail_on_undefined: x

    result = lookup_module.run(terms, variables=variables)

    assert result == ['value1', 'value2']
    templar_mock.template.assert_any_call('value1', fail_on_undefined=True)
    templar_mock.template.assert_any_call('value2', fail_on_undefined=True)

def test_run_with_default(lookup_module, templar_mock):
    terms = ['var1', 'var2']
    variables = {'var1': 'value1'}
    templar_mock._available_variables = variables
    templar_mock.template.side_effect = lambda x, fail_on_undefined: x
    lookup_module.set_options = MagicMock()
    lookup_module.get_option = MagicMock(return_value='default_value')

    result = lookup_module.run(terms, variables=variables)

    assert result == ['value1', 'default_value']
    templar_mock.template.assert_any_call('value1', fail_on_undefined=True)
    lookup_module.get_option.assert_called_with('default')

def test_run_with_invalid_identifier(lookup_module):
    terms = [123]
    with pytest.raises(AnsibleError, match='Invalid setting identifier'):
        lookup_module.run(terms)

def test_run_with_undefined_variable(lookup_module, templar_mock):
    terms = ['var1']
    variables = {}
    templar_mock._available_variables = variables
    lookup_module.set_options = MagicMock()
    lookup_module.get_option = MagicMock(return_value=None)

    with pytest.raises(AnsibleUndefinedVariable, match='No variable found with this name: var1'):
        lookup_module.run(terms, variables=variables)

def test_run_with_hostvars(lookup_module, templar_mock):
    terms = ['var1']
    variables = {
        'hostvars': {
            'localhost': {
                'var1': 'value1'
            }
        },
        'inventory_hostname': 'localhost'
    }
    templar_mock._available_variables = variables
    templar_mock.template.side_effect = lambda x, fail_on_undefined: x

    result = lookup_module.run(terms, variables=variables)

    assert result == ['value1']
    templar_mock.template.assert_any_call('value1', fail_on_undefined=True)
