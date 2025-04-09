# file: pytutils/env.py:44-67
# asked: {"lines": [44, 55, 57, 59, 60, 62, 64, 65, 67], "branches": [[59, 60], [59, 67], [64, 59], [64, 65]]}
# gained: {"lines": [44, 55, 57, 59, 60, 62, 64, 65, 67], "branches": [[59, 60], [59, 67], [64, 59], [64, 65]]}

import os
import collections
import pytest
from unittest import mock
from pytutils.env import load_env_file

def test_load_env_file(monkeypatch):
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    
    mock_environ = {
        'HOME': '/mock/home',
        'PATH': '/mock/path'
    }
    monkeypatch.setattr(os, 'environ', mock_environ)
    
    result = load_env_file(lines, write_environ=mock_environ)
    
    assert 'TEST' in result
    assert 'THISIS' in result
    assert 'YOLO' in result
    
    assert result['TEST'] == '/mock/home/yeee-/mock/path'
    assert result['THISIS'] == '/mock/home/a/test'
    assert result['YOLO'] == '/mock/home/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    
    assert mock_environ['TEST'] == '/mock/home/yeee-/mock/path'
    assert mock_environ['THISIS'] == '/mock/home/a/test'
    assert mock_environ['YOLO'] == '/mock/home/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'

def test_load_env_file_no_write_environ(monkeypatch):
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    
    mock_environ = {
        'HOME': '/mock/home',
        'PATH': '/mock/path'
    }
    monkeypatch.setattr(os, 'environ', mock_environ)
    
    result = load_env_file(lines, write_environ=None)
    
    assert 'TEST' in result
    assert 'THISIS' in result
    assert 'YOLO' in result
    
    assert result['TEST'] == '/mock/home/yeee-/mock/path'
    assert result['THISIS'] == '/mock/home/a/test'
    assert result['YOLO'] == '/mock/home/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
