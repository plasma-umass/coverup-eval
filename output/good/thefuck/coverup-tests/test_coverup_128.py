# file thefuck/types.py:186-199
# lines [193, 194, 195, 196, 197, 198, 199]
# branches ['194->195', '194->196', '196->exit', '196->197']

import pytest
from thefuck.types import Rule, Command, CorrectedCommand

class TestRule(Rule):
    def __init__(self):
        super(TestRule, self).__init__(
            name='test_rule',
            match=lambda x: True,
            get_new_command=lambda x: ['new_command1', 'new_command2'],
            enabled_by_default=True,
            side_effect=None,
            priority=1,
            requires_output=False
        )

@pytest.fixture
def command():
    return Command('test', 'test')

@pytest.fixture
def rule():
    return TestRule()

def test_get_corrected_commands(rule, command):
    corrected_commands = list(rule.get_corrected_commands(command))
    assert len(corrected_commands) == 2
    assert corrected_commands[0].script == 'new_command1'
    assert corrected_commands[0].priority == 1
    assert corrected_commands[1].script == 'new_command2'
    assert corrected_commands[1].priority == 2
