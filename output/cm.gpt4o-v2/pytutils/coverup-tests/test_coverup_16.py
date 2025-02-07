# file: pytutils/env.py:44-67
# asked: {"lines": [44, 55, 57, 59, 60, 62, 64, 65, 67], "branches": [[59, 60], [59, 67], [64, 59], [64, 65]]}
# gained: {"lines": [44, 55, 57, 59, 60, 62, 64, 65, 67], "branches": [[59, 60], [59, 67], [64, 59], [64, 65]]}

import pytest
import collections
import os
from unittest import mock
from pytutils.env import load_env_file, parse_env_file_contents, expand

def test_load_env_file(monkeypatch):
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    
    mock_environ = {}
    monkeypatch.setattr(os, 'environ', mock_environ)
    
    result = load_env_file(lines, write_environ=mock_environ)
    
    assert isinstance(result, collections.OrderedDict)
    assert 'TEST' in result
    assert 'THISIS' in result
    assert 'YOLO' in result
    
    assert result['TEST'] == os.path.expandvars('${HOME}/yeee-$PATH')
    assert result['THISIS'] == os.path.expanduser('~/a/test')
    assert result['YOLO'] == os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    
    assert mock_environ['TEST'] == os.path.expandvars('${HOME}/yeee-$PATH')
    assert mock_environ['THISIS'] == os.path.expanduser('~/a/test')
    assert mock_environ['YOLO'] == os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')

def test_load_env_file_no_write_environ():
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    
    result = load_env_file(lines, write_environ=None)
    
    assert isinstance(result, collections.OrderedDict)
    assert 'TEST' in result
    assert 'THISIS' in result
    assert 'YOLO' in result
    
    assert result['TEST'] == os.path.expandvars('${HOME}/yeee-$PATH')
    assert result['THISIS'] == os.path.expanduser('~/a/test')
    assert result['YOLO'] == os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
