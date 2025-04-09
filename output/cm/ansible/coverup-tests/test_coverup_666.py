# file lib/ansible/modules/iptables.py:566-568
# lines [566, 567, 568]
# branches ['567->exit', '567->568']

import pytest
from ansible.modules.iptables import append_csv

def test_append_csv_single_value(mocker):
    # Mock the extend method to verify it's called with correct parameters
    mock_rule = mocker.MagicMock()

    # Call the function with a single value
    append_csv(mock_rule, ['value1'], '-f')

    # Assert the extend method was called once with the correct flag and parameter
    mock_rule.extend.assert_called_once_with(['-f', 'value1'])

def test_append_csv_multiple_values(mocker):
    # Mock the extend method to verify it's called with correct parameters
    mock_rule = mocker.MagicMock()

    # Call the function with multiple values
    append_csv(mock_rule, ['value1', 'value2', 'value3'], '-f')

    # Assert the extend method was called once with the correct flag and joined parameters
    mock_rule.extend.assert_called_once_with(['-f', 'value1,value2,value3'])

def test_append_csv_no_values(mocker):
    # Mock the extend method to verify it's not called when param is empty
    mock_rule = mocker.MagicMock()

    # Call the function with no values
    append_csv(mock_rule, [], '-f')

    # Assert the extend method was not called
    mock_rule.extend.assert_not_called()

def test_append_csv_none_value(mocker):
    # Mock the extend method to verify it's not called when param is None
    mock_rule = mocker.MagicMock()

    # Call the function with None
    append_csv(mock_rule, None, '-f')

    # Assert the extend method was not called
    mock_rule.extend.assert_not_called()
