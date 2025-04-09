# file: lib/ansible/utils/listify.py:29-39
# asked: {"lines": [29, 31, 32, 34, 36, 37, 39], "branches": [[31, 32], [31, 34], [36, 37], [36, 39]]}
# gained: {"lines": [29, 31, 32, 34, 36, 37, 39], "branches": [[31, 32], [31, 34], [36, 37], [36, 39]]}

import pytest
from ansible.utils.listify import listify_lookup_plugin_terms
from collections.abc import Iterable
from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader

class MockTemplar:
    def template(self, var, convert_bare=False, fail_on_undefined=True):
        if fail_on_undefined and var == 'undefined':
            raise ValueError("Undefined variable")
        if convert_bare and isinstance(var, str):
            return var.upper()
        return var

@pytest.fixture
def templar():
    return MockTemplar()

def test_listify_lookup_plugin_terms_string(templar):
    terms = "test string"
    result = listify_lookup_plugin_terms(terms, templar, None)
    assert result == ["test string"]

def test_listify_lookup_plugin_terms_string_convert_bare(templar):
    terms = "test string"
    result = listify_lookup_plugin_terms(terms, templar, None, convert_bare=True)
    assert result == ["TEST STRING"]

def test_listify_lookup_plugin_terms_undefined(templar):
    terms = "undefined"
    with pytest.raises(ValueError):
        listify_lookup_plugin_terms(terms, templar, None, fail_on_undefined=True)

def test_listify_lookup_plugin_terms_list(templar):
    terms = ["item1", "item2"]
    result = listify_lookup_plugin_terms(terms, templar, None)
    assert result == ["item1", "item2"]

def test_listify_lookup_plugin_terms_non_iterable(templar):
    terms = 42
    result = listify_lookup_plugin_terms(terms, templar, None)
    assert result == [42]
