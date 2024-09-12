# file: lib/ansible/module_utils/common/parameters.py:245-296
# asked: {"lines": [], "branches": [[268, 267], [289, 291], [291, 267], [293, 292]]}
# gained: {"lines": [], "branches": [[289, 291]]}

import pytest
from ansible.module_utils.common.parameters import _list_deprecations
from ansible.module_utils.common._collections_compat import Mapping

class MockMapping(Mapping):
    def __init__(self, **kwargs):
        self._store = kwargs

    def __getitem__(self, key):
        return self._store[key]

    def __iter__(self):
        return iter(self._store)

    def __len__(self):
        return len(self._store)

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
    expected = [{
        'msg': "Param 'param1' is deprecated. See the module docs for more information",
        'date': '2023-01-01',
        'collection_name': 'test_collection'
    }]
    result = _list_deprecations(argument_spec, parameters)
    assert result == expected

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
    expected = [{
        'msg': "Param 'param1' is deprecated. See the module docs for more information",
        'version': '2.9',
        'collection_name': 'test_collection'
    }]
    result = _list_deprecations(argument_spec, parameters)
    assert result == expected

def test_list_deprecations_with_sub_arguments(monkeypatch):
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
        'param1': MockMapping(subparam1='subvalue1')
    }
    expected = [{
        'msg': "Param 'param1[\"subparam1\"]' is deprecated. See the module docs for more information",
        'version': '2.9',
        'collection_name': 'test_collection'
    }]
    result = _list_deprecations(argument_spec, parameters)
    assert result == expected

def test_list_deprecations_with_sub_arguments_list(monkeypatch):
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
        'param1': [MockMapping(subparam1='subvalue1')]
    }
    expected = [{
        'msg': "Param 'param1[\"subparam1\"]' is deprecated. See the module docs for more information",
        'version': '2.9',
        'collection_name': 'test_collection'
    }]
    result = _list_deprecations(argument_spec, parameters)
    assert result == expected
