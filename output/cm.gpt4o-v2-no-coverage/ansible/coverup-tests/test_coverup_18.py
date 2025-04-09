# file: lib/ansible/module_utils/common/parameters.py:245-296
# asked: {"lines": [245, 266, 267, 268, 269, 270, 272, 273, 274, 275, 276, 277, 279, 280, 281, 282, 283, 286, 287, 288, 289, 290, 291, 292, 293, 294, 296], "branches": [[267, 268], [267, 296], [268, 267], [268, 269], [269, 270], [269, 272], [273, 274], [273, 279], [279, 280], [279, 286], [287, 267], [287, 288], [289, 290], [289, 291], [291, 267], [291, 292], [292, 267], [292, 293], [293, 292], [293, 294]]}
# gained: {"lines": [245, 266, 267, 268, 269, 270, 272, 273, 274, 275, 276, 277, 279, 280, 281, 282, 283, 286, 287, 288, 289, 290, 291, 292, 293, 294, 296], "branches": [[267, 268], [267, 296], [268, 269], [269, 270], [269, 272], [273, 274], [273, 279], [279, 280], [279, 286], [287, 267], [287, 288], [289, 290], [289, 291], [291, 292], [292, 267], [292, 293], [293, 294]]}

import pytest
from ansible.module_utils.common.parameters import _list_deprecations
from ansible.module_utils.common._collections_compat import Mapping

class MockMapping(Mapping):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

def test_list_deprecations_no_deprecations():
    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'int'}
    }
    parameters = {
        'param1': 'value1',
        'param2': 2
    }
    result = _list_deprecations(argument_spec, parameters)
    assert result == []

def test_list_deprecations_with_removed_at_date():
    argument_spec = {
        'param1': {'type': 'str', 'removed_at_date': '2023-01-01'}
    }
    parameters = {
        'param1': 'value1'
    }
    result = _list_deprecations(argument_spec, parameters)
    assert result == [{
        'msg': "Param 'param1' is deprecated. See the module docs for more information",
        'date': '2023-01-01',
        'collection_name': None
    }]

def test_list_deprecations_with_removed_in_version():
    argument_spec = {
        'param1': {'type': 'str', 'removed_in_version': '2.9'}
    }
    parameters = {
        'param1': 'value1'
    }
    result = _list_deprecations(argument_spec, parameters)
    assert result == [{
        'msg': "Param 'param1' is deprecated. See the module docs for more information",
        'version': '2.9',
        'collection_name': None
    }]

def test_list_deprecations_with_sub_arguments():
    argument_spec = {
        'param1': {
            'type': 'dict',
            'options': {
                'subparam1': {'type': 'str', 'removed_in_version': '2.9'}
            }
        }
    }
    parameters = {
        'param1': {
            'subparam1': 'value1'
        }
    }
    result = _list_deprecations(argument_spec, parameters)
    assert result == [{
        'msg': "Param 'param1[\"subparam1\"]' is deprecated. See the module docs for more information",
        'version': '2.9',
        'collection_name': None
    }]

def test_list_deprecations_with_sub_arguments_list():
    argument_spec = {
        'param1': {
            'type': 'list',
            'options': {
                'subparam1': {'type': 'str', 'removed_in_version': '2.9'}
            }
        }
    }
    parameters = {
        'param1': [
            {'subparam1': 'value1'}
        ]
    }
    result = _list_deprecations(argument_spec, parameters)
    assert result == [{
        'msg': "Param 'param1[\"subparam1\"]' is deprecated. See the module docs for more information",
        'version': '2.9',
        'collection_name': None
    }]
