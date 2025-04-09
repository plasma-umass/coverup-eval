# file thefuck/types.py:169-184
# lines [169, 176, 177, 179, 180, 181, 182, 183, 184]
# branches ['176->177', '176->179', '181->exit', '181->182']

import pytest
from unittest import mock
from thefuck.types import Rule
import sys

class MockCommand:
    def __init__(self, output):
        self.output = output

@pytest.fixture
def mock_logs(mocker):
    return mocker.patch('thefuck.types.logs')

@pytest.fixture
def mock_rule(mocker):
    rule = Rule(
        name='mock_rule',
        match=mocker.Mock(),
        get_new_command=mocker.Mock(),
        enabled_by_default=True,
        side_effect=None,
        priority=1000,
        requires_output=True
    )
    return rule

def test_rule_is_match_no_output(mock_rule, mock_logs):
    command = MockCommand(output=None)
    assert not mock_rule.is_match(command)
    mock_rule.match.assert_not_called()

def test_rule_is_match_with_output(mock_rule, mock_logs):
    command = MockCommand(output='some output')
    mock_rule.match.return_value = True
    assert mock_rule.is_match(command)
    mock_rule.match.assert_called_once_with(command)

def test_rule_is_match_exception(mock_rule, mock_logs):
    command = MockCommand(output='some output')
    mock_rule.match.side_effect = Exception('Test exception')
    assert not mock_rule.is_match(command)
    mock_logs.rule_failed.assert_called_once()
    exc_info = mock_logs.rule_failed.call_args[0][1]
    assert exc_info[0] == Exception
    assert str(exc_info[1]) == 'Test exception'
