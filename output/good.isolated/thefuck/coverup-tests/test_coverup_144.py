# file thefuck/system/unix.py:22-37
# lines []
# branches ['29->37']

import pytest
from thefuck.system import unix
from thefuck import const
from unittest.mock import Mock


@pytest.fixture
def mock_getch(mocker):
    return mocker.patch('thefuck.system.unix.getch')


def test_get_key_esc_sequence(mock_getch):
    mock_getch.side_effect = ['\x1b', '[', 'A']
    assert unix.get_key() == const.KEY_UP
    mock_getch.assert_called()

    mock_getch.side_effect = ['\x1b', '[', 'B']
    assert unix.get_key() == const.KEY_DOWN
    mock_getch.assert_called()

    mock_getch.side_effect = ['\x1b', 'O', 'C']  # Changed from ['\x1b', '[', 'C']
    assert unix.get_key() == '\x1b'  # Changed from 'C'
    mock_getch.assert_called()
