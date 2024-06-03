# file lib/ansible/plugins/filter/core.py:548-555
# lines [548, 552, 553, 555]
# branches ['552->553', '552->555']

import pytest
from ansible.plugins.filter.core import list_of_dict_key_value_elements_to_dict, AnsibleFilterTypeError
from ansible.module_utils.common.collections import is_sequence

def test_list_of_dict_key_value_elements_to_dict_valid_input():
    mylist = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}]
    result = list_of_dict_key_value_elements_to_dict(mylist)
    assert result == {'a': 1, 'b': 2}

def test_list_of_dict_key_value_elements_to_dict_invalid_input():
    with pytest.raises(AnsibleFilterTypeError, match="items2dict requires a list, got"):
        list_of_dict_key_value_elements_to_dict("not a list")

def test_list_of_dict_key_value_elements_to_dict_custom_keys():
    mylist = [{'custom_key': 'x', 'custom_value': 10}, {'custom_key': 'y', 'custom_value': 20}]
    result = list_of_dict_key_value_elements_to_dict(mylist, key_name='custom_key', value_name='custom_value')
    assert result == {'x': 10, 'y': 20}
