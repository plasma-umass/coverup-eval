# file lib/ansible/module_utils/common/dict_transformations.py:16-52
# lines [16, 30, 32, 33, 34, 35, 36, 37, 39, 41, 43, 44, 45, 46, 47, 48, 50, 52]
# branches ['33->34', '33->41', '34->35', '34->36', '36->37', '36->39', '44->45', '44->52', '45->46', '45->47', '47->48', '47->50']

import pytest
from ansible.module_utils.common.dict_transformations import camel_dict_to_snake_dict

def _camel_to_snake(name, reversible=False):
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    if reversible:
        s2 = re.sub(r'([a-z])_([a-z])', r'\1_\2', s2)
    return s2

def test_camel_dict_to_snake_dict(mocker):
    # Mock the _camel_to_snake function to ensure it is called correctly
    mock_camel_to_snake = mocker.patch('ansible.module_utils.common.dict_transformations._camel_to_snake', side_effect=_camel_to_snake)

    camel_dict = {
        'CamelCaseKey': 'value',
        'NestedCamelCase': {
            'AnotherCamelCase': 'nested_value'
        },
        'ListCamelCase': [
            {'ListNestedCamelCase': 'list_value'},
            'string_value'
        ],
        'Tags': {
            'Key': 'Value'
        }
    }

    expected_snake_dict = {
        'camel_case_key': 'value',
        'nested_camel_case': {
            'another_camel_case': 'nested_value'
        },
        'list_camel_case': [
            {'list_nested_camel_case': 'list_value'},
            'string_value'
        ],
        'tags': {
            'Key': 'Value'
        }
    }

    result = camel_dict_to_snake_dict(camel_dict, reversible=True, ignore_list=('Tags',))
    assert result == expected_snake_dict

    # Ensure the mock was called correctly
    assert mock_camel_to_snake.call_count > 0

    # Clean up after the test
    mocker.stopall()
