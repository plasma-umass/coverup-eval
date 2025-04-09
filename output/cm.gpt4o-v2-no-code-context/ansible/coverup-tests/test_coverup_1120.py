# file: lib/ansible/module_utils/common/parameters.py:639-689
# asked: {"lines": [643, 646, 647, 648, 650, 651, 653, 654, 655, 656, 657, 658, 659, 660, 661, 664, 665, 666, 667, 668, 670, 672, 673, 674, 675, 676, 677, 679, 680, 681, 682, 683, 684, 686, 687, 688, 689], "branches": [[642, 643], [645, 646], [647, 648], [647, 650], [650, 651], [650, 686], [651, 645], [651, 653], [653, 654], [653, 661], [655, 645], [655, 656], [658, 659], [658, 660], [661, 645], [661, 664], [665, 666], [665, 672], [668, 670], [668, 672], [672, 673], [672, 679], [673, 674], [673, 675], [676, 677], [676, 679], [679, 645], [679, 680], [682, 683], [682, 684], [687, 688], [687, 689]]}
# gained: {"lines": [646, 647, 650, 651, 653, 654, 655, 656, 657, 658, 660, 661, 664, 665, 666, 667, 668, 670, 672, 679, 680, 681, 682, 684, 686, 687, 689], "branches": [[645, 646], [647, 650], [650, 651], [650, 686], [651, 653], [653, 654], [653, 661], [655, 656], [658, 660], [661, 645], [661, 664], [665, 666], [665, 672], [668, 670], [668, 672], [672, 679], [679, 645], [679, 680], [682, 684], [687, 689]]}

import pytest
from ansible.module_utils.common.parameters import _validate_argument_values, AnsibleValidationErrorMultiple, ArgumentValueError, ArgumentTypeError
from ansible.module_utils._text import to_native
from collections.abc import Sequence
from ansible.module_utils.six import binary_type, text_type
from ansible.module_utils.common._collections_compat import KeysView

def test_validate_argument_values_no_errors():
    argument_spec = {
        'param1': {'choices': ['a', 'b', 'c']},
        'param2': {'choices': [1, 2, 3]},
    }
    parameters = {
        'param1': 'a',
        'param2': 2,
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert not errors.errors

def test_validate_argument_values_with_errors():
    argument_spec = {
        'param1': {'choices': ['a', 'b', 'c']},
        'param2': {'choices': [1, 2, 3]},
    }
    parameters = {
        'param1': 'd',
        'param2': 4,
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 2
    assert isinstance(errors.errors[0], ArgumentValueError)
    assert isinstance(errors.errors[1], ArgumentValueError)

def test_validate_argument_values_with_list():
    argument_spec = {
        'param1': {'choices': ['a', 'b', 'c'], 'type': 'list'},
    }
    parameters = {
        'param1': ['a', 'd'],
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 1
    assert isinstance(errors.errors[0], ArgumentValueError)

def test_validate_argument_values_non_iterable_choices():
    argument_spec = {
        'param1': {'choices': 123},
    }
    parameters = {
        'param1': 'a',
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 1
    assert isinstance(errors.errors[0], ArgumentTypeError)

def test_validate_argument_values_bool_conversion():
    argument_spec = {
        'param1': {'choices': [True, False]},
    }
    parameters = {
        'param1': 'False',
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert not errors.errors

def test_validate_argument_values_bool_conversion_no_match():
    argument_spec = {
        'param1': {'choices': [True]},
    }
    parameters = {
        'param1': 'False',
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 1
    assert isinstance(errors.errors[0], ArgumentValueError)
