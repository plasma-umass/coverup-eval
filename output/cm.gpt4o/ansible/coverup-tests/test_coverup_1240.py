# file lib/ansible/module_utils/common/parameters.py:245-296
# lines []
# branches ['268->267', '289->291', '291->267', '293->292']

import pytest
from ansible.module_utils.common.parameters import _list_deprecations
from collections.abc import Mapping

def test_list_deprecations(mocker):
    argument_spec = {
        'param1': {
            'removed_at_date': '2023-01-01',
            'removed_from_collection': 'test_collection'
        },
        'param2': {
            'removed_in_version': '2.9',
            'removed_from_collection': 'test_collection'
        },
        'param3': {
            'options': {
                'subparam1': {
                    'removed_at_date': '2023-01-01',
                    'removed_from_collection': 'test_collection'
                }
            }
        },
        'param4': {
            'options': {
                'subparam2': {
                    'removed_in_version': '2.10',
                    'removed_from_collection': 'test_collection'
                }
            }
        }
    }
    parameters = {
        'param1': 'value1',
        'param2': 'value2',
        'param3': {
            'subparam1': 'subvalue1'
        },
        'param4': [
            {
                'subparam2': 'subvalue2'
            }
        ]
    }

    expected_deprecations = [
        {
            'msg': "Param 'param1' is deprecated. See the module docs for more information",
            'date': '2023-01-01',
            'collection_name': 'test_collection'
        },
        {
            'msg': "Param 'param2' is deprecated. See the module docs for more information",
            'version': '2.9',
            'collection_name': 'test_collection'
        },
        {
            'msg': "Param 'param3[\"subparam1\"]' is deprecated. See the module docs for more information",
            'date': '2023-01-01',
            'collection_name': 'test_collection'
        },
        {
            'msg': "Param 'param4[\"subparam2\"]' is deprecated. See the module docs for more information",
            'version': '2.10',
            'collection_name': 'test_collection'
        }
    ]

    deprecations = _list_deprecations(argument_spec, parameters)
    assert deprecations == expected_deprecations

    # Clean up if necessary (not needed in this case as no external state is modified)
