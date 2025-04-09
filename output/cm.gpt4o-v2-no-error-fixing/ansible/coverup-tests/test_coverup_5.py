# file: lib/ansible/module_utils/common/parameters.py:639-689
# asked: {"lines": [639, 642, 643, 645, 646, 647, 648, 650, 651, 653, 654, 655, 656, 657, 658, 659, 660, 661, 664, 665, 666, 667, 668, 670, 672, 673, 674, 675, 676, 677, 679, 680, 681, 682, 683, 684, 686, 687, 688, 689], "branches": [[642, 643], [642, 645], [645, 0], [645, 646], [647, 648], [647, 650], [650, 651], [650, 686], [651, 645], [651, 653], [653, 654], [653, 661], [655, 645], [655, 656], [658, 659], [658, 660], [661, 645], [661, 664], [665, 666], [665, 672], [668, 670], [668, 672], [672, 673], [672, 679], [673, 674], [673, 675], [676, 677], [676, 679], [679, 645], [679, 680], [682, 683], [682, 684], [687, 688], [687, 689]]}
# gained: {"lines": [639, 642, 645, 646, 647, 648, 650, 651, 653, 654, 655, 656, 657, 658, 660, 661, 664, 665, 672, 673, 674, 675, 676, 677, 679, 680, 681, 682, 684, 686, 687, 689], "branches": [[642, 645], [645, 0], [645, 646], [647, 648], [647, 650], [650, 651], [650, 686], [651, 653], [653, 654], [653, 661], [655, 645], [655, 656], [658, 660], [661, 645], [661, 664], [665, 672], [672, 673], [672, 679], [673, 674], [676, 677], [679, 645], [679, 680], [682, 684], [687, 689]]}

import pytest
from ansible.module_utils.common.parameters import _validate_argument_values
from ansible.module_utils.errors import AnsibleValidationErrorMultiple, ArgumentTypeError, ArgumentValueError
from ansible.module_utils.parsing.convert_bool import BOOLEANS_FALSE, BOOLEANS_TRUE
from ansible.module_utils.common._collections_compat import KeysView, Sequence
from ansible.module_utils.six import binary_type, text_type

def test_validate_argument_values_no_choices():
    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'int'}
    }
    parameters = {
        'param1': 'value1',
        'param2': 10
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 0

def test_validate_argument_values_with_choices():
    argument_spec = {
        'param1': {'type': 'str', 'choices': ['value1', 'value2']},
        'param2': {'type': 'int', 'choices': [10, 20]}
    }
    parameters = {
        'param1': 'value1',
        'param2': 10
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 0

def test_validate_argument_values_invalid_choice():
    argument_spec = {
        'param1': {'type': 'str', 'choices': ['value1', 'value2']},
        'param2': {'type': 'int', 'choices': [10, 20]}
    }
    parameters = {
        'param1': 'invalid_value',
        'param2': 10
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 1
    assert isinstance(errors.errors[0], ArgumentValueError)

def test_validate_argument_values_list_choice():
    argument_spec = {
        'param1': {'type': 'list', 'choices': ['value1', 'value2', 'value3']}
    }
    parameters = {
        'param1': ['value1', 'value3']
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 0

def test_validate_argument_values_list_invalid_choice():
    argument_spec = {
        'param1': {'type': 'list', 'choices': ['value1', 'value2', 'value3']}
    }
    parameters = {
        'param1': ['value1', 'invalid_value']
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 1
    assert isinstance(errors.errors[0], ArgumentValueError)

def test_validate_argument_values_bool_conversion():
    argument_spec = {
        'param1': {'type': 'str', 'choices': ['true', 'false']}
    }
    parameters = {
        'param1': 'True'
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 0

def test_validate_argument_values_non_iterable_choices():
    argument_spec = {
        'param1': {'type': 'str', 'choices': 123}
    }
    parameters = {
        'param1': 'value1'
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 1
    assert isinstance(errors.errors[0], ArgumentTypeError)
