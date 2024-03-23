# file lib/ansible/module_utils/common/dict_transformations.py:55-76
# lines [55, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 76]
# branches ['63->64', '63->65', '66->67', '66->69', '67->68', '67->74', '69->70', '69->73', '70->71', '70->74']

import pytest
from ansible.module_utils.common.dict_transformations import snake_dict_to_camel_dict

def test_snake_dict_to_camel_dict():
    # Test with a complex dictionary containing nested dictionaries and lists
    snake_dict = {
        'simple_key': 'value',
        'nested_dict': {
            'inner_key': 'inner_value',
            'inner_list': [1, 2, {'deep_key': 'deep_value'}]
        },
        'nested_list': [
            {'list_dict_key': 'list_dict_value'},
            ['sublist_item_1', 'sublist_item_2']
        ]
    }

    expected_camel_dict = {
        'simpleKey': 'value',
        'nestedDict': {
            'innerKey': 'inner_value',
            'innerList': [1, 2, {'deepKey': 'deep_value'}]
        },
        'nestedList': [
            {'listDictKey': 'list_dict_value'},
            ['sublist_item_1', 'sublist_item_2']
        ]
    }

    camel_dict = snake_dict_to_camel_dict(snake_dict)
    assert camel_dict == expected_camel_dict

    # Test with capitalize_first=True
    expected_camel_dict_capitalized = {
        'SimpleKey': 'value',
        'NestedDict': {
            'InnerKey': 'inner_value',
            'InnerList': [1, 2, {'DeepKey': 'deep_value'}]
        },
        'NestedList': [
            {'ListDictKey': 'list_dict_value'},
            ['sublist_item_1', 'sublist_item_2']
        ]
    }

    camel_dict_capitalized = snake_dict_to_camel_dict(snake_dict, capitalize_first=True)
    assert camel_dict_capitalized == expected_camel_dict_capitalized

    # Test with an empty dictionary
    assert snake_dict_to_camel_dict({}) == {}

    # Test with None
    assert snake_dict_to_camel_dict(None) is None

    # Test with a list containing None
    assert snake_dict_to_camel_dict([None, {'key_with_none': None}]) == [None, {'keyWithNone': None}]
