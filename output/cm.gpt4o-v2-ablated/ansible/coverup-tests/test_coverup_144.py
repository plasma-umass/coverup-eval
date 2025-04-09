# file: lib/ansible/utils/listify.py:29-39
# asked: {"lines": [29, 31, 32, 34, 36, 37, 39], "branches": [[31, 32], [31, 34], [36, 37], [36, 39]]}
# gained: {"lines": [29, 31, 32, 34, 36, 37, 39], "branches": [[31, 32], [31, 34], [36, 37], [36, 39]]}

import pytest
from unittest.mock import Mock
from collections.abc import Iterable
from ansible.utils.listify import listify_lookup_plugin_terms

def test_listify_lookup_plugin_terms_string(monkeypatch):
    templar = Mock()
    templar.template = Mock(return_value='templated_string')
    terms = 'test_string'
    
    result = listify_lookup_plugin_terms(terms, templar, None)
    
    templar.template.assert_called_once_with('test_string', convert_bare=False, fail_on_undefined=True)
    assert result == ['templated_string']

def test_listify_lookup_plugin_terms_non_string(monkeypatch):
    templar = Mock()
    templar.template = Mock(return_value=['templated_list'])
    terms = ['test_list']
    
    result = listify_lookup_plugin_terms(terms, templar, None)
    
    templar.template.assert_called_once_with(['test_list'], fail_on_undefined=True)
    assert result == ['templated_list']

def test_listify_lookup_plugin_terms_non_iterable(monkeypatch):
    templar = Mock()
    templar.template = Mock(return_value=42)
    terms = 42
    
    result = listify_lookup_plugin_terms(terms, templar, None)
    
    templar.template.assert_called_once_with(42, fail_on_undefined=True)
    assert result == [42]

def test_listify_lookup_plugin_terms_convert_bare(monkeypatch):
    templar = Mock()
    templar.template = Mock(return_value='templated_string')
    terms = 'test_string'
    
    result = listify_lookup_plugin_terms(terms, templar, None, convert_bare=True)
    
    templar.template.assert_called_once_with('test_string', convert_bare=True, fail_on_undefined=True)
    assert result == ['templated_string']

def test_listify_lookup_plugin_terms_fail_on_undefined(monkeypatch):
    templar = Mock()
    templar.template = Mock(return_value='templated_string')
    terms = 'test_string'
    
    result = listify_lookup_plugin_terms(terms, templar, None, fail_on_undefined=False)
    
    templar.template.assert_called_once_with('test_string', convert_bare=False, fail_on_undefined=False)
    assert result == ['templated_string']
