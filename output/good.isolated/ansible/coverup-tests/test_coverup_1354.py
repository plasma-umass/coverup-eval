# file lib/ansible/module_utils/common/parameters.py:299-344
# lines [317, 318]
# branches ['314->321', '326->309', '327->309']

import pytest
from ansible.module_utils.common.parameters import _list_no_log_values
from ansible.module_utils._text import to_native

def test_list_no_log_values_with_type_error(mocker):
    argument_spec = {
        'password': {'no_log': True},
        'options_field': {
            'options': {
                'nested_password': {'no_log': True}
            },
            'type': 'dict'
        }
    }
    params = {
        'password': 'secret',
        'options_field': {
            'nested_password': 'hidden'
        }
    }

    # Mocking _return_datastructure_name to raise a TypeError
    mocker.patch('ansible.module_utils.common.parameters._return_datastructure_name', side_effect=TypeError)

    with pytest.raises(TypeError) as exc:
        _list_no_log_values(argument_spec, params)

    assert 'Failed to convert "password"' in to_native(exc.value)

def test_list_no_log_values_with_sub_parameters_as_dict(mocker):
    argument_spec = {
        'options_field': {
            'options': {
                'nested_password': {'no_log': True}
            },
            'type': 'dict'
        }
    }
    params = {
        'options_field': {
            'nested_password': 'hidden'
        }
    }

    # Mocking _return_datastructure_name to return a set containing 'hidden'
    mocker.patch('ansible.module_utils.common.parameters._return_datastructure_name', return_value={'hidden'})

    no_log_values = _list_no_log_values(argument_spec, params)

    assert 'hidden' in no_log_values

def test_list_no_log_values_with_sub_parameters_as_list_of_dicts(mocker):
    argument_spec = {
        'options_field': {
            'options': {
                'nested_password': {'no_log': True}
            },
            'type': 'list',
            'elements': 'dict'
        }
    }
    params = {
        'options_field': [
            {'nested_password': 'hidden1'},
            {'nested_password': 'hidden2'}
        ]
    }

    # Mocking _return_datastructure_name to return a set containing 'hidden1' and 'hidden2'
    mocker.patch('ansible.module_utils.common.parameters._return_datastructure_name', side_effect=[{'hidden1'}, {'hidden2'}])

    no_log_values = _list_no_log_values(argument_spec, params)

    assert 'hidden1' in no_log_values
    assert 'hidden2' in no_log_values
