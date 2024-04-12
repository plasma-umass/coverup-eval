# file lib/ansible/module_utils/common/parameters.py:245-296
# lines [274, 275, 276, 277]
# branches ['268->267', '273->274', '291->267', '293->292']

import pytest
from ansible.module_utils.common.parameters import _list_deprecations

def test_list_deprecations_with_removed_at_date_and_sub_arguments(mocker):
    argument_spec = {
        'param1': {
            'removed_at_date': '2023-01-01',
            'removed_from_collection': 'test_collection',
            'options': {
                'subparam1': {
                    'removed_in_version': '2.9',
                    'removed_from_collection': 'sub_test_collection'
                }
            }
        }
    }
    parameters = {
        'param1': [
            {'subparam1': 'value1'},
            {'subparam1': 'value2'}
        ]
    }

    expected_deprecations = [
        {
            'msg': "Param 'param1' is deprecated. See the module docs for more information",
            'date': '2023-01-01',
            'collection_name': 'test_collection'
        },
        {
            'msg': "Param 'param1[\"subparam1\"]' is deprecated. See the module docs for more information",
            'version': '2.9',
            'collection_name': 'sub_test_collection'
        },
        {
            'msg': "Param 'param1[\"subparam1\"]' is deprecated. See the module docs for more information",
            'version': '2.9',
            'collection_name': 'sub_test_collection'
        }
    ]

    deprecations = _list_deprecations(argument_spec, parameters)
    assert deprecations == expected_deprecations
