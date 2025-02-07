# file: lib/ansible/module_utils/common/parameters.py:802-824
# asked: {"lines": [810, 811, 812, 814, 815, 816, 817, 818, 820, 821, 822], "branches": [[809, 810], [810, 811], [810, 815], [811, 812], [811, 814], [820, 821], [820, 822]]}
# gained: {"lines": [810, 811, 812, 815, 816, 817, 818, 820, 821, 822], "branches": [[809, 810], [810, 811], [810, 815], [811, 812], [820, 821]]}

import pytest
from ansible.module_utils.common.parameters import set_fallbacks
from ansible.module_utils.errors import AnsibleFallbackNotFound

def test_set_fallbacks_with_fallback_strategy(monkeypatch):
    def mock_fallback_strategy(*args, **kwargs):
        return "fallback_value"

    argument_spec = {
        'param1': {
            'fallback': (mock_fallback_strategy, {'key': 'value'}),
            'no_log': True
        }
    }
    parameters = {}

    no_log_values = set_fallbacks(argument_spec, parameters)

    assert parameters['param1'] == "fallback_value"
    assert "fallback_value" in no_log_values

def test_set_fallbacks_without_fallback_strategy():
    argument_spec = {
        'param1': {
            'fallback': (None,)
        }
    }
    parameters = {}

    no_log_values = set_fallbacks(argument_spec, parameters)

    assert 'param1' not in parameters
    assert len(no_log_values) == 0

def test_set_fallbacks_with_exception(monkeypatch):
    def mock_fallback_strategy(*args, **kwargs):
        raise AnsibleFallbackNotFound

    argument_spec = {
        'param1': {
            'fallback': (mock_fallback_strategy,)
        }
    }
    parameters = {}

    no_log_values = set_fallbacks(argument_spec, parameters)

    assert 'param1' not in parameters
    assert len(no_log_values) == 0
