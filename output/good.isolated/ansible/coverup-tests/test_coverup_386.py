# file lib/ansible/plugins/filter/core.py:535-545
# lines [535, 539, 540, 542, 543, 544, 545]
# branches ['539->540', '539->542', '543->544', '543->545']

import pytest
from ansible.errors import AnsibleFilterTypeError
from ansible.plugins.filter.core import dict_to_list_of_dict_key_value_elements
from collections.abc import Mapping

def test_dict_to_list_of_dict_key_value_elements_success():
    test_dict = {'a': 1, 'b': 2}
    expected_output = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}]
    assert dict_to_list_of_dict_key_value_elements(test_dict) == expected_output

def test_dict_to_list_of_dict_key_value_elements_custom_key_value_names():
    test_dict = {'a': 1, 'b': 2}
    expected_output = [{'custom_key': 'a', 'custom_value': 1}, {'custom_key': 'b', 'custom_value': 2}]
    assert dict_to_list_of_dict_key_value_elements(test_dict, key_name='custom_key', value_name='custom_value') == expected_output

def test_dict_to_list_of_dict_key_value_elements_non_mapping():
    with pytest.raises(AnsibleFilterTypeError):
        dict_to_list_of_dict_key_value_elements([1, 2, 3])  # Not a mapping type

def test_dict_to_list_of_dict_key_value_elements_empty_dict():
    assert dict_to_list_of_dict_key_value_elements({}) == []
