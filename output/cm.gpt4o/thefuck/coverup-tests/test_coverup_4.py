# file thefuck/types.py:89-109
# lines [89, 103, 104, 105, 106, 107, 108, 109]
# branches []

import pytest
from thefuck.types import Rule

class MockCommand:
    pass

def test_rule_initialization():
    name = "test_rule"
    match = lambda x: True
    get_new_command = lambda x: "new_command"
    enabled_by_default = True
    side_effect = lambda x, y: None
    priority = 100
    requires_output = False

    rule = Rule(name, match, get_new_command, enabled_by_default, side_effect, priority, requires_output)

    assert rule.name == name
    assert rule.match(MockCommand())
    assert rule.get_new_command(MockCommand()) == "new_command"
    assert rule.enabled_by_default == enabled_by_default
    assert rule.side_effect(MockCommand(), "new_command") is None
    assert rule.priority == priority
    assert rule.requires_output == requires_output
