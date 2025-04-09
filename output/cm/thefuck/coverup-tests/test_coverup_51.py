# file thefuck/corrector.py:52-78
# lines [52, 59, 60, 61, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 77, 78]
# branches ['77->exit', '77->78']

import pytest
from thefuck.types import CorrectedCommand
from thefuck.corrector import organize_commands
from unittest.mock import patch


@pytest.fixture
def mock_log_debug(mocker):
    return mocker.patch('thefuck.corrector.logs.debug')


def test_organize_commands_with_duplicates(mock_log_debug):
    # Create a list of CorrectedCommand with duplicates
    commands = [CorrectedCommand('test', None, priority=900),
                CorrectedCommand('test', None, priority=900),
                CorrectedCommand('unique', None, priority=800),
                CorrectedCommand('another', None, priority=1000)]

    # Convert the list to an iterator
    commands_iter = iter(commands)

    # Call the organize_commands function with the iterator
    result = list(organize_commands(commands_iter))

    # Check that the result contains no duplicates and is sorted by priority
    assert result == [CorrectedCommand('test', None, priority=900),
                      CorrectedCommand('unique', None, priority=800),
                      CorrectedCommand('another', None, priority=1000)]

    # Check that the debug log was called with the correct string
    expected_log_message = u'Corrected commands: {}'.format(
        ', '.join(u'{}'.format(cmd) for cmd in result))
    mock_log_debug.assert_called_once_with(expected_log_message)


def test_organize_commands_empty_iterator(mock_log_debug):
    # Create an empty iterator
    empty_commands_iter = iter([])

    # Call the organize_commands function with the empty iterator
    result = list(organize_commands(empty_commands_iter))

    # Check that the result is an empty list
    assert result == []

    # Check that the debug log was not called
    mock_log_debug.assert_not_called()
