# file thefuck/types.py:122-128
# lines [122, 123, 125, 126, 127, 128]
# branches []

import pytest
from thefuck.types import Rule

@pytest.fixture
def rule_instance():
    return Rule(name='test_rule', match=lambda x: True, get_new_command=lambda x: 'new_command',
                enabled_by_default=True, side_effect=None, priority=900, requires_output=False)

def test_rule_repr(rule_instance):
    expected_repr = ("Rule(name=test_rule, match={}, get_new_command={}, "
                     "enabled_by_default=True, side_effect=None, priority=900, requires_output=False)"
                     .format(rule_instance.match, rule_instance.get_new_command))
    assert repr(rule_instance) == expected_repr
