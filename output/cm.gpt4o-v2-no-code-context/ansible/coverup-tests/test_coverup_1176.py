# file: lib/ansible/module_utils/common/parameters.py:299-344
# asked: {"lines": [317, 318, 339, 340], "branches": [[314, 321], [326, 309], [327, 309], [338, 339]]}
# gained: {"lines": [317, 318], "branches": []}

import pytest
from ansible.module_utils.common.parameters import _list_no_log_values
from ansible.module_utils._text import to_native
from collections.abc import Mapping
from ansible.module_utils.six import string_types

def test_list_no_log_values_type_error():
    argument_spec = {
        'param1': {'no_log': True},
    }
    params = {
        'param1': object(),  # This will cause TypeError in _return_datastructure_name
    }
    with pytest.raises(TypeError, match='Failed to convert "param1"'):
        _list_no_log_values(argument_spec, params)

def test_list_no_log_values_suboptions_type_error():
    argument_spec = {
        'param1': {
            'type': 'dict',
            'options': {
                'subparam1': {'no_log': True}
            }
        }
    }
    params = {
        'param1': 'not_a_dict',  # This will cause TypeError in sub parameter validation
    }
    with pytest.raises(TypeError, match="dictionary requested, could not parse JSON or key=value"):
        _list_no_log_values(argument_spec, params)

def test_list_no_log_values_suboptions_list_type_error():
    argument_spec = {
        'param1': {
            'type': 'list',
            'elements': 'dict',
            'options': {
                'subparam1': {'no_log': True}
            }
        }
    }
    params = {
        'param1': ['not_a_dict'],  # This will cause TypeError in sub parameter validation
    }
    with pytest.raises(TypeError, match="dictionary requested, could not parse JSON or key=value"):
        _list_no_log_values(argument_spec, params)

def test_list_no_log_values_suboptions():
    argument_spec = {
        'param1': {
            'type': 'dict',
            'options': {
                'subparam1': {'no_log': True}
            }
        }
    }
    params = {
        'param1': {
            'subparam1': 'secret_value'
        }
    }
    no_log_values = _list_no_log_values(argument_spec, params)
    assert 'secret_value' in no_log_values

def test_list_no_log_values_suboptions_list():
    argument_spec = {
        'param1': {
            'type': 'list',
            'elements': 'dict',
            'options': {
                'subparam1': {'no_log': True}
            }
        }
    }
    params = {
        'param1': [
            {'subparam1': 'secret_value1'},
            {'subparam1': 'secret_value2'}
        ]
    }
    no_log_values = _list_no_log_values(argument_spec, params)
    assert 'secret_value1' in no_log_values
    assert 'secret_value2' in no_log_values
