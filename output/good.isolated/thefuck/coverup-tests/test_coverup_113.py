# file thefuck/logs.py:39-40
# lines [39, 40]
# branches []

import pytest
from thefuck.logs import rule_failed, exception
from thefuck.types import Rule

# Mocking the exception function to verify it's called with correct arguments
def test_rule_failed(mocker):
    mock_exception = mocker.patch('thefuck.logs.exception')
    rule = Rule(name='test_rule', match=lambda x: True, get_new_command=lambda x: 'new_command',
                enabled_by_default=True, side_effect=None, priority=0, requires_output=False)
    try:
        raise ValueError("Test exception")
    except:
        rule_failed(rule, exc_info=True)
    
    # Assert that the exception function was called with the correct rule name
    mock_exception.assert_called_once_with(u'Rule test_rule', True)

    # Clean up by unpatching
    mocker.stopall()
