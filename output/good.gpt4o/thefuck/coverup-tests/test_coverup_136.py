# file thefuck/types.py:111-120
# lines [112, 113, 114, 115, 116, 117, 118, 120]
# branches ['112->113', '112->120']

import pytest
from thefuck.types import Rule

def test_rule_equality():
    match_func = lambda x: True
    get_new_command_func = lambda x: "new_command"

    rule1 = Rule(
        name="test_rule",
        match=match_func,
        get_new_command=get_new_command_func,
        enabled_by_default=True,
        side_effect=None,
        priority=1000,
        requires_output=True
    )

    rule2 = Rule(
        name="test_rule",
        match=match_func,
        get_new_command=get_new_command_func,
        enabled_by_default=True,
        side_effect=None,
        priority=1000,
        requires_output=True
    )

    rule3 = Rule(
        name="different_rule",
        match=lambda x: False,
        get_new_command=lambda x: "different_command",
        enabled_by_default=False,
        side_effect=None,
        priority=500,
        requires_output=False
    )

    # Test equality with the same attributes
    assert rule1 == rule2

    # Test inequality with different attributes
    assert rule1 != rule3

    # Test inequality with a different type
    assert rule1 != "not_a_rule"
