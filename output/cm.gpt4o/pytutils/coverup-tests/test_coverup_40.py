# file pytutils/env.py:44-67
# lines []
# branches ['64->59']

import pytest
import collections
import os
from unittest import mock
from pytutils.env import load_env_file

def test_load_env_file_with_write_environ_none():
    lines = [
        'TEST=${HOME}/yeee-$PATH',
        'THISIS=~/a/test',
        'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'
    ]
    
    with mock.patch.dict(os.environ, {}, clear=True):
        with mock.patch('os.path.expanduser', side_effect=lambda x: x):
            result = load_env_file(lines, write_environ=None)
            
            assert result == collections.OrderedDict([
                ('TEST', os.path.expandvars('${HOME}/yeee-$PATH')),
                ('THISIS', '~/a/test'),
                ('YOLO', '~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
            ])
            
            # Ensure os.environ is not modified
            assert 'TEST' not in os.environ
            assert 'THISIS' not in os.environ
            assert 'YOLO' not in os.environ
