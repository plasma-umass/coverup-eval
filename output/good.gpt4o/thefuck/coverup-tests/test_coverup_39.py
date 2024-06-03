# file thefuck/types.py:122-128
# lines [122, 123, 125, 126, 127, 128]
# branches []

import pytest
from unittest.mock import Mock

# Assuming the Rule class is imported from thefuck.types
from thefuck.types import Rule

@pytest.fixture
def mock_rule():
    rule = Rule(
        name="test_rule",
        match=Mock(),
        get_new_command=Mock(),
        enabled_by_default=True,
        side_effect=Mock(),
        priority=100,
        requires_output=False
    )
    return rule

def test_rule_repr(mock_rule):
    expected_repr = 'Rule(name=test_rule, match=<Mock id=\'{}\'>, get_new_command=<Mock id=\'{}\'>, enabled_by_default=True, side_effect=<Mock id=\'{}\'>, priority=100, requires_output=False)'.format(
        id(mock_rule.match), id(mock_rule.get_new_command), id(mock_rule.side_effect))
    assert repr(mock_rule) == expected_repr
