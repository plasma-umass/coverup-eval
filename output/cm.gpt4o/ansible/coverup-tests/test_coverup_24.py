# file lib/ansible/module_utils/common/parameters.py:245-296
# lines [245, 266, 267, 268, 269, 270, 272, 273, 274, 275, 276, 277, 279, 280, 281, 282, 283, 286, 287, 288, 289, 290, 291, 292, 293, 294, 296]
# branches ['267->268', '267->296', '268->267', '268->269', '269->270', '269->272', '273->274', '273->279', '279->280', '279->286', '287->267', '287->288', '289->290', '289->291', '291->267', '291->292', '292->267', '292->293', '293->292', '293->294']

import pytest
from ansible.module_utils.common.parameters import _list_deprecations

def test_list_deprecations():
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
                    'removed_in_version': '3.0',
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
        }
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
            'version': '3.0',
            'collection_name': 'test_collection'
        }
    ]
    
    deprecations = _list_deprecations(argument_spec, parameters)
    assert deprecations == expected_deprecations
