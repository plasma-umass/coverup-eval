# file: lib/ansible/module_utils/common/parameters.py:802-824
# asked: {"lines": [802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 814, 815, 816, 817, 818, 820, 821, 822, 824], "branches": [[804, 805], [804, 824], [809, 804], [809, 810], [810, 811], [810, 815], [811, 812], [811, 814], [820, 821], [820, 822]]}
# gained: {"lines": [802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 814, 815, 816, 817, 818, 820, 821, 822, 824], "branches": [[804, 805], [804, 824], [809, 804], [809, 810], [810, 811], [810, 815], [811, 812], [811, 814], [820, 821], [820, 822]]}

import pytest
from ansible.module_utils.common.parameters import set_fallbacks
from ansible.module_utils.errors import AnsibleFallbackNotFound

def test_set_fallbacks_no_fallback():
    argument_spec = {
        'param1': {'fallback': (None,)},
        'param2': {'fallback': (None,)}
    }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {}
    assert no_log_values == set()

def test_set_fallbacks_with_fallback():
    def fallback_func():
        return 'fallback_value'
    
    argument_spec = {
        'param1': {'fallback': (fallback_func,)},
        'param2': {'fallback': (None,)}
    }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'param1': 'fallback_value'}
    assert no_log_values == set()

def test_set_fallbacks_with_no_log():
    def fallback_func():
        return 'fallback_value'
    
    argument_spec = {
        'param1': {'fallback': (fallback_func,), 'no_log': True},
        'param2': {'fallback': (None,)}
    }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'param1': 'fallback_value'}
    assert no_log_values == {'fallback_value'}

def test_set_fallbacks_with_args_kwargs():
    def fallback_func(arg1, kwarg1=None):
        return f'{arg1}_{kwarg1}'
    
    argument_spec = {
        'param1': {'fallback': (fallback_func, ['arg1'], {'kwarg1': 'kwarg1'})},
        'param2': {'fallback': (None,)}
    }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {'param1': 'arg1_kwarg1'}
    assert no_log_values == set()

def test_set_fallbacks_fallback_not_found():
    def fallback_func():
        raise AnsibleFallbackNotFound
    
    argument_spec = {
        'param1': {'fallback': (fallback_func,)},
        'param2': {'fallback': (None,)}
    }
    parameters = {}
    no_log_values = set_fallbacks(argument_spec, parameters)
    assert parameters == {}
    assert no_log_values == set()
