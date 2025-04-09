# file lib/ansible/module_utils/common/parameters.py:692-790
# lines [692, 698, 699, 701, 702, 704, 705, 707, 708, 710, 711, 712, 713, 714, 715, 716, 717, 719, 720, 721, 724, 727, 728, 730, 732, 733, 735, 736, 737, 740, 741, 742, 743, 745, 746, 747, 748, 749, 750, 751, 753, 754, 756, 757, 758, 759, 761, 762, 764, 765, 766, 767, 769, 771, 772, 773, 774, 776, 777, 779, 780, 781, 782, 783, 785, 788, 790]
# branches ['698->699', '698->701', '701->702', '701->704', '704->705', '704->707', '707->708', '707->710', '710->exit', '710->711', '712->710', '712->713', '714->715', '714->720', '715->716', '715->719', '716->717', '716->724', '720->721', '720->724', '727->728', '727->730', '732->733', '732->790', '735->736', '735->740', '741->742', '741->743', '753->754', '753->756', '779->780', '779->785']

import pytest
from ansible.module_utils.common.parameters import _validate_sub_spec, AnsibleValidationErrorMultiple, SubParameterTypeError, AliasError, NoLogError, MutuallyExclusiveError, RequiredError
from ansible.module_utils._text import to_native
from collections.abc import Sequence
from ansible.module_utils.six import string_types

def test_validate_sub_spec(mocker):
    # Mocking the dependencies
    mocker.patch('ansible.module_utils.common.parameters.set_fallbacks', return_value=set())
    mocker.patch('ansible.module_utils.common.parameters._handle_aliases', return_value={})
    mocker.patch('ansible.module_utils.common.parameters._list_no_log_values', return_value=set())
    mocker.patch('ansible.module_utils.common.parameters._get_legal_inputs', return_value=set())
    mocker.patch('ansible.module_utils.common.parameters._get_unsupported_parameters', return_value=set())
    mocker.patch('ansible.module_utils.common.parameters.check_mutually_exclusive')
    mocker.patch('ansible.module_utils.common.parameters._set_defaults', return_value=set())
    mocker.patch('ansible.module_utils.common.parameters.check_required_arguments')
    mocker.patch('ansible.module_utils.common.parameters._validate_argument_types')
    mocker.patch('ansible.module_utils.common.parameters._validate_argument_values')
    mocker.patch('ansible.module_utils.common.parameters.warn')
    
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
    assert 'param1' in parameters
    assert 'param2' in parameters
    assert 'subparam1' in parameters['param1']
    assert 'subparam2' in parameters['param1']
    assert isinstance(parameters['param2'], list)
    assert 'subparam3' in parameters['param2'][0]
    assert 'subparam4' in parameters['param2'][0]
