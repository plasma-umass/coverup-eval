# file: lib/ansible/module_utils/common/dict_transformations.py:16-52
# asked: {"lines": [30, 32, 33, 34, 35, 36, 37, 39, 41, 43, 44, 45, 46, 47, 48, 50, 52], "branches": [[33, 34], [33, 41], [34, 35], [34, 36], [36, 37], [36, 39], [44, 45], [44, 52], [45, 46], [45, 47], [47, 48], [47, 50]]}
# gained: {"lines": [30, 32, 33, 34, 35, 36, 37, 39, 41, 43, 44, 45, 46, 47, 48, 50, 52], "branches": [[33, 34], [33, 41], [34, 35], [34, 36], [36, 37], [36, 39], [44, 45], [44, 52], [45, 46], [45, 47], [47, 48], [47, 50]]}

import pytest
from ansible.module_utils.common.dict_transformations import camel_dict_to_snake_dict

def test_camel_dict_to_snake_dict_with_nested_dict():
    camel_dict = {
        'OuterKey': {
            'InnerKey': 'value'
        }
    }
    expected_snake_dict = {
        'outer_key': {
            'inner_key': 'value'
        }
    }
    result = camel_dict_to_snake_dict(camel_dict)
    assert result == expected_snake_dict

def test_camel_dict_to_snake_dict_with_list_of_dicts():
    camel_dict = {
        'ListKey': [
            {'InnerKey': 'value1'},
            {'InnerKey': 'value2'}
        ]
    }
    expected_snake_dict = {
        'list_key': [
            {'inner_key': 'value1'},
            {'inner_key': 'value2'}
        ]
    }
    result = camel_dict_to_snake_dict(camel_dict)
    assert result == expected_snake_dict

def test_camel_dict_to_snake_dict_with_mixed_list():
    camel_dict = {
        'ListKey': [
            {'InnerKey': 'value1'},
            ['SubListValue1', 'SubListValue2'],
            'StringValue'
        ]
    }
    expected_snake_dict = {
        'list_key': [
            {'inner_key': 'value1'},
            ['SubListValue1', 'SubListValue2'],
            'StringValue'
        ]
    }
    result = camel_dict_to_snake_dict(camel_dict)
    assert result == expected_snake_dict

def test_camel_dict_to_snake_dict_with_ignore_list():
    camel_dict = {
        'OuterKey': {
            'InnerKey': 'value'
        },
        'Tags': {
            'TagKey': 'TagValue'
        }
    }
    expected_snake_dict = {
        'outer_key': {
            'inner_key': 'value'
        },
        'tags': {
            'TagKey': 'TagValue'
        }
    }
    result = camel_dict_to_snake_dict(camel_dict, ignore_list=['Tags'])
    assert result == expected_snake_dict
