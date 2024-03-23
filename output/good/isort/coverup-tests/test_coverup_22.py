# file isort/format.py:77-86
# lines [78, 79, 80, 81, 82, 83, 84, 85, 86]
# branches ['79->80', '79->86', '82->83', '82->84', '84->79', '84->85']

import sys
from unittest.mock import patch

import pytest

from isort.format import ask_whether_to_apply_changes_to_file


@pytest.fixture
def mock_input(mocker):
    return mocker.patch('builtins.input')


@pytest.fixture
def mock_sys_exit(mocker):
    return mocker.patch('sys.exit', side_effect=SystemExit(1))


def test_ask_whether_to_apply_changes_to_file_yes(mock_input):
    mock_input.return_value = 'yes'
    assert ask_whether_to_apply_changes_to_file('dummy_file.py') is True
    mock_input.assert_called_once()


def test_ask_whether_to_apply_changes_to_file_no(mock_input):
    mock_input.return_value = 'no'
    assert ask_whether_to_apply_changes_to_file('dummy_file.py') is False
    mock_input.assert_called_once()


def test_ask_whether_to_apply_changes_to_file_quit(mock_input, mock_sys_exit):
    mock_input.return_value = 'quit'
    with pytest.raises(SystemExit):
        ask_whether_to_apply_changes_to_file('dummy_file.py')
    mock_input.assert_called_once()
    mock_sys_exit.assert_called_once_with(1)
