# file thefuck/system/unix.py:22-37
# lines [22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 37]
# branches ['25->26', '25->27', '27->28', '27->37', '29->30', '29->37', '32->33', '32->34', '34->35', '34->37']

import pytest
from thefuck.system import unix
from thefuck import const
from unittest.mock import patch


@pytest.fixture
def mock_getch(mocker):
    return mocker.patch('thefuck.system.unix.getch')


def test_get_key_arrow_up(mock_getch):
    mock_getch.side_effect = ['\x1b', '[', 'A']
    assert unix.get_key() == const.KEY_UP


def test_get_key_arrow_down(mock_getch):
    mock_getch.side_effect = ['\x1b', '[', 'B']
    assert unix.get_key() == const.KEY_DOWN


def test_get_key_mapped_key(mock_getch):
    for key, value in const.KEY_MAPPING.items():
        mock_getch.return_value = key
        assert unix.get_key() == value


def test_get_key_unmapped_key(mock_getch):
    mock_getch.return_value = 'x'
    assert unix.get_key() == 'x'


def test_get_key_escape_sequence_not_arrow(mock_getch):
    mock_getch.side_effect = ['\x1b', '[', 'C']
    assert unix.get_key() == '\x1b'
