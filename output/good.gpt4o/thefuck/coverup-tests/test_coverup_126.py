# file thefuck/system/unix.py:22-37
# lines []
# branches ['29->37', '34->37']

import pytest
from unittest import mock
from thefuck.system.unix import get_key, const

def test_get_key_escape_sequence_up(mocker):
    mocker.patch('thefuck.system.unix.getch', side_effect=['\x1b', '[', 'A'])
    result = get_key()
    assert result == const.KEY_UP

def test_get_key_escape_sequence_down(mocker):
    mocker.patch('thefuck.system.unix.getch', side_effect=['\x1b', '[', 'B'])
    result = get_key()
    assert result == const.KEY_DOWN

def test_get_key_other_escape_sequence(mocker):
    mocker.patch('thefuck.system.unix.getch', side_effect=['\x1b', '[', 'C'])
    result = get_key()
    assert result == '\x1b'
