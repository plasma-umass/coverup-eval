# file: pytutils/env.py:7-10
# asked: {"lines": [7, 8, 9, 10], "branches": []}
# gained: {"lines": [7, 8, 9, 10], "branches": []}

import os
import pytest

from pytutils.env import expand

def test_expand_with_env_variable(monkeypatch):
    monkeypatch.setenv('MY_VAR', 'my_value')
    result = expand('$MY_VAR/some/path')
    assert result == 'my_value/some/path'

def test_expand_with_user_home(monkeypatch):
    monkeypatch.setenv('HOME', '/home/testuser')
    result = expand('~/some/path')
    assert result == '/home/testuser/some/path'

def test_expand_with_nonexistent_env_variable():
    result = expand('$NON_EXISTENT_VAR/some/path')
    assert result == '$NON_EXISTENT_VAR/some/path'

def test_expand_with_nonexistent_user():
    result = expand('~nonexistentuser/some/path')
    assert result == '~nonexistentuser/some/path'
