# file: lib/ansible/module_utils/common/parameters.py:245-296
# asked: {"lines": [], "branches": [[268, 267], [291, 267], [293, 292]]}
# gained: {"lines": [], "branches": [[268, 267], [293, 292]]}

import pytest
from ansible.module_utils.common.parameters import _list_deprecations
from ansible.module_utils.common._collections_compat import Mapping

class TestListDeprecations:
    def test_no_parameters_in_argument_spec(self):
        argument_spec = {
            'param1': {
                'removed_at_date': '2023-01-01',
                'removed_from_collection': 'test_collection'
            }
        }
        parameters = {}
        expected = []
        result = _list_deprecations(argument_spec, parameters)
        assert result == expected

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
            'param1': {
                'removed_in_version': '2.9',
                'removed_from_collection': 'test_collection'
            }
        }
        parameters = {
            'param1': 'value1'
        }
        expected = [{
            'msg': "Param 'param1' is deprecated. See the module docs for more information",
            'version': '2.9',
            'collection_name': 'test_collection'
        }]
        result = _list_deprecations(argument_spec, parameters)
        assert result == expected

    def test_sub_argument_spec(self):
        argument_spec = {
            'param1': {
                'options': {
                    'subparam1': {
                        'removed_in_version': '2.9',
                        'removed_from_collection': 'test_collection'
                    }
                }
            }
        }
        parameters = {
            'param1': {
                'subparam1': 'value1'
            }
        }
        expected = [{
            'msg': "Param 'param1[\"subparam1\"]' is deprecated. See the module docs for more information",
            'version': '2.9',
            'collection_name': 'test_collection'
        }]
        result = _list_deprecations(argument_spec, parameters)
        assert result == expected

    def test_sub_argument_spec_with_list(self):
        argument_spec = {
            'param1': {
                'options': {
                    'subparam1': {
                        'removed_in_version': '2.9',
                        'removed_from_collection': 'test_collection'
                    }
                }
            }
        }
        parameters = {
            'param1': [
                {
                    'subparam1': 'value1'
                }
            ]
        }
        expected = [{
            'msg': "Param 'param1[\"subparam1\"]' is deprecated. See the module docs for more information",
            'version': '2.9',
            'collection_name': 'test_collection'
        }]
        result = _list_deprecations(argument_spec, parameters)
        assert result == expected

    def test_sub_argument_spec_with_non_mapping_list(self):
        argument_spec = {
            'param1': {
                'options': {
                    'subparam1': {
                        'removed_in_version': '2.9',
                        'removed_from_collection': 'test_collection'
                    }
                }
            }
        }
        parameters = {
            'param1': [
                'not_a_mapping'
            ]
        }
        expected = []
        result = _list_deprecations(argument_spec, parameters)
        assert result == expected
