# file: lib/ansible/module_utils/common/parameters.py:299-344
# asked: {"lines": [310, 312, 314, 315, 316, 317, 318, 321, 322, 323, 324, 326, 327, 329, 330, 332, 335, 336, 338, 339, 340, 342], "branches": [[309, 310], [310, 312], [310, 321], [314, 315], [314, 321], [322, 309], [322, 323], [326, 309], [326, 327], [327, 309], [327, 329], [329, 330], [329, 332], [332, 309], [332, 335], [335, 336], [335, 338], [338, 339], [338, 342]]}
# gained: {"lines": [310, 312, 314, 315, 316, 321, 322, 323, 324, 326, 327, 329, 330, 332, 335, 336, 338, 342], "branches": [[309, 310], [310, 312], [310, 321], [314, 315], [322, 309], [322, 323], [326, 327], [327, 329], [329, 330], [329, 332], [332, 309], [332, 335], [335, 336], [335, 338], [338, 342]]}

import pytest
from ansible.module_utils.common.parameters import _list_no_log_values
from ansible.module_utils._text import to_native
from collections.abc import Mapping
from ansible.module_utils.common.validation import check_type_dict

def _return_datastructure_name(value):
    if isinstance(value, dict):
        return value.keys()
    elif isinstance(value, list):
        return [str(v) for v in value]
    else:
        return [str(value)]

def test_list_no_log_values_simple_no_log():
    argument_spec = {
        'param1': {'no_log': True},
        'param2': {'no_log': False}
    }
    params = {
        'param1': 'secret_value',
        'param2': 'normal_value'
    }
    result = _list_no_log_values(argument_spec, params)
    assert result == {'secret_value'}

def test_list_no_log_values_with_suboptions():
    argument_spec = {
        'param1': {
            'type': 'dict',
            'options': {
                'subparam1': {'no_log': True},
                'subparam2': {'no_log': False}
            }
        }
    }
    params = {
        'param1': {
            'subparam1': 'secret_sub_value',
            'subparam2': 'normal_sub_value'
        }
    }
    result = _list_no_log_values(argument_spec, params)
    assert result == {'secret_sub_value'}

def test_list_no_log_values_with_list_of_dicts():
    argument_spec = {
        'param1': {
            'type': 'list',
            'elements': 'dict',
            'options': {
                'subparam1': {'no_log': True},
                'subparam2': {'no_log': False}
            }
        }
    }
    params = {
        'param1': [
            {'subparam1': 'secret_sub_value1', 'subparam2': 'normal_sub_value1'},
            {'subparam1': 'secret_sub_value2', 'subparam2': 'normal_sub_value2'}
        ]
    }
    result = _list_no_log_values(argument_spec, params)
    assert result == {'secret_sub_value1', 'secret_sub_value2'}

def test_list_no_log_values_with_invalid_subparam_type():
    argument_spec = {
        'param1': {
            'type': 'dict',
            'options': {
                'subparam1': {'no_log': True}
            }
        }
    }
    params = {
        'param1': 'invalid_type'
    }
    with pytest.raises(TypeError, match="dictionary requested, could not parse JSON or key=value"):
        _list_no_log_values(argument_spec, params)

def test_list_no_log_values_with_string_subparam():
    argument_spec = {
        'param1': {
            'type': 'dict',
            'options': {
                'subparam1': {'no_log': True}
            }
        }
    }
    params = {
        'param1': '{"subparam1": "secret_sub_value"}'
    }
    result = _list_no_log_values(argument_spec, params)
    assert result == {'secret_sub_value'}
