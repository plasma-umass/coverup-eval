# file lib/ansible/module_utils/common/parameters.py:692-790
# lines [702, 705, 708, 717, 719, 721, 736, 737, 749, 750, 751, 754, 758, 759, 766, 767, 773, 774, 782, 783]
# branches ['701->702', '704->705', '707->708', '715->719', '716->717', '720->721', '735->736', '753->754']

import pytest
from ansible.module_utils.common.parameters import _validate_sub_spec, AnsibleValidationErrorMultiple, SubParameterTypeError, AliasError, NoLogError, MutuallyExclusiveError, RequiredError
from ansible.module_utils._text import to_native
from collections.abc import Sequence
from ansible.module_utils.six import string_types

def test_validate_sub_spec(mocker):
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
        'param1': None,
        'param2': [{'subparam3': 'value3', 'subparam4': 4}]
    }

    errors = AnsibleValidationErrorMultiple()
    no_log_values = set()
    unsupported_parameters = set()

    mocker.patch('ansible.module_utils.common.parameters.set_fallbacks', return_value=set())
    mocker.patch('ansible.module_utils.common.parameters._handle_aliases', side_effect=TypeError('alias error'))
    mocker.patch('ansible.module_utils.common.parameters._list_no_log_values', side_effect=TypeError('no log error'))
    mocker.patch('ansible.module_utils.common.parameters._get_legal_inputs', return_value={})
    mocker.patch('ansible.module_utils.common.parameters._get_unsupported_parameters', return_value=set())
    mocker.patch('ansible.module_utils.common.parameters.check_mutually_exclusive', side_effect=TypeError('mutually exclusive error'))
    mocker.patch('ansible.module_utils.common.parameters._set_defaults', return_value=set())
    mocker.patch('ansible.module_utils.common.parameters.check_required_arguments', side_effect=TypeError('required error'))
    mocker.patch('ansible.module_utils.common.parameters._validate_argument_types')
    mocker.patch('ansible.module_utils.common.parameters._validate_argument_values')
    mocker.patch('ansible.module_utils.common.parameters._ADDITIONAL_CHECKS', [{'func': mocker.Mock(side_effect=TypeError('additional check error')), 'attr': 'check_attr', 'err': lambda x: SubParameterTypeError(x)}])

    _validate_sub_spec(argument_spec, parameters, errors=errors, no_log_values=no_log_values, unsupported_parameters=unsupported_parameters)

    error_messages = [str(e) for e in errors]
    unique_error_messages = set(error_messages)
    assert len(unique_error_messages) == 5
    assert any(isinstance(e, AliasError) and 'alias error' in str(e) for e in errors)
    assert any(isinstance(e, NoLogError) and 'no log error' in str(e) for e in errors)
    assert any(isinstance(e, MutuallyExclusiveError) and 'mutually exclusive error' in str(e) for e in errors)
    assert any(isinstance(e, RequiredError) and 'required error' in str(e) for e in errors)
    assert any(isinstance(e, SubParameterTypeError) and 'additional check error' in str(e) for e in errors)
