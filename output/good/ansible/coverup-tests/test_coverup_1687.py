# file lib/ansible/constants.py:23-30
# lines [25, 26, 27, 28, 29, 30]
# branches []

import pytest
from ansible.constants import _warning

def test_warning_with_display(mocker):
    # Mock the Display class and its warning method
    mock_display_class = mocker.patch('ansible.utils.display.Display')
    mock_warning = mock_display_class.return_value.warning

    # Call the _warning function which should use the Display class
    _warning("Test warning message with Display")

    # Assert that the Display class was used
    assert mock_warning.called
    mock_warning.assert_called_once_with("Test warning message with Display")

def test_warning_without_display(mocker):
    # Mock the Display class to raise an exception
    mocker.patch('ansible.utils.display.Display', side_effect=Exception)

    # Mock sys.stderr to capture output
    mock_stderr = mocker.patch('sys.stderr')

    # Call the _warning function which should fall back to sys.stderr.write
    _warning("Test warning message without Display")

    # Assert that sys.stderr.write was called with the correct message
    assert mock_stderr.write.called
    mock_stderr.write.assert_called_once_with(' [WARNING] Test warning message without Display\n')
