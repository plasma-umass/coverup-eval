# file lib/ansible/modules/iptables.py:541-550
# lines []
# branches ['546->exit']

import pytest
from ansible.modules.iptables import append_param

def test_append_param_with_bang_character(mocker):
    # Mock the extend method to prevent actual changes
    mock_rule = mocker.MagicMock()

    # Call the function with a parameter starting with '!'
    append_param(mock_rule, '!value', '-f', False)

    # Assert that the extend method was called with the correct parameters
    mock_rule.extend.assert_called_with(['!', '-f', 'value'])

    # Call the function with a parameter not starting with '!'
    append_param(mock_rule, 'value', '-f', False)

    # Assert that the extend method was called with the correct parameters
    mock_rule.extend.assert_called_with(['-f', 'value'])

def test_append_param_with_none(mocker):
    # Mock the extend method to prevent actual changes
    mock_rule = mocker.MagicMock()

    # Call the function with None as the parameter
    append_param(mock_rule, None, '-f', False)

    # Assert that the extend method was not called
    mock_rule.extend.assert_not_called()
