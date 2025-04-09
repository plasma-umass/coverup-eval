# file: pytutils/env.py:44-67
# asked: {"lines": [44, 55, 57, 59, 60, 62, 64, 65, 67], "branches": [[59, 60], [59, 67], [64, 59], [64, 65]]}
# gained: {"lines": [44, 55, 57, 59, 60, 62, 64, 65, 67], "branches": [[59, 60], [59, 67], [64, 65]]}

import collections
import os
import pytest
from unittest import mock
from pytutils.env import load_env_file

def test_load_env_file(monkeypatch):
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    
    mock_environ = {}
    monkeypatch.setattr(os, 'environ', mock_environ)
    
    with mock.patch('pytutils.env.expand', side_effect=lambda x: x.replace('${HOME}', '/home/user').replace('~', '/home/user')):
        result = load_env_file(lines, write_environ=mock_environ)
    
    expected = collections.OrderedDict([
        ('TEST', '/home/user/yeee-$PATH'),
        ('THISIS', '/home/user/a/test'),
        ('YOLO', '/home/user/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ])
    
    assert result == expected
    assert mock_environ == expected
