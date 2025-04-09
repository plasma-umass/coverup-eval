# file lib/ansible/utils/listify.py:29-39
# lines [29, 31, 32, 34, 36, 37, 39]
# branches ['31->32', '31->34', '36->37', '36->39']

import pytest
from ansible.utils.listify import listify_lookup_plugin_terms
from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader
from collections.abc import Iterable
from ansible.module_utils.six import string_types

class MockTemplar(Templar):
    def template(self, variable, convert_bare=False, fail_on_undefined=True):
        if fail_on_undefined and variable == "{{ undefined_variable }}":
            raise ValueError("Undefined variable")
        return variable

@pytest.fixture
def templar():
    loader = DataLoader()
    return MockTemplar(loader=loader)

def test_listify_lookup_plugin_terms_with_undefined_variable(templar):
    with pytest.raises(ValueError):
        listify_lookup_plugin_terms("{{ undefined_variable }}", templar, None, fail_on_undefined=True)

def test_listify_lookup_plugin_terms_with_defined_variable(templar):
    terms = "{{ defined_variable }}"
    result = listify_lookup_plugin_terms(terms, templar, None, fail_on_undefined=False)
    assert isinstance(result, list)
    assert result == [terms]

def test_listify_lookup_plugin_terms_with_non_string_non_iterable(templar):
    terms = 42
    result = listify_lookup_plugin_terms(terms, templar, None)
    assert isinstance(result, list)
    assert result == [terms]

def test_listify_lookup_plugin_terms_with_string(templar):
    terms = "some_string"
    result = listify_lookup_plugin_terms(terms, templar, None)
    assert isinstance(result, list)
    assert result == [terms.strip()]

def test_listify_lookup_plugin_terms_with_convert_bare(templar):
    terms = "bare_string"
    result = listify_lookup_plugin_terms(terms, templar, None, convert_bare=True)
    assert isinstance(result, list)
    assert result == [terms.strip()]

def test_listify_lookup_plugin_terms_with_iterable(templar):
    terms = ["item1", "item2"]
    result = listify_lookup_plugin_terms(terms, templar, None)
    assert isinstance(result, Iterable)
    assert result == terms
