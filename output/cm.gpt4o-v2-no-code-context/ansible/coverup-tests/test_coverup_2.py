# file: lib/ansible/module_utils/common/parameters.py:692-790
# asked: {"lines": [692, 698, 699, 701, 702, 704, 705, 707, 708, 710, 711, 712, 713, 714, 715, 716, 717, 719, 720, 721, 724, 727, 728, 730, 732, 733, 735, 736, 737, 740, 741, 742, 743, 745, 746, 747, 748, 749, 750, 751, 753, 754, 756, 757, 758, 759, 761, 762, 764, 765, 766, 767, 769, 771, 772, 773, 774, 776, 777, 779, 780, 781, 782, 783, 785, 788, 790], "branches": [[698, 699], [698, 701], [701, 702], [701, 704], [704, 705], [704, 707], [707, 708], [707, 710], [710, 0], [710, 711], [712, 710], [712, 713], [714, 715], [714, 720], [715, 716], [715, 719], [716, 717], [716, 724], [720, 721], [720, 724], [727, 728], [727, 730], [732, 733], [732, 790], [735, 736], [735, 740], [741, 742], [741, 743], [753, 754], [753, 756], [779, 780], [779, 785]]}
# gained: {"lines": [692, 698, 699, 701, 704, 707, 710, 711, 712, 713, 714, 715, 716, 720, 724, 727, 728, 730, 732, 733, 735, 740, 741, 742, 743, 745, 746, 747, 748, 753, 756, 757, 761, 762, 764, 765, 769, 771, 772, 776, 777, 779, 780, 781, 785, 788, 790], "branches": [[698, 699], [698, 701], [701, 704], [704, 707], [707, 710], [710, 0], [710, 711], [712, 710], [712, 713], [714, 715], [714, 720], [715, 716], [716, 724], [720, 724], [727, 728], [727, 730], [732, 733], [732, 790], [735, 740], [741, 742], [741, 743], [753, 756], [779, 780], [779, 785]]}

import pytest
from ansible.module_utils.common.parameters import _validate_sub_spec, AnsibleValidationErrorMultiple, SubParameterTypeError, AliasError, NoLogError, MutuallyExclusiveError, RequiredError
from ansible.module_utils._text import to_native
from collections.abc import Sequence
from ansible.module_utils.six import string_types

def test_validate_sub_spec(monkeypatch):
    # Mocking the dependencies
    def mock_set_fallbacks(sub_spec, sub_parameters):
        return set()

    def mock_handle_aliases(sub_spec, sub_parameters, alias_warnings, alias_deprecations):
        return {}

    def mock_list_no_log_values(sub_spec, sub_parameters):
        return set()

    def mock_get_legal_inputs(sub_spec, sub_parameters, options_aliases):
        return set(sub_spec.keys())

    def mock_get_unsupported_parameters(sub_spec, sub_parameters, legal_inputs, options_context):
        return set()

    def mock_check_mutually_exclusive(mutually_exclusive, sub_parameters, options_context):
        pass

    def mock_set_defaults(sub_spec, sub_parameters, apply_defaults=True):
        return set()

    def mock_check_required_arguments(sub_spec, sub_parameters, options_context):
        pass

    def mock_validate_argument_types(sub_spec, sub_parameters, new_prefix, options_context, errors=None):
        pass

    def mock_validate_argument_values(sub_spec, sub_parameters, options_context, errors=None):
        pass

    def mock_additional_check_func(attr, sub_parameters, options_context):
        pass

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
    monkeypatch.setattr('ansible.module_utils.common.parameters._ADDITIONAL_CHECKS', [{'func': mock_additional_check_func, 'attr': 'attr', 'err': TypeError}])

    argument_spec = {
        'param1': {
            'type': 'dict',
            'options': {
                'subparam1': {'type': 'str'},
                'subparam2': {'type': 'int'}
            },
            'apply_defaults': True
        },
        'param2': {
            'type': 'list',
            'elements': 'dict',
            'options': {
                'subparam3': {'type': 'str'},
                'subparam4': {'type': 'int'}
            }
        }
    }

    parameters = {
        'param1': {
            'subparam1': 'value1',
            'subparam2': 2
        },
        'param2': [
            {
                'subparam3': 'value3',
                'subparam4': 4
            }
        ]
    }

    errors = AnsibleValidationErrorMultiple()
    no_log_values = set()
    unsupported_parameters = set()

    _validate_sub_spec(argument_spec, parameters, errors=errors, no_log_values=no_log_values, unsupported_parameters=unsupported_parameters)

    assert not errors.errors
    assert no_log_values == set()
    assert unsupported_parameters == set()
