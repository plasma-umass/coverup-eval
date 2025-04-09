# file lib/ansible/template/native_helpers.py:23-43
# lines [23, 27, 28, 29, 30, 31, 32, 34, 41, 43]
# branches ['27->28', '27->30', '28->29', '28->43', '30->31', '30->34', '31->32', '31->43', '34->41', '34->43']

import pytest
from collections.abc import Mapping
from jinja2 import StrictUndefined, UndefinedError

# Assuming the function _fail_on_undefined is imported from ansible.template.native_helpers
from ansible.template.native_helpers import _fail_on_undefined

def test_fail_on_undefined_with_mapping():
    # Mocking a nested data structure with a StrictUndefined value
    mock_data = {
        'key1': 'value1',
        'key2': {
            'nested_key1': 'nested_value1',
            'nested_key2': StrictUndefined(name='undefined_var')
        }
    }

    with pytest.raises(UndefinedError):
        _fail_on_undefined(mock_data)

def test_fail_on_undefined_with_sequence():
    # Mocking a nested sequence with a StrictUndefined value
    mock_data = [
        'value1',
        ['nested_value1', StrictUndefined(name='undefined_var')]
    ]

    with pytest.raises(UndefinedError):
        _fail_on_undefined(mock_data)

def test_fail_on_undefined_with_no_undefined():
    # Mocking a nested data structure without any StrictUndefined value
    mock_data = {
        'key1': 'value1',
        'key2': {
            'nested_key1': 'nested_value1',
            'nested_key2': 'nested_value2'
        }
    }

    result = _fail_on_undefined(mock_data)
    assert result == mock_data

def test_fail_on_undefined_with_non_mapping_sequence():
    # Mocking a non-mapping, non-sequence data structure
    mock_data = 'simple_string'

    result = _fail_on_undefined(mock_data)
    assert result == mock_data
