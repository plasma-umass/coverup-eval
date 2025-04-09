# file isort/format.py:77-86
# lines [77, 78, 79, 80, 81, 82, 83, 84, 85, 86]
# branches ['79->80', '79->86', '82->83', '82->84', '84->79', '84->85']

import pytest
from unittest import mock
import sys
from isort.format import ask_whether_to_apply_changes_to_file

def test_ask_whether_to_apply_changes_to_file_yes(mocker):
    mocker.patch('builtins.input', return_value='y')
    assert ask_whether_to_apply_changes_to_file('dummy_path') == True

def test_ask_whether_to_apply_changes_to_file_no(mocker):
    mocker.patch('builtins.input', return_value='n')
    assert ask_whether_to_apply_changes_to_file('dummy_path') == False

def test_ask_whether_to_apply_changes_to_file_quit(mocker):
    mocker.patch('builtins.input', return_value='q')
    with pytest.raises(SystemExit) as e:
        ask_whether_to_apply_changes_to_file('dummy_path')
    assert e.type == SystemExit
    assert e.value.code == 1

def test_ask_whether_to_apply_changes_to_file_invalid_then_yes(mocker):
    inputs = iter(['invalid', 'y'])
    mocker.patch('builtins.input', lambda _: next(inputs))
    assert ask_whether_to_apply_changes_to_file('dummy_path') == True

def test_ask_whether_to_apply_changes_to_file_invalid_then_no(mocker):
    inputs = iter(['invalid', 'n'])
    mocker.patch('builtins.input', lambda _: next(inputs))
    assert ask_whether_to_apply_changes_to_file('dummy_path') == False

def test_ask_whether_to_apply_changes_to_file_invalid_then_quit(mocker):
    inputs = iter(['invalid', 'q'])
    mocker.patch('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit) as e:
        ask_whether_to_apply_changes_to_file('dummy_path')
    assert e.type == SystemExit
    assert e.value.code == 1
