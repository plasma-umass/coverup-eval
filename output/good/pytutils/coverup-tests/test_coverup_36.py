# file pytutils/env.py:44-67
# lines []
# branches ['64->59']

import os
import pytest
from collections import OrderedDict
from pytutils.env import load_env_file

def test_load_env_file_with_none_write_environ(mocker):
    # Mock the os.environ to ensure it is not modified during the test
    mock_environ = mocker.patch.dict(os.environ, {}, clear=True)
    
    lines = ['TEST_VAR=VALUE']
    result = load_env_file(lines, write_environ=None)
    
    # Assert that the result is as expected
    assert result == OrderedDict([('TEST_VAR', 'VALUE')])
    
    # Assert that os.environ was not modified
    assert len(os.environ) == 0
