# file lib/ansible/module_utils/common/parameters.py:245-296
# lines [245, 266, 267, 268, 269, 270, 272, 273, 274, 275, 276, 277, 279, 280, 281, 282, 283, 286, 287, 288, 289, 290, 291, 292, 293, 294, 296]
# branches ['267->268', '267->296', '268->267', '268->269', '269->270', '269->272', '273->274', '273->279', '279->280', '279->286', '287->267', '287->288', '289->290', '289->291', '291->267', '291->292', '292->267', '292->293', '293->292', '293->294']

import pytest
from ansible.module_utils.common.parameters import _list_deprecations
from collections.abc import Mapping

def test_list_deprecations_with_sub_arguments():
    argument_spec = {
        'parent': {
            'options': {
                'child': {
                    'removed_in_version': '2.10',
                    'removed_from_collection': 'test_collection'
                }
            }
        }
    }
    parameters = {
        'parent': {
            'child': 'value'
        }
    }

    expected_deprecations = [
        {
            'msg': "Param 'parent[\"child\"]' is deprecated. See the module docs for more information",
            'version': '2.10',
            'collection_name': 'test_collection'
        }
    ]

    deprecations = _list_deprecations(argument_spec, parameters)
    assert deprecations == expected_deprecations, "Deprecations did not match expected output"

def test_list_deprecations_with_sub_arguments_list():
    argument_spec = {
        'parent': {
            'options': {
                'child': {
                    'removed_in_version': '2.10',
                    'removed_from_collection': 'test_collection'
                }
            }
        }
    }
    parameters = {
        'parent': [
            {'child': 'value1'},
            {'child': 'value2'}
        ]
    }

    expected_deprecations = [
        {
            'msg': "Param 'parent[\"child\"]' is deprecated. See the module docs for more information",
            'version': '2.10',
            'collection_name': 'test_collection'
        },
        {
            'msg': "Param 'parent[\"child\"]' is deprecated. See the module docs for more information",
            'version': '2.10',
            'collection_name': 'test_collection'
        }
    ]

    deprecations = _list_deprecations(argument_spec, parameters)
    assert deprecations == expected_deprecations, "Deprecations did not match expected output for list of sub-arguments"
