# file pytutils/env.py:44-67
# lines [44, 55, 57, 59, 60, 62, 64, 65, 67]
# branches ['59->60', '59->67', '64->59', '64->65']

import os
import collections
import pytest
from unittest import mock
from pytutils.env import load_env_file

def test_load_env_file(mocker):
    # Mock the os.environ to ensure no side effects
    mock_environ = mocker.patch.dict(os.environ, {}, clear=True)
    
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    
    # Call the function with the test lines
    result = load_env_file(lines, write_environ=mock_environ)
    
    # Assertions to verify the expected behavior
    assert 'TEST' in result
    assert 'THISIS' in result
    assert 'YOLO' in result
    
    assert result['TEST'] == os.path.expandvars('${HOME}/yeee-$PATH')
    assert result['THISIS'] == os.path.expanduser('~/a/test')
    assert result['YOLO'] == os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    
    # Ensure the mock environment was updated correctly
    assert mock_environ['TEST'] == os.path.expandvars('${HOME}/yeee-$PATH')
    assert mock_environ['THISIS'] == os.path.expanduser('~/a/test')
    assert mock_environ['YOLO'] == os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
