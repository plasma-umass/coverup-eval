# file: lib/ansible/plugins/filter/core.py:535-545
# asked: {"lines": [539, 540, 542, 543, 544, 545], "branches": [[539, 540], [539, 542], [543, 544], [543, 545]]}
# gained: {"lines": [539, 540, 542, 543, 544, 545], "branches": [[539, 540], [539, 542], [543, 544], [543, 545]]}

import pytest
from ansible.errors import AnsibleFilterTypeError
from collections.abc import Mapping

# Assuming the function is imported from the module
from ansible.plugins.filter.core import dict_to_list_of_dict_key_value_elements

def test_dict_to_list_of_dict_key_value_elements_valid_dict():
    mydict = {'a': 1, 'b': 2}
    expected = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}]
    result = dict_to_list_of_dict_key_value_elements(mydict)
    assert result == expected

def test_dict_to_list_of_dict_key_value_elements_empty_dict():
    mydict = {}
    expected = []
    result = dict_to_list_of_dict_key_value_elements(mydict)
    assert result == expected

def test_dict_to_list_of_dict_key_value_elements_custom_key_value_names():
    mydict = {'a': 1, 'b': 2}
    expected = [{'custom_key': 'a', 'custom_value': 1}, {'custom_key': 'b', 'custom_value': 2}]
    result = dict_to_list_of_dict_key_value_elements(mydict, key_name='custom_key', value_name='custom_value')
    assert result == expected

def test_dict_to_list_of_dict_key_value_elements_invalid_type():
    with pytest.raises(AnsibleFilterTypeError, match="dict2items requires a dictionary, got <class 'list'> instead."):
        dict_to_list_of_dict_key_value_elements(['a', 'b'])

def test_dict_to_list_of_dict_key_value_elements_non_mapping_type():
    with pytest.raises(AnsibleFilterTypeError, match="dict2items requires a dictionary, got <class 'int'> instead."):
        dict_to_list_of_dict_key_value_elements(123)
