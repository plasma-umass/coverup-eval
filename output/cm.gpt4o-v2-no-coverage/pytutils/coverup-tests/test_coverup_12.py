# file: pytutils/env.py:7-10
# asked: {"lines": [7, 8, 9, 10], "branches": []}
# gained: {"lines": [7, 8, 9, 10], "branches": []}

import os
import pytest

from pytutils.env import expand

def test_expand_with_env_variable(monkeypatch):
    monkeypatch.setenv('MYVAR', 'myvalue')
    result = expand('$MYVAR/some/path')
    assert result == 'myvalue/some/path'

def test_expand_with_user_directory(monkeypatch):
    monkeypatch.setattr(os.path, 'expanduser', lambda x: x.replace('~', '/home/user'))
    result = expand('~/some/path')
    assert result == '/home/user/some/path'

def test_expand_with_both_env_and_user(monkeypatch):
    monkeypatch.setenv('MYVAR', 'myvalue')
    monkeypatch.setattr(os.path, 'expanduser', lambda x: x.replace('~', '/home/user'))
    result = expand('$MYVAR/~/some/path')
    assert result == 'myvalue//home/user/some/path'
