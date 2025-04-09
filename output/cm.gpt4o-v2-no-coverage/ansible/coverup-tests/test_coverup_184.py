# file: lib/ansible/module_utils/common/arg_spec.py:94-140
# asked: {"lines": [94, 95, 96, 97, 98, 99, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 140], "branches": [[135, 0], [135, 136], [137, 138], [137, 140]]}
# gained: {"lines": [94, 95, 96, 97, 98, 99, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 140], "branches": [[135, 0], [135, 136], [137, 138], [137, 140]]}

import pytest
from ansible.module_utils.common.arg_spec import ArgumentSpecValidator

def test_argument_spec_validator_init():
    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'int', 'aliases': ['p2', 'param_two']},
    }
    mutually_exclusive = [['param1', 'param2']]
    required_together = [['param1', 'param2']]
    required_one_of = [['param1', 'param2']]
    required_if = [['param1', 'value1', ['param2']]]
    required_by = {'param1': ['param2']}

    validator = ArgumentSpecValidator(
        argument_spec,
        mutually_exclusive=mutually_exclusive,
        required_together=required_together,
        required_one_of=required_one_of,
        required_if=required_if,
        required_by=required_by
    )

    assert validator._mutually_exclusive == mutually_exclusive
    assert validator._required_together == required_together
    assert validator._required_one_of == required_one_of
    assert validator._required_if == required_if
    assert validator._required_by == required_by
    assert validator.argument_spec == argument_spec
    assert validator._valid_parameter_names == {'param1', 'param2 (p2, param_two)'}

