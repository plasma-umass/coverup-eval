# file: lib/ansible/module_utils/common/parameters.py:639-689
# asked: {"lines": [643, 659, 666, 667, 668, 670, 683, 688], "branches": [[642, 643], [651, 645], [658, 659], [665, 666], [668, 670], [668, 672], [673, 675], [676, 679], [682, 683], [687, 688]]}
# gained: {"lines": [666, 667, 668, 670], "branches": [[665, 666], [668, 670]]}

import pytest
from ansible.module_utils.common.parameters import _validate_argument_values
from ansible.module_utils.errors import AnsibleValidationErrorMultiple, ArgumentValueError, ArgumentTypeError
from ansible.module_utils.parsing.convert_bool import BOOLEANS_FALSE, BOOLEANS_TRUE

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
    assert len(errors.errors) == 0

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

def test_validate_argument_values_list_type():
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

def test_validate_argument_values_bool_false():
    argument_spec = {
        'param1': {'choices': ['no', 'yes']},
    }
    parameters = {
        'param1': 'False',
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 0
    assert parameters['param1'] == 'no'

def test_validate_argument_values_bool_true():
    argument_spec = {
        'param1': {'choices': ['no', 'yes']},
    }
    parameters = {
        'param1': 'True',
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_argument_values(argument_spec, parameters, errors=errors)
    assert len(errors.errors) == 0
    assert parameters['param1'] == 'yes'

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
