# file: lib/ansible/module_utils/common/parameters.py:245-296
# asked: {"lines": [], "branches": [[268, 267], [291, 267], [293, 292]]}
# gained: {"lines": [], "branches": [[268, 267], [291, 267]]}

import pytest
from ansible.module_utils.common.parameters import _list_deprecations
from ansible.module_utils.common._collections_compat import Mapping

class TestListDeprecations:
    
    def test_deprecation_with_removed_at_date(self):
        argument_spec = {
            'param1': {
                'removed_at_date': '2023-01-01',
                'removed_from_collection': 'test_collection'
            }
        }
        parameters = {
            'param1': 'value1'
        }
        expected = [{
            'msg': "Param 'param1' is deprecated. See the module docs for more information",
            'date': '2023-01-01',
            'collection_name': 'test_collection'
        }]
        result = _list_deprecations(argument_spec, parameters)
        assert result == expected

    def test_deprecation_with_removed_in_version(self):
        argument_spec = {
            'param2': {
                'removed_in_version': '2.9',
                'removed_from_collection': 'test_collection'
            }
        }
        parameters = {
            'param2': 'value2'
        }
        expected = [{
            'msg': "Param 'param2' is deprecated. See the module docs for more information",
            'version': '2.9',
            'collection_name': 'test_collection'
        }]
        result = _list_deprecations(argument_spec, parameters)
        assert result == expected

    def test_deprecation_with_sub_arguments(self):
        argument_spec = {
            'param3': {
                'options': {
                    'subparam1': {
                        'removed_in_version': '2.9',
                        'removed_from_collection': 'test_collection'
                    }
                }
            }
        }
        parameters = {
            'param3': {
                'subparam1': 'value3'
            }
        }
        expected = [{
            'msg': "Param 'param3[\"subparam1\"]' is deprecated. See the module docs for more information",
            'version': '2.9',
            'collection_name': 'test_collection'
        }]
        result = _list_deprecations(argument_spec, parameters)
        assert result == expected

    def test_deprecation_with_sub_arguments_list(self):
        argument_spec = {
            'param4': {
                'options': {
                    'subparam2': {
                        'removed_in_version': '2.9',
                        'removed_from_collection': 'test_collection'
                    }
                }
            }
        }
        parameters = {
            'param4': [{
                'subparam2': 'value4'
            }]
        }
        expected = [{
            'msg': "Param 'param4[\"subparam2\"]' is deprecated. See the module docs for more information",
            'version': '2.9',
            'collection_name': 'test_collection'
        }]
        result = _list_deprecations(argument_spec, parameters)
        assert result == expected

    def test_no_deprecation(self):
        argument_spec = {
            'param5': {
                'type': 'str'
            }
        }
        parameters = {
            'param5': 'value5'
        }
        expected = []
        result = _list_deprecations(argument_spec, parameters)
        assert result == expected

    def test_no_parameters(self):
        argument_spec = {
            'param6': {
                'removed_in_version': '2.9',
                'removed_from_collection': 'test_collection'
            }
        }
        parameters = {}
        expected = []
        result = _list_deprecations(argument_spec, parameters)
        assert result == expected

    def test_sub_arguments_not_mapping(self):
        argument_spec = {
            'param7': {
                'options': {
                    'subparam3': {
                        'removed_in_version': '2.9',
                        'removed_from_collection': 'test_collection'
                    }
                }
            }
        }
        parameters = {
            'param7': 'not_a_mapping'
        }
        expected = []
        result = _list_deprecations(argument_spec, parameters)
        assert result == expected
