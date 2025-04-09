# file: lib/ansible/module_utils/common/parameters.py:692-790
# asked: {"lines": [702, 705, 708, 717, 719, 721, 736, 737, 749, 750, 751, 754, 758, 759, 766, 767, 773, 774, 782, 783], "branches": [[701, 702], [704, 705], [707, 708], [715, 719], [716, 717], [720, 721], [735, 736], [753, 754]]}
# gained: {"lines": [749, 750, 751, 758, 759, 766, 767, 773, 774, 782, 783], "branches": []}

import pytest
from ansible.module_utils.common.parameters import _validate_sub_spec, AnsibleValidationErrorMultiple, SubParameterTypeError, AliasError, NoLogError, MutuallyExclusiveError, RequiredError
from ansible.module_utils._text import to_native
from collections.abc import Sequence
from ansible.module_utils.six import string_types

def test_validate_sub_spec(monkeypatch):
    def mock_set_fallbacks(sub_spec, sub_parameters):
        return set()

    def mock_handle_aliases(sub_spec, sub_parameters, alias_warnings, alias_deprecations):
        if 'invalid' in sub_parameters:
            raise TypeError("Invalid alias")
        return {}

    def mock_list_no_log_values(sub_spec, sub_parameters):
        if 'invalid' in sub_parameters:
            raise TypeError("Invalid no_log value")
        return set()

    def mock_get_legal_inputs(sub_spec, sub_parameters, options_aliases):
        return set(sub_spec.keys())

    def mock_get_unsupported_parameters(sub_spec, sub_parameters, legal_inputs, options_context):
        return set()

    def mock_check_mutually_exclusive(mutually_exclusive, sub_parameters, options_context):
        if 'subparam1' in sub_parameters and 'subparam2' in sub_parameters:
            raise TypeError("Mutually exclusive parameters")

    def mock_set_defaults(sub_spec, sub_parameters, apply_defaults=True):
        return set()

    def mock_check_required_arguments(sub_spec, sub_parameters, options_context):
        if 'required_param' not in sub_parameters:
            raise TypeError("Missing required parameter")

    def mock_validate_argument_types(sub_spec, sub_parameters, new_prefix, options_context, errors=None):
        pass

    def mock_validate_argument_values(sub_spec, sub_parameters, options_context, errors=None):
        pass

    def mock_additional_check(attr, sub_parameters, options_context):
        if 'invalid_check' in sub_parameters:
            raise TypeError("Invalid additional check")

    monkeypatch.setattr('ansible.module_utils.common.parameters.set_fallbacks', mock_set_fallbacks)
    monkeypatch.setattr('ansible.module_utils.common.parameters._handle_aliases', mock_handle_aliases)
    monkeypatch.setattr('ansible.module_utils.common.parameters._list_no_log_values', mock_list_no_log_values)
    monkeypatch.setattr('ansible.module_utils.common.parameters._get_legal_inputs', mock_get_legal_inputs)
    monkeypatch.setattr('ansible.module_utils.common.parameters._get_unsupported_parameters', mock_get_unsupported_parameters)
    monkeypatch.setattr('ansible.module_utils.common.parameters.check_mutually_exclusive', mock_check_mutually_exclusive)
    monkeypatch.setattr('ansible.module_utils.common.parameters._set_defaults', mock_set_defaults)
    monkeypatch.setattr('ansible.module_utils.common.parameters.check_required_arguments', mock_check_required_arguments)
    monkeypatch.setattr('ansible.module_utils.common.parameters._validate_argument_types', mock_validate_argument_types)
    monkeypatch.setattr('ansible.module_utils.common.parameters._validate_argument_values', mock_validate_argument_values)
    monkeypatch.setattr('ansible.module_utils.common.parameters._ADDITIONAL_CHECKS', [{'func': mock_additional_check, 'attr': 'attr', 'err': TypeError}])

    argument_spec = {
        'param1': {
            'type': 'dict',
            'options': {
                'subparam1': {'type': 'str'},
                'subparam2': {'type': 'int'},
                'required_param': {'type': 'str'}
            },
            'apply_defaults': True,
            'mutually_exclusive': ['subparam1', 'subparam2']
        }
    }
    parameters = {
        'param1': {
            'subparam1': 'value1',
            'subparam2': 'value2',
            'invalid': 'value',
            'invalid_check': 'value'
        }
    }

    errors = AnsibleValidationErrorMultiple()
    no_log_values = set()
    unsupported_parameters = set()

    _validate_sub_spec(argument_spec, parameters, errors=errors, no_log_values=no_log_values, unsupported_parameters=unsupported_parameters)

    assert 'param1' in parameters
    assert 'subparam1' in parameters['param1']
    assert errors.errors != []
    assert no_log_values == set()
    assert unsupported_parameters == set()
