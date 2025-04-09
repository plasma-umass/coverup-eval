# file: isort/format.py:77-86
# asked: {"lines": [77, 78, 79, 80, 81, 82, 83, 84, 85, 86], "branches": [[79, 80], [79, 86], [82, 83], [82, 84], [84, 79], [84, 85]]}
# gained: {"lines": [77, 78, 79, 80, 81, 82, 83, 84, 85, 86], "branches": [[79, 80], [79, 86], [82, 83], [82, 84], [84, 79], [84, 85]]}

import pytest
import sys
from unittest import mock

from isort.format import ask_whether_to_apply_changes_to_file

def test_ask_whether_to_apply_changes_to_file_yes(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    assert ask_whether_to_apply_changes_to_file('dummy_path') == True

def test_ask_whether_to_apply_changes_to_file_no(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    assert ask_whether_to_apply_changes_to_file('dummy_path') == False

def test_ask_whether_to_apply_changes_to_file_quit(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'q')
    with pytest.raises(SystemExit) as e:
        ask_whether_to_apply_changes_to_file('dummy_path')
    assert e.type == SystemExit
    assert e.value.code == 1

def test_ask_whether_to_apply_changes_to_file_invalid_then_yes(monkeypatch):
    inputs = iter(['invalid', 'y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert ask_whether_to_apply_changes_to_file('dummy_path') == True

def test_ask_whether_to_apply_changes_to_file_invalid_then_no(monkeypatch):
    inputs = iter(['invalid', 'n'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert ask_whether_to_apply_changes_to_file('dummy_path') == False

def test_ask_whether_to_apply_changes_to_file_invalid_then_quit(monkeypatch):
    inputs = iter(['invalid', 'q'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit) as e:
        ask_whether_to_apply_changes_to_file('dummy_path')
    assert e.type == SystemExit
    assert e.value.code == 1
