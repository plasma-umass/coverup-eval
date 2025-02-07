# file: lib/ansible/module_utils/common/parameters.py:188-242
# asked: {"lines": [], "branches": [[222, 221], [238, 240]]}
# gained: {"lines": [], "branches": [[222, 221], [238, 240]]}

import pytest
from ansible.module_utils.common.parameters import _handle_aliases

def test_handle_aliases_deprecated_aliases():
    argument_spec = {
        'param1': {
            'deprecated_aliases': [{'name': 'old_param1', 'version': '2.0', 'collection_name': 'test'}],
            'aliases': ['alias1'],
            'default': None,
            'required': False
        }
    }
    parameters = {'old_param1': 'value1'}
    alias_deprecations = []

    _handle_aliases(argument_spec, parameters, alias_deprecations=alias_deprecations)

    assert alias_deprecations == [{'name': 'old_param1', 'version': '2.0', 'collection_name': 'test'}]

def test_handle_aliases_alias_warnings():
    argument_spec = {
        'param1': {
            'aliases': ['alias1'],
            'default': None,
            'required': False
        }
    }
    parameters = {'alias1': 'value1', 'param1': 'value2'}
    alias_warnings = []

    _handle_aliases(argument_spec, parameters, alias_warnings=alias_warnings)

    assert alias_warnings == [('param1', 'alias1')]
    assert parameters['param1'] == 'value1'

def test_handle_aliases_no_deprecated_aliases():
    argument_spec = {
        'param1': {
            'deprecated_aliases': [{'name': 'old_param1', 'version': '2.0', 'collection_name': 'test'}],
            'aliases': ['alias1'],
            'default': None,
            'required': False
        }
    }
    parameters = {}
    alias_deprecations = []

    _handle_aliases(argument_spec, parameters, alias_deprecations=alias_deprecations)

    assert alias_deprecations == []

def test_handle_aliases_no_alias_warnings():
    argument_spec = {
        'param1': {
            'aliases': ['alias1'],
            'default': None,
            'required': False
        }
    }
    parameters = {'alias1': 'value1'}
    alias_warnings = []

    _handle_aliases(argument_spec, parameters, alias_warnings=alias_warnings)

    assert alias_warnings == []
    assert parameters['param1'] == 'value1'
