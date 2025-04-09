# file lib/ansible/module_utils/common/dict_transformations.py:16-52
# lines [37]
# branches ['36->37']

import pytest
from ansible.module_utils.common.dict_transformations import camel_dict_to_snake_dict

def test_camel_dict_to_snake_dict_with_nested_lists():
    camel_dict = {
        'CamelCaseKey': [
            {'NestedCamelCaseKey': 'value1'},
            [{'DeepNestedCamelCaseKey': 'value2'}]
        ]
    }
    expected_snake_dict = {
        'camel_case_key': [
            {'nested_camel_case_key': 'value1'},
            [{'deep_nested_camel_case_key': 'value2'}]
        ]
    }
    
    result = camel_dict_to_snake_dict(camel_dict)
    assert result == expected_snake_dict

