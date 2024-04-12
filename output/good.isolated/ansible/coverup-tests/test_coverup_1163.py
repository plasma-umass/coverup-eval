# file lib/ansible/module_utils/common/dict_transformations.py:16-52
# lines [30, 32, 33, 34, 35, 36, 37, 39, 41, 43, 44, 45, 46, 47, 48, 50, 52]
# branches ['33->34', '33->41', '34->35', '34->36', '36->37', '36->39', '44->45', '44->52', '45->46', '45->47', '47->48', '47->50']

import pytest
from ansible.module_utils.common.dict_transformations import camel_dict_to_snake_dict

def test_camel_dict_to_snake_dict_with_nested_lists_and_dicts(mocker):
    # Mock the _camel_to_snake function since it's not provided in the snippet
    mock_camel_to_snake = mocker.patch('ansible.module_utils.common.dict_transformations._camel_to_snake', side_effect=lambda x, reversible: x.lower())

    # Define a camelCase dictionary with nested lists and dicts to cover lines 30-52
    camel_dict = {
        'CamelCaseKey': {
            'NestedCamelCaseKey': 'value',
            'AnotherNestedKey': [
                {'ListNestedCamelCase': 'value'},
                ['SubList', {'SubListDict': 'value'}]
            ]
        },
        'SimpleKey': 'simpleValue',
        'ListKey': ['item1', {'ListItemDict': 'value'}]
    }

    # Expected snake_case dictionary
    expected_snake_dict = {
        'camelcasekey': {
            'nestedcamelcasekey': 'value',
            'anothernestedkey': [
                {'listnestedcamelcase': 'value'},
                ['SubList', {'sublistdict': 'value'}]
            ]
        },
        'simplekey': 'simpleValue',
        'listkey': ['item1', {'listitemdict': 'value'}]
    }

    # Call the function to test
    result = camel_dict_to_snake_dict(camel_dict)

    # Assertions to verify the postconditions
    assert result == expected_snake_dict
    assert isinstance(result['camelcasekey']['anothernestedkey'][1], list)
    assert isinstance(result['camelcasekey']['anothernestedkey'][1][1], dict)
    assert result['camelcasekey']['anothernestedkey'][1][1]['sublistdict'] == 'value'
    assert result['listkey'][1]['listitemdict'] == 'value'

    # Verify that the _camel_to_snake mock was called
    assert mock_camel_to_snake.call_count > 0
