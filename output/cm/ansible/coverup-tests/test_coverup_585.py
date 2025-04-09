# file lib/ansible/plugins/filter/core.py:548-555
# lines [548, 552, 553, 555]
# branches ['552->553', '552->555']

import pytest
from ansible.errors import AnsibleFilterTypeError
from ansible.plugins.filter.core import list_of_dict_key_value_elements_to_dict

def test_list_of_dict_key_value_elements_to_dict_success():
    input_list = [{'key': 'name', 'value': 'John'}, {'key': 'age', 'value': 30}]
    expected_output = {'name': 'John', 'age': 30}
    assert list_of_dict_key_value_elements_to_dict(input_list) == expected_output

def test_list_of_dict_key_value_elements_to_dict_custom_keys():
    input_list = [{'id': 'name', 'val': 'John'}, {'id': 'age', 'val': 30}]
    expected_output = {'name': 'John', 'age': 30}
    assert list_of_dict_key_value_elements_to_dict(input_list, key_name='id', value_name='val') == expected_output

def test_list_of_dict_key_value_elements_to_dict_type_error():
    with pytest.raises(AnsibleFilterTypeError):
        list_of_dict_key_value_elements_to_dict("not a list")
