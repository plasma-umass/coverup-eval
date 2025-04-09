# file: lib/ansible/vars/clean.py:22-66
# asked: {"lines": [22, 51, 52, 53, 54, 55, 56, 58, 60, 61, 62, 64, 66], "branches": [[51, 52], [51, 54], [54, 55], [54, 58], [60, 61], [60, 66], [61, 62], [61, 64]]}
# gained: {"lines": [22, 51, 52, 53, 54, 55, 56, 58, 60, 61, 62, 64, 66], "branches": [[51, 52], [51, 54], [54, 55], [54, 58], [60, 61], [60, 66], [61, 62], [61, 64]]}

import pytest
from ansible.vars.clean import module_response_deepcopy

def test_module_response_deepcopy_dict():
    input_data = {'key1': 'value1', 'key2': {'subkey1': 'subvalue1'}}
    result = module_response_deepcopy(input_data)
    assert result == input_data
    assert result is not input_data
    assert result['key2'] is not input_data['key2']

def test_module_response_deepcopy_list():
    input_data = ['value1', ['subvalue1', 'subvalue2']]
    result = module_response_deepcopy(input_data)
    assert result == input_data
    assert result is not input_data
    assert result[1] is not input_data[1]

def test_module_response_deepcopy_other():
    input_data = 'string'
    result = module_response_deepcopy(input_data)
    assert result == input_data
    assert result is input_data
