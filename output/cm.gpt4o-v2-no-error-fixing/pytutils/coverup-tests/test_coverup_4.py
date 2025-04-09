# file: pytutils/env.py:7-10
# asked: {"lines": [7, 8, 9, 10], "branches": []}
# gained: {"lines": [7, 8, 9, 10], "branches": []}

import os
import pytest

from pytutils.env import expand

def test_expand_with_env_variable(monkeypatch):
    monkeypatch.setenv('MY_VAR', 'my_value')
    result = expand('$MY_VAR')
    assert result == 'my_value'

def test_expand_with_user_home(monkeypatch):
    monkeypatch.setenv('HOME', '/home/testuser')
    result = expand('~')
    assert result == '/home/testuser'

def test_expand_with_combined(monkeypatch):
    monkeypatch.setenv('MY_VAR', 'my_value')
    monkeypatch.setenv('HOME', '/home/testuser')
    result = expand('~/path/$MY_VAR')
    assert result == '/home/testuser/path/my_value'
