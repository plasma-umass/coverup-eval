# file lib/ansible/module_utils/common/parameters.py:639-689
# lines [643, 646, 647, 648, 650, 651, 653, 654, 655, 656, 657, 658, 659, 660, 661, 664, 665, 666, 667, 668, 670, 672, 673, 674, 675, 676, 677, 679, 680, 681, 682, 683, 684, 686, 687, 688, 689]
# branches ['642->643', '645->646', '647->648', '647->650', '650->651', '650->686', '651->645', '651->653', '653->654', '653->661', '655->645', '655->656', '658->659', '658->660', '661->645', '661->664', '665->666', '665->672', '668->670', '668->672', '672->673', '672->679', '673->674', '673->675', '676->677', '676->679', '679->645', '679->680', '682->683', '682->684', '687->688', '687->689']

import pytest
from ansible.module_utils.common.parameters import _validate_argument_values, AnsibleValidationErrorMultiple, ArgumentValueError, ArgumentTypeError
from ansible.module_utils._text import to_native
from collections.abc import Sequence
from ansible.module_utils.six import binary_type, text_type

def test_validate_argument_values(mocker):
    argument_spec = {
        'param1': {'choices': ['choice1', 'choice2']},
        'param2': {'choices': ['True', 'False']},
        'param3': {'choices': 'not_iterable'},
    }
    parameters = {
        'param1': 'invalid_choice',
        'param2': 'False',
        'param3': 'some_value',
    }
    options_context = ['context1', 'context2']

    errors = AnsibleValidationErrorMultiple()

    # Mock lenient_lowercase and BOOLEANS_FALSE/BOOLEANS_TRUE
    mocker.patch('ansible.module_utils.common.parameters.lenient_lowercase', return_value=['true', 'false'])
    mocker.patch('ansible.module_utils.common.parameters.BOOLEANS_FALSE', {'false'})
    mocker.patch('ansible.module_utils.common.parameters.BOOLEANS_TRUE', {'true'})

    _validate_argument_values(argument_spec, parameters, options_context, errors)

    error_messages = [str(error) for error in errors]
    
    assert len(error_messages) == 2
    assert any("value of param1 must be one of: choice1, choice2, got: invalid_choice" in msg for msg in error_messages)
    assert any("internal error: choices for argument param3 are not iterable: not_iterable" in msg for msg in error_messages)
