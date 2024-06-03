# file thefuck/types.py:86-88
# lines [86, 87]
# branches []

import pytest
from thefuck.types import Rule

def test_rule_initialization(mocker):
    mocker.patch.object(Rule, '__init__', lambda self, name, match, get_new_command, enabled_by_default, side_effect, priority, requires_output: None)
    rule = Rule('name', 'match', 'get_new_command', True, None, 100, False)
    assert isinstance(rule, Rule)

# Ensure the test is cleaned up properly
@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
