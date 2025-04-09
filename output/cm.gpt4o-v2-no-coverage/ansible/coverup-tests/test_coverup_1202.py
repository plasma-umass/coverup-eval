# file: lib/ansible/template/native_helpers.py:23-43
# asked: {"lines": [], "branches": [[28, 43], [31, 43]]}
# gained: {"lines": [], "branches": [[28, 43], [31, 43]]}

import pytest
from jinja2.runtime import StrictUndefined
from ansible.module_utils.common.collections import is_sequence, Mapping
from ansible.template.native_helpers import _fail_on_undefined

def test_fail_on_undefined_with_mapping():
    data = {
        'key1': 'value1',
        'key2': StrictUndefined(name='undefined_key')
    }
    with pytest.raises(Exception) as excinfo:
        _fail_on_undefined(data)
    assert 'undefined_key' in str(excinfo.value)

def test_fail_on_undefined_with_sequence():
    data = ['value1', StrictUndefined(name='undefined_item')]
    with pytest.raises(Exception) as excinfo:
        _fail_on_undefined(data)
    assert 'undefined_item' in str(excinfo.value)

def test_fail_on_undefined_with_nested_structure():
    data = {
        'key1': ['value1', {'key2': StrictUndefined(name='undefined_nested')}]
    }
    with pytest.raises(Exception) as excinfo:
        _fail_on_undefined(data)
    assert 'undefined_nested' in str(excinfo.value)

def test_fail_on_undefined_with_no_undefined():
    data = {
        'key1': 'value1',
        'key2': ['value2', {'key3': 'value3'}]
    }
    result = _fail_on_undefined(data)
    assert result == data
