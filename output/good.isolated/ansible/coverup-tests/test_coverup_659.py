# file lib/ansible/modules/iptables.py:581-583
# lines [581, 582, 583]
# branches ['582->exit', '582->583']

import pytest
from ansible.modules.iptables import append_wait

def test_append_wait_with_param(mocker):
    # Mock the extend method to prevent actual changes
    mock_rule = mocker.MagicMock()

    # Call the function with a parameter
    append_wait(mock_rule, 'some_param', '--flag')

    # Assert that extend was called with the correct parameters
    mock_rule.extend.assert_called_once_with(['--flag', 'some_param'])

def test_append_wait_without_param(mocker):
    # Mock the extend method to prevent actual changes
    mock_rule = mocker.MagicMock()

    # Call the function without a parameter
    append_wait(mock_rule, None, '--flag')

    # Assert that extend was not called since param is None
    mock_rule.extend.assert_not_called()
