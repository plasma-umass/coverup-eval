# file: lib/ansible/module_utils/common/parameters.py:245-296
# asked: {"lines": [], "branches": [[268, 267], [291, 267], [293, 292]]}
# gained: {"lines": [], "branches": [[268, 267], [291, 267]]}

import pytest
from ansible.module_utils.common.parameters import _list_deprecations
from collections.abc import Mapping

def test_list_deprecations_with_removed_at_date():
    argument_spec = {
        'param1': {
            'removed_at_date': '2023-01-01',
            'removed_from_collection': 'test_collection'
        }
    }
    parameters = {
        'param1': 'value1'
    }
    result = _list_deprecations(argument_spec, parameters)
    assert result == [{
        'msg': "Param 'param1' is deprecated. See the module docs for more information",
        'date': '2023-01-01',
        'collection_name': 'test_collection'
    }]

def test_list_deprecations_with_removed_in_version():
    argument_spec = {
        'param1': {
            'removed_in_version': '2.9',
            'removed_from_collection': 'test_collection'
        }
    }
    parameters = {
        'param1': 'value1'
    }
    result = _list_deprecations(argument_spec, parameters)
    assert result == [{
        'msg': "Param 'param1' is deprecated. See the module docs for more information",
        'version': '2.9',
        'collection_name': 'test_collection'
    }]

def test_list_deprecations_with_sub_arguments():
    argument_spec = {
        'param1': {
            'options': {
                'sub_param1': {
                    'removed_in_version': '2.9',
                    'removed_from_collection': 'test_collection'
                }
            }
        }
    }
    parameters = {
        'param1': {
            'sub_param1': 'value1'
        }
    }
    result = _list_deprecations(argument_spec, parameters)
    assert result == [{
        'msg': "Param 'param1[\"sub_param1\"]' is deprecated. See the module docs for more information",
        'version': '2.9',
        'collection_name': 'test_collection'
    }]

def test_list_deprecations_with_sub_arguments_list():
    argument_spec = {
        'param1': {
            'options': {
                'sub_param1': {
                    'removed_in_version': '2.9',
                    'removed_from_collection': 'test_collection'
                }
            }
        }
    }
    parameters = {
        'param1': [
            {
                'sub_param1': 'value1'
            }
        ]
    }
    result = _list_deprecations(argument_spec, parameters)
    assert result == [{
        'msg': "Param 'param1[\"sub_param1\"]' is deprecated. See the module docs for more information",
        'version': '2.9',
        'collection_name': 'test_collection'
    }]

def test_list_deprecations_with_no_parameters():
    argument_spec = {
        'param1': {
            'removed_in_version': '2.9',
            'removed_from_collection': 'test_collection'
        }
    }
    parameters = {}
    result = _list_deprecations(argument_spec, parameters)
    assert result == []

def test_list_deprecations_with_non_mapping_sub_arguments():
    argument_spec = {
        'param1': {
            'options': {
                'sub_param1': {
                    'removed_in_version': '2.9',
                    'removed_from_collection': 'test_collection'
                }
            }
        }
    }
    parameters = {
        'param1': 'not_a_mapping'
    }
    result = _list_deprecations(argument_spec, parameters)
    assert result == []
