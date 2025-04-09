# file: lib/ansible/utils/listify.py:29-39
# asked: {"lines": [29, 31, 32, 34, 36, 37, 39], "branches": [[31, 32], [31, 34], [36, 37], [36, 39]]}
# gained: {"lines": [29, 31, 32, 34, 36, 37, 39], "branches": [[31, 32], [31, 34], [36, 37], [36, 39]]}

import pytest
from unittest.mock import Mock
from ansible.utils.listify import listify_lookup_plugin_terms
from ansible.module_utils.six import string_types
from ansible.module_utils.common._collections_compat import Iterable

@pytest.fixture
def templar():
    return Mock()

@pytest.fixture
def loader():
    return Mock()

def test_listify_lookup_plugin_terms_string(templar, loader):
    templar.template.return_value = "templated_string"
    result = listify_lookup_plugin_terms("  test_string  ", templar, loader)
    templar.template.assert_called_once_with("test_string", convert_bare=False, fail_on_undefined=True)
    assert result == ["templated_string"]

def test_listify_lookup_plugin_terms_non_string(templar, loader):
    templar.template.return_value = ["templated_list"]
    result = listify_lookup_plugin_terms(["test_list"], templar, loader)
    templar.template.assert_called_once_with(["test_list"], fail_on_undefined=True)
    assert result == ["templated_list"]

def test_listify_lookup_plugin_terms_non_iterable(templar, loader):
    templar.template.return_value = 123
    result = listify_lookup_plugin_terms(123, templar, loader)
    templar.template.assert_called_once_with(123, fail_on_undefined=True)
    assert result == [123]

def test_listify_lookup_plugin_terms_convert_bare(templar, loader):
    templar.template.return_value = "templated_string"
    result = listify_lookup_plugin_terms("  test_string  ", templar, loader, convert_bare=True)
    templar.template.assert_called_once_with("test_string", convert_bare=True, fail_on_undefined=True)
    assert result == ["templated_string"]

def test_listify_lookup_plugin_terms_fail_on_undefined_false(templar, loader):
    templar.template.return_value = "templated_string"
    result = listify_lookup_plugin_terms("  test_string  ", templar, loader, fail_on_undefined=False)
    templar.template.assert_called_once_with("test_string", convert_bare=False, fail_on_undefined=False)
    assert result == ["templated_string"]
