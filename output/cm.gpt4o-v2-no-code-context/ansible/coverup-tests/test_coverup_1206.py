# file: lib/ansible/module_utils/common/parameters.py:245-296
# asked: {"lines": [], "branches": [[293, 292]]}
# gained: {"lines": [], "branches": [[293, 292]]}

import pytest
from ansible.module_utils.common.parameters import _list_deprecations
from collections.abc import Mapping

def test_list_deprecations_with_sub_arguments(monkeypatch):
    argument_spec = {
        'param1': {
            'removed_in_version': '2.9',
            'options': {
                'subparam1': {
                    'removed_at_date': '2023-01-01'
                },
                'subparam2': {
                    'removed_in_version': '3.0'
                }
            }
        }
    }
    parameters = {
        'param1': {
            'subparam1': 'value1',
            'subparam2': 'value2'
        }
    }

    deprecations = _list_deprecations(argument_spec, parameters)
    
    assert len(deprecations) == 3
    assert deprecations[0]['msg'] == "Param 'param1' is deprecated. See the module docs for more information"
    assert deprecations[0]['version'] == '2.9'
    assert deprecations[1]['msg'] == "Param 'param1[\"subparam1\"]' is deprecated. See the module docs for more information"
    assert deprecations[1]['date'] == '2023-01-01'
    assert deprecations[2]['msg'] == "Param 'param1[\"subparam2\"]' is deprecated. See the module docs for more information"
    assert deprecations[2]['version'] == '3.0'

def test_list_deprecations_with_empty_sub_arguments(monkeypatch):
    argument_spec = {
        'param1': {
            'removed_in_version': '2.9',
            'options': {
                'subparam1': {
                    'removed_at_date': '2023-01-01'
                }
            }
        }
    }
    parameters = {
        'param1': {}
    }

    deprecations = _list_deprecations(argument_spec, parameters)
    
    assert len(deprecations) == 1
    assert deprecations[0]['msg'] == "Param 'param1' is deprecated. See the module docs for more information"
    assert deprecations[0]['version'] == '2.9'

def test_list_deprecations_with_non_mapping_sub_arguments(monkeypatch):
    argument_spec = {
        'param1': {
            'removed_in_version': '2.9',
            'options': {
                'subparam1': {
                    'removed_at_date': '2023-01-01'
                }
            }
        }
    }
    parameters = {
        'param1': ['not_a_mapping']
    }

    deprecations = _list_deprecations(argument_spec, parameters)
    
    assert len(deprecations) == 1
    assert deprecations[0]['msg'] == "Param 'param1' is deprecated. See the module docs for more information"
    assert deprecations[0]['version'] == '2.9'
