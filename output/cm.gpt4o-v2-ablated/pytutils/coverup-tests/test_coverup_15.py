# file: pytutils/env.py:44-67
# asked: {"lines": [44, 55, 57, 59, 60, 62, 64, 65, 67], "branches": [[59, 60], [59, 67], [64, 59], [64, 65]]}
# gained: {"lines": [44, 55, 57, 59, 60, 62, 64, 65, 67], "branches": [[59, 60], [59, 67], [64, 59], [64, 65]]}

import os
import collections
import pytest
from unittest import mock
from pytutils.env import load_env_file

def test_load_env_file(monkeypatch):
    # Mock environment variables
    mock_environ = {}
    monkeypatch.setattr(os, 'environ', mock_environ)

    # Test data
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]

    # Mock the expand function to return predictable results
    def mock_expand(value):
        return value.replace('${HOME}', '/home/user').replace('~', '/home/user').replace('$PATH', '/usr/bin').replace('$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST', '')

    monkeypatch.setattr('pytutils.env.expand', mock_expand)

    # Call the function
    result = load_env_file(lines, write_environ=mock_environ)

    # Expected result
    expected = collections.OrderedDict([
        ('TEST', '/home/user/yeee-/usr/bin'),
        ('THISIS', '/home/user/a/test'),
        ('YOLO', '/home/user/swaggins/')
    ])

    # Assertions
    assert result == expected
    assert mock_environ == expected

    # Clean up
    for key in expected.keys():
        del os.environ[key]

def test_load_env_file_no_write_environ(monkeypatch):
    # Test data
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]

    # Mock the expand function to return predictable results
    def mock_expand(value):
        return value.replace('${HOME}', '/home/user').replace('~', '/home/user').replace('$PATH', '/usr/bin').replace('$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST', '')

    monkeypatch.setattr('pytutils.env.expand', mock_expand)

    # Call the function without write_environ
    result = load_env_file(lines, write_environ=None)

    # Expected result
    expected = collections.OrderedDict([
        ('TEST', '/home/user/yeee-/usr/bin'),
        ('THISIS', '/home/user/a/test'),
        ('YOLO', '/home/user/swaggins/')
    ])

    # Assertions
    assert result == expected
