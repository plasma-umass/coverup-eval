# file lib/ansible/utils/listify.py:29-39
# lines [31, 32, 34, 36, 37, 39]
# branches ['31->32', '31->34', '36->37', '36->39']

import pytest
from ansible.utils.listify import listify_lookup_plugin_terms
from unittest.mock import Mock

def test_listify_lookup_plugin_terms_string(mocker):
    templar = Mock()
    templar.template = Mock(return_value='templated_string')
    terms = 'some_string'
    
    result = listify_lookup_plugin_terms(terms, templar, None)
    
    templar.template.assert_called_once_with('some_string', convert_bare=False, fail_on_undefined=True)
    assert result == ['templated_string']

def test_listify_lookup_plugin_terms_non_iterable(mocker):
    templar = Mock()
    templar.template = Mock(return_value=42)
    terms = 42
    
    result = listify_lookup_plugin_terms(terms, templar, None)
    
    templar.template.assert_called_once_with(42, fail_on_undefined=True)
    assert result == [42]
